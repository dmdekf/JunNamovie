from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, View
from django.middleware.csrf import _compare_salted_tokens
from accounts.oauth.providers.google import GoogleLoginMixin
# Create your views here.


class SocialLoginCallbackView(GoogleLoginMixin, View):

    success_url = settings.LOGIN_REDIRECT_URL
    failure_url = settings.LOGIN_URL
    required_profiles = ['email']
    model = get_user_model()

    def get(self, request, *args, **kwargs):

        provider = kwargs.get('provider')

        if provider == 'google':
            csrf_token = request.GET.get('state')
            code = request.GET.get('code')
            # state(csrf_token)이 잘못된 경우
            if not _compare_salted_tokens(csrf_token, request.COOKIES.get('csrftoken')):
                messages.error(request, '잘못된 경로로 로그인하셨습니다.',
                               extra_tags='danger')
                return HttpResponseRedirect(self.failure_url)
            is_success, error = self.login_with_google(csrf_token, code)
            if not is_success:  # 로그인 실패할 경우
                messages.error(request, error, extra_tags='danger')
            return HttpResponseRedirect(self.success_url if is_success else self.failure_url)

        return HttpResponseRedirect(self.failure_url)

    def set_session(self, **kwargs):
        for key, value in kwargs.items():
            self.request.session[key] = value


def login(request):
    if request.user.is_authenticated:
        token = request.GET["code"]
        conlole.log(token)
        return redirect('movies:index')
    return render(request, 'accounts/login.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    return render(request, 'accounts/login.html')
