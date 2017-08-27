from django import forms
from django.contrib.auth.models import User
from .models import *


class UserSignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

		widgets = {
		'password' : forms.PasswordInput()
		}



class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput()) 



class BeanForm(forms.ModelForm):
	class Meta:
		model = Bean
		fields = '__all__'

class SyrupForm(forms.ModelForm):
	class Meta:
		model = Syrup
		fields = ['name', 'price']

class PowderForm(forms.ModelForm):
	class Meta:
		model = Powder
		fields = ['name', 'price']

class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['name', 'price']


class CoffeeForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields = ['name','bean', 'roast', 'powder', 'syrup', 'water', 'foam', 'milk', 'shots', 'extra_instructions' ]
		#coffee = forms.MultipleChoiceField(Coffee.objects.all(), widget=forms.CheckboxSelectMultiple)

class CityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = ['name']

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = '__all__'
		exclude = ['user', 'slug']



    
