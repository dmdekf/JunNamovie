from django.conf import settings
from django.contrib.auth import login
import requests


class GoogleClient:
    client_id = '525887776863-6hlane191e75rv8pis7vi05st3j0rfci.apps.googleusercontent.com'
    secret_key = 'd4n3BebrDDirMUqGd7wV8lpg'
    grant_type = 'authorization_code'

    auth_url = 'https://www.googleapis.com/oauth2/v4/token'
    profile_url = 'https://www.googleapis.com/auth/userinfo.profile'

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def get_access_token(self, state, code):
        res = requests.get(self.auth_url, params={'client_id': self.client_id, 'client_secret': self.secret_key,
                                                  'grant_type': self.grant_type, 'state': state, 'code': code})
        return res.ok, res.json()

    def get_profile(self, access_token, token_type='Bearer'):
        res = requests.get(self.profile_url, headers={
                           'Authorization': '{} {}'.format(token_type, access_token)}).json()

        if res.get('resultcode') != '00':
            return False, res.get('message')
        else:
            return True, res.get('response')


class GoogleLoginMixin:
    google_client = GoogleClient()

    def login_with_google(self, state, code):

        # 인증토근 발급
        is_success, token_infos = self.google_client.get_access_token(
            state, code)

        if not is_success:
            return False, '{} [{}]'.format(token_infos.get('error_desc'), token_infos.get('error'))

        access_token = token_infos.get('access_token')
        refresh_token = token_infos.get('refresh_token')
        expires_in = token_infos.get('expires_in')
        token_type = token_infos.get('token_type')

        # 네이버 프로필 얻기
        is_success, profiles = self.get_google_profile(
            access_token, token_type)
        if not is_success:
            return False, profiles

        # 사용자 생성 또는 업데이트
        user, created = self.model.objects.get_or_create(
            email=profiles.get('email'))
        if created:  # 사용자 생성할 경우
            user.set_password(None)
        user.name = profiles.get('email')
        user.is_active = True
        user.save()

        # 로그인
        login(self.request, user, 'user.oauth.backends.GoogleBackend')

        # 세션데이터 추가
        self.set_session(access_token=access_token, refresh_token=refresh_token,
                         expires_in=expires_in, token_type=token_type)
        print('-------------')
        print(set_session)
        print(access_token)
        print(self.set_session)
        return True, user

    def get_google_profile(self, access_token, token_type):
        is_success, profiles = self.google_client.get_profile(
            access_token, token_type)

        if not is_success:
            return False, profiles

        for profile in self.required_profiles:
            if profile not in profiles:
                return False, '{}은 필수정보입니다. 정보제공에 동의해주세요.'.format(profile)

        return True, profiles
