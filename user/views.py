from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    status = ''
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.check_password(request.POST['password']):
                login(request, user)
                return redirect(reverse('index'))
            else:
                status = 'PASSWORD DOES NOT MATCHED!'
        except User.DoesNotExist:
            status = 'USER DOES NOT EXISTS!'
    return render(request, 'login.html', {'status': status})


def register_view(request):
    status = ''
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            status = 'USER ALREADY EXISTS!'
        except User.DoesNotExist:
            user = User(email=request.POST['email'])
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect(reverse('index'))
    return render(request, 'register.html', {'status': status})


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def forgot_view(request):
    status = ''
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
        except User.DoesNotExist:
            status = 'USER DOES NOT EXISTS!'
    return render(request, 'forgot.html', {'status': status})


def reset_view(request):
    return render(request, 'reset.html')


@login_required
def change_view(request):
    status = 0
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.check_password(request.POST['old_password']):
                user.set_password(request.POST['new_password'])
                user.save()
            else:
                status = 1
        except User.DoesNotExist:
            status = 2
    return render(request, 'change.html', {'status': status})
