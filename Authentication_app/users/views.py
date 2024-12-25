from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def password_reset(request):
    return render(request, 'password_reset.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login,
    })


def password_reset_success(request):
    return render(request, 'password_reset_complete.html')

@login_required
def password_change_done(request):
    messages.success(request, 'Your password has been reset successfully.')
    return redirect('password_reset_success')