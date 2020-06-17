from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import MyUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

# soicial로그인 관련 코드 출력.


def getcode(request):
    code = request.GET['code']
    context = {
        'code': code
    }
    messages.success(request, '소셜 로그인 임시코드발급성공!')
    return render(request, 'accounts/getcode.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, '로그인되었습니다. 환영합니다!')
            return redirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('/')
    else:
        form = MyUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
