from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('usernameOrEmail')
        password = request.POST.get('password')
        
        api_url = "http://localhost:5199/api/User/login"
        response = requests.post(api_url, data={
            'usernameOrEmail': username_or_email,
            'password': password,
        })
        
        if response.status_code == 200:
            token = response.json().get('data')
            
            if token:
                request.session['auth_token'] = token
                
                return redirect('success_url')
            else:
                return render(request, 'login.html', {'error': 'Login failed, no token returned.'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')