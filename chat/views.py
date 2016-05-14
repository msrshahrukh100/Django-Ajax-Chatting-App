from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Onlineusers
# Create your views here.
def home(request):
	if request.method == 'POST' and request.POST.get('signup'):
		signupform = Signupform(request.POST or None)
		loginform = Loginform()
		if signupform.is_valid():
			em = signupform.cleaned_data['email']
			na = signupform.cleaned_data['username']
			pw = signupform.cleaned_data['password']
			if User.objects.all().filter(email=em).exists():
				messages.error(request, 'This email is already taken!')
			elif User.objects.all().filter(username=na).exists():
				messages.error(request, 'This username is already taken!')
			else:
				messages.success(request, 'You have successfully signed up.Login to continue')
				User.objects.create_user(na,em,pw)

		context = {'form1': signupform,'form2':loginform}
	elif  request.method == 'POST':
		signupform = Signupform()
		loginform = Loginform(request.POST or None)
		if loginform.is_valid():
			na = loginform.cleaned_data['username']
			pw = loginform.cleaned_data['password']
			user = authenticate(username=na, password=pw)
			if user :
				login(request, user)
				o = Onlineusers(olu = user)
				o.save()
				return redirect('dashboard')
			else :
				messages.error(request, 'Invalid login credentials!')
		context = {'form1': signupform,'form2':loginform}
	else:
		context = {'form1':Signupform(),
		'form2':Loginform()}
	return render(request,"home.html",context)



@login_required(login_url='home')
def dashboard(request):
	context = {'online':Onlineusers.objects.all()}
	return render(request,"dashboard.html",context)

@login_required(login_url='home')
def chatting(request,id):
	pass


	




def logout_view(request):
	user = request.user
	logout(request)
	x = Onlineusers.objects.get(olu = user)
	x.delete()
	return redirect('home')
# Redirect to a success page.
