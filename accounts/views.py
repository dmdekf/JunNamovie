from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


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
