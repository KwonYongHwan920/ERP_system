from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], is_active=False)
            auth.login(request, user)
            return render(request, 'signup_waiting.html', {'user':user})
        return redirect('/')
    return render(request, 'signup.html')

@login_required
def welcome_home(request):
	# return HttpResponse("HttpResponse : /home/templates/welcome_home.html.")
	return render(request, 'welcome_home.html')