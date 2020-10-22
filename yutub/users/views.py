from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            context['error'] = "El usuario no puede ser identificado"
    return render(request, "templatesBase/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')