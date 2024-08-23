from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password != repeat_password:
            return render(request, 'Core/auth/signup.html', {'error': 'Пароли не совпадают'})
        User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )
        return redirect('signin')
    return render(request, 'Core/auth/signup.html')

def signin(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'Core/auth/signin.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'Core/auth/signin.html')
def signout(request):
    logout(request)
    return redirect('signin')
    

def profile(request):
    return render(request, 'Core/auth/profile.html')