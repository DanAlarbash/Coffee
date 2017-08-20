from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.db.models import Q
from django.core.exceptions import ValidationError
from decimal import Decimal

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

def admin_home(request):
	if not (request.user.is_staff or request.user.is_superuser):
		messages.warning(request, "Admin and Staff Only!")
		return redirect("coffee_bean:home") #change home to userhome later
	return render(request, "admin_home.html")


def user_home(request):
	return render(request, "coffee_list.html")




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



def powder_list(request):

	obj_list = Powder.objects.all()
	query = request.GET.get("q")
	if query:
		obj_list = obj_list.filter(
			Q(name__icontains=query)
			).distinct()

	
	context = {
		"powder_list": obj_list,
		
	}
	return render(request, 'powder_list.html', context)



def powder_create(request):
	form = PowderForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request, "Powder created!")
		return redirect("coffee_bean:powder_list")
	context = {
		"form":form,
	}
	return render(request, 'powder_create.html', context)


def powder_edit(request, slug):
	syrup_object = get_object_or_404(Powder, slug=slug)
	form = PowderForm(request.POST or None, request.FILES or None, instance=powder_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Powder Updated!")
		return redirect("coffee_bean:powder_list")
	context = {
		"form":form,
		"powder_object":powder_object,
	}
	return render(request, 'powder_edit.html', context)

def powder_detail(request, slug):
	obj =  get_object_or_404(Powder, slug=slug)
	username = request.user
	context = {
	"obj" : obj,
	"username" : username
	}
	return render(request, 'powder_detail.html', context)



def powder_delete(request, slug):
	obj = Powder.objects.get(slug=slug).delete()
	messages.warning(request, "Powder Deleted.")
	return redirect("coffee_bean:powder_list")

def roast_list(request):

	obj_list = Roast.objects.all()
	query = request.GET.get("q")
	if query:
		obj_list = obj_list.filter(
			Q(name__icontains=query)
			).distinct()

	
	context = {
		"roast_list": obj_list,
		
	}
	return render(request, 'roast_list.html', context)



def roast_create(request):
	form = RoastForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request, "Roast created!")
		return redirect("coffee_bean:roast_list")
	context = {
		"form":form,
	}
	return render(request, 'roast_create.html', context)


def roast_edit(request, slug):
	roast_object = get_object_or_404(Roast, slug=slug)
	form = RoastForm(request.POST or None, request.FILES or None, instance=roast_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Roast Updated!")
		return redirect("coffee_bean:roast_list")
	context = {
		"form":form,
		"roast_object":roast_object,
	}
	return render(request, 'roast_edit.html', context)

def roast_detail(request, slug):
	obj =  get_object_or_404(Roast, slug=slug)
	username = request.user
	context = {
	"obj" : obj,
	"username" : username
	}
	return render(request, 'roast_detail.html', context)



def roast_delete(request, slug):
	obj = Roast.objects.get(slug=slug).delete()
	messages.warning(request, "Roast Deleted.")
	return redirect("coffee_bean:roast_list")

def coffee_list(request):

	obj_list = Coffee.objects.all()
	query = request.GET.get("q")
	if query:
		obj_list = obj_list.filter(
			Q(name__icontains=query)|
			Q(user__icontains=query)
			).distinct()

	
	context = {
		"coffee_list": obj_list,
		
	}
	return render(request, 'coffee_list.html', context)


def coffee_price (coffeetotal):
	total_price = coffeetotal.bean.price + coffeetotal.roast.price +(coffeetotal.shots*Decimal(0.250))
	if coffeetotal.milk:
		total_price+= Decimal(0.100)
	if coffeetotal.powder.all().count()>0:
		for powder in coffeetotal.powder.all():
			total_price+= powder.price
	if coffeetotal.syrup.all().count()>0:
		for syrup in coffeetotal.syrup.all():
			total_price+= syrup.price
	return total_price



def coffee_create(request):

	context = {}
	form = CoffeeForm()
	if request.method == "POST":
		form = CoffeeForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			form.save_m2m()
			obj.price = coffee_price(obj)
			obj.save()

			messages.success(request, "Coffee created!")
			return redirect("coffee_bean:coffee_list")
	context = {
		'form':form
	}

	return render(request, 'coffee_create.html', context)



def coffee_edit(request, slug):
	coffee_object = get_object_or_404(Coffee, slug=slug)
	form = CoffeeForm(request.POST or None, request.FILES or None, instance=coffee_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Coffee Updated!")
		return redirect("coffee_bean:coffee_list")
	context = {
		"form":form,
		"coffee_object":coffee_object,
	}
	return render(request, 'coffee_edit.html', context)

def coffee_delete(request, slug):
	obj = Coffee.objects.get(slug=slug).delete()
	messages.warning(request, "Coffee Deleted.")
	return redirect("coffee_bean:coffee_list")

def coffee_detail(request, slug):
	obj =  get_object_or_404(Coffee, slug=slug)
	username = request.user
	syrp = obj.syrup.all()
	powd = obj.powder.all()
	context = {
	"obj" : obj,
	"username" : username,
	"syrp": syrp,
	"powd": powd,
	}
	return render(request, 'coffee_detail.html', context)

















