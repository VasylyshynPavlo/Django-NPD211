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
            messages.error(request, 'Паролі не співпадають!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ім\'я користувача вже зайняте!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email вже зареєстрований!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Реєстрація успішна! Тепер ви можете увійти.')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вхід успішний!')
            return redirect('home')
        else:
            messages.error(request, 'Невірне ім\'я користувача або пароль!')
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
            messages.error(request, 'Паролі не співпадають!')
            return redirect('home')

        if User.objects.filter(username=username).exclude(id=user.id).exists():
            messages.error(request, 'Ім\'я користувача вже зайняте!')
            return redirect('home')
        if User.objects.filter(email=email).exclude(id=user.id).exists():
            messages.error(request, 'Email вже зареєстрований!')
            return redirect('home')

        user.username = username
        user.email = email
        if password:
            user.set_password(password)
        user.save()

        messages.success(request, 'Дані профілю успішно оновлені!')
        return redirect('home')

    return render(request, 'home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    messages.success(request, 'Ви успішно вийшли з акаунта.')
    return redirect('login')
