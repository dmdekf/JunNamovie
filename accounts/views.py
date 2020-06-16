from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, View
from django.middleware.csrf import _compare_salted_tokens
from django.http import HttpResponseRedirect
import requests
# Create your views here.


def getcode(request):
    code = request.GET['code']
    context = {
        'code': code
    }
    return render(request, 'accounts/getcode.html', context)


def login(request):
    if request.user.is_authenticated:
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
