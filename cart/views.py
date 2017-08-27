from django.shortcuts import render, redirect
from .models import Cart, CartItem, Order
from coffee_bean.models import Coffee, Address
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib import messages
from .forms import *



def mycart(request):
	cart, created = Cart.objects.get_or_create(user=request.user)

	item_id = request.GET.get("item")
	qty = request.GET.get("qty", 1)

	if item_id:
		coffee = Coffee.objects.get(id=item_id)
		cart_item, created = CartItem.objects.get_or_create(cart=cart, items=coffee)
		
		if int(qty)<1:
			cart_item.delete()
		else:
			cart_item.quantitiy = int(qty)
			cart_item.save()

	return render(request, 'cart.html', {'cart': cart})

############################################################################################

def create_address(request):
	form = AddressForm()
	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			address = form.save(commit=False)
			address.user = request.user
			address.save()
			form.save()
			return redirect("cart:select_address")

	context = {
	"form": form
	}
	return render(request, 'create_address.html', context)

def select_address(request):
	if Address.objects.filter(user=request.user).count()<1:
		return redirect("cart:create_address")
	form = AddressSelectForm()
	form.fields['address'].queryset = Address.objects.filter(user=request.user)
	if request.method == 'POST':
		form = AddressSelectForm(request.POST)
		if form.is_valid():
			address = form.cleaned_data['address']
			order = Order.objects.get(user=request.user)
			order.address=address
			order.save()
			return redirect("cart:checkout")
	context = {
	'form':form

	}
	return render(request, 'select_address.html', context)


def address_list(request):
	username = request.user
	add_list = Address.objects.all().filter(user=username)
	context = {
		"add_list": add_list,
	}
	return render(request, 'address_list.html', context)


def address_edit(request, slug):
	address_obj = get_object_or_404(Address, slug=slug)
	form = AddressForm(request.POST or None, request.FILES or None, instance=address_obj)
	if form.is_valid():
		form.save()
		messages.success(request, "Address Updated!")
		return redirect("cart:address_list")
	context = {
		"form":form,
		"address_obj":address_obj,
	}
	return render(request, 'address_edit.html', context)


def address_delete(request, slug):
	obj = Address.objects.get(slug=slug).delete()
	messages.warning(request, "Address Deleted.")
	return redirect("cart:address_list")



############################################################################################



def checkout(request):
	cart, created = Cart.objects.get_or_create(user=request.user)
	order, created = Order.objects.get_or_create(cart=cart, user=request.user)

	if order.address == None:
		return redirect("cart:select_address")
	return redirect("payment:pay", order_id=order.id) #payment page






