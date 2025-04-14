from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') #redirects to home after registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password =   form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid Username or password!')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

@login_required
def home_view(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    return redirect('home') #redirects back home after logout



