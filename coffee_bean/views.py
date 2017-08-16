from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from .forms import UserSignUp, UserLogin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.db.models import Q
# Create your views here.



def usersignup(request):
	context = {}
	form = UserSignUp()
	context ['form'] = form 
	if request.method == "POST":
		form = UserSignUp(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = user.username
			password = user.password
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)

			return redirect("coffee_bean:home")
		messages.error(request, form.errors)
		return redirect("coffee_bean:signup")
	return render(request, 'signup.html', context)

def userlogout(request):
	logout(request)
	return redirect("coffee_bean:login")


def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == "POST":
		form = UserLogin(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("coffee_bean:home")

			messages.warning(request, "Wrong username/password combination. Please try again.")
			return redirect("coffee_bean:login")
		messages.error(request, form.errors)
		return redirect("coffee_bean:login")
	return render(request, 'login.html', context)



def home(request):
	return HttpResponse("<h1> Welcome to the Coffee shop</h1>")

#def home_admin(request):


def bean(request):
	context = {}
	form = BeanForm()

def bean_list(request):

	obj_list = Bean.objects.all()
	

	query = request.GET.get("q")
	if query:
		obj_list = obj_list.filter(
			Q(name__icontains=query)
			).distinct()

	
	context = {
		"bean_list": objs,
		
	}
	return render(request, 'bean_list.html', context)



def bean_creat(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = BeanForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request, "Bean created!")
		return redirect("bean:bean_list")
	context = {
		"form":form,
	}
	return render(request, 'post_create.html', context)



def syrup(request):
	context = {}
	form = SyrupsForm()


def powder(request):
	context = {}
	form = PowderForm()


def roast(request):
	context = {}
	form = RoastForm()








