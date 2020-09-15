from django.shortcuts import render, redirect#, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
#from django.conf import settings
from .models import *
#from .forms import UserEditForm
import bcrypt

def base(request):
    return render (request, 'login.html')

def user_login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid Email/Password")
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['name'] = user.first_name
        return redirect('bookbarn/homepage')
    return redirect('/')

def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        password = request.POST['password']
        hashedpw = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        print(hashedpw)
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashedpw)
        request.session['user_id'] = new_user.id
        request.session['name'] = new_user.first_name
        #request.session['name'] = new_user.first_name
        return redirect('bookbarn/homepage')

def success(request):
    if 'name' not in request.session:
        return redirect('/')
    return render(request, 'success.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    request.session.clear()
    return redirect('/')