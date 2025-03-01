from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'The username is already taken!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration is successful! You can now log in.')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password!')
            return redirect('login')

    return render(request, 'login.html')

@login_required
def home(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password and password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('home')

        if User.objects.filter(username=username).exclude(id=user.id).exists():
            messages.error(request, 'The username is already taken!')
            return redirect('home')
        if User.objects.filter(email=email).exclude(id=user.id).exists():
            messages.error(request, 'Email is already registered!')
            return redirect('home')

        user.username = username
        user.email = email
        if password:
            user.set_password(password)
        user.save()

        messages.success(request, 'Profile data has been successfully updated!')
        return redirect('home')

    return render(request, 'home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out of your account.')
    return redirect('login')
