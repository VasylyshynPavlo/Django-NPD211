from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def user_detail(request, id):
    user = users[int(id) - 1]

    return HttpResponse(f"<h1>{user['name']}</h1>" + f"<p>{user['email']}</p>")
