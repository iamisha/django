from imaplib import _Authenticator
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if password != re_password:
            messages.error(request, "Password doesn't match.")
            return redirect('/register/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('/register/')
        user = User.objects.create(
            username = email,
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        # make password hashing
        user.set_password(password)
        user.save()     

        messages.success(request, "User registered successfully.")
    
    return render(request,'form.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # authenticate user
        user = _Authenticator(username=email,password=password)
        if user is not None:
            # login user
            login(request,user)
            return redirect('/login/')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('/login/')
    return render(request,'form.html')