from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages , auth

# Create your views here.


def logoutuser(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        if email == '' and password == '':
            messages.error(request, "Please provide an email and password")
        elif password == '':
            messages.error(request, "Please provide password")
        elif email == '':
            messages.error(request, "Please provide an email")
        else:
            try:
                user = Account.objects.get(email=email)
            except:
                messages.error(request, "user does not exist")
                
                
        user = authenticate(request,email=email, password=password)
        
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "email or password does not match")
    return render(request,'login.html')

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render(request,"registeration.html", context={"form":form})