from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from .forms import *
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
				return redirect("coffee_bean:bean_list")

			messages.warning(request, "Wrong username/password combination. Please try again.")
			return redirect("coffee_bean:login")
		messages.error(request, form.errors)
		return redirect("coffee_bean:login")
	return render(request, 'login.html', context)



def home(request):
	return HttpResponse("<h1> Welcome to the Coffee shop</h1>")

#def home_admin(request):


# def bean(request):
# 	context = {}
# 	form = BeanForm()

def bean_list(request):

	obj_list = Bean.objects.all()
	query = request.GET.get("q")
	if query:
		obj_list = obj_list.filter(
			Q(name__icontains=query)
			).distinct()

	
	context = {
		"bean_list": obj_list,
		
	}
	return render(request, 'bean_list.html', context)



def bean_create(request):
	form = BeanForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request, "Bean created!")
		return redirect("coffee_bean:bean_list")
	context = {
		"form":form,
	}
	return render(request, 'bean_create.html', context)


def bean_edit(request, slug):
	bean_object = get_object_or_404(Bean, slug=slug)
	form = BeanForm(request.POST or None, request.FILES or None, instance=bean_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Bean Updated!")
		return redirect("coffee_bean:bean_list")
	context = {
		"form":form,
		"bean_object":bean_object,
	}
	return render(request, 'bean_edit.html', context)

def bean_detail(request, slug):
	obj =  get_object_or_404(Bean, slug=slug)
	username = request.user
	context = {
	"obj" : obj,
	"username" : username
	}
	return render(request, 'bean_detail.html', context)



def bean_delete(request, slug):
	obj = Bean.objects.get(slug=slug).delete()
	messages.warning(request, "Bean Deleted.")
	return redirect("coffee_bean:bean_list")



def syrup_list(request):

	obj_list = Syrup.objects.all()
	query = request.GET.get("q")
	if query:
		obj_list = obj_list.filter(
			Q(name__icontains=query)
			).distinct()

	
	context = {
		"syrup_list": obj_list,
		
	}
	return render(request, 'syrup_list.html', context)



def syrup_create(request):
	form = SyrupForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request, "Syrup created!")
		return redirect("coffee_bean:syrup_list")
	context = {
		"form":form,
	}
	return render(request, 'syrup_create.html', context)


def syrup_edit(request, slug):
	syrup_object = get_object_or_404(Syrup, slug=slug)
	form = SyrupForm(request.POST or None, request.FILES or None, instance=syrup_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Syrup Updated!")
		return redirect("coffee_bean:syrup_list")
	context = {
		"form":form,
		"syrup_object":syrup_object,
	}
	return render(request, 'syrup_edit.html', context)

def syrup_detail(request, slug):
	obj =  get_object_or_404(Syrup, slug=slug)
	username = request.user
	context = {
	"obj" : obj,
	"username" : username
	}
	return render(request, 'syrup_detail.html', context)



def syrup_delete(request, slug):
	obj = Syrup.objects.get(slug=slug).delete()
	messages.warning(request, "Syrup Deleted.")
	return redirect("coffee_bean:syrup_list")


def powder(request):
	context = {}
	form = PowderForm()


def roast(request):
	context = {}
	form = RoastForm()








