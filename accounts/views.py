from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            new_user = User.objects.create_user(username=username, password=password1, is_active=True)
            login(request, new_user)
            return redirect('/')

    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html')
