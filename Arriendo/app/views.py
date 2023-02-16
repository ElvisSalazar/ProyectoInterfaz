from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'SignUp.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                # return HttpResponse('User creation successfully')
                return redirect('home')
            except:
                return render(request, 'signUp.html',{
                    'form': UserCreationForm,
                    'error': 'Username Already exist'
                })

        return render(request, 'signUp.html',{
                    'form': UserCreationForm,
                    'error': 'Password do not match'
                })

def home(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password =password  )

        if user is None:
            return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'invalid username or password'
        })

        login(request, user)
        return redirect('homepage')

        
        

def signout(request):
    logout(request)
    return redirect('home')

def homepage(request):
    return render(request, 'homepage.html')

def add(request):
    return render(request, 'add.html')