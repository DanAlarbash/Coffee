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
		fields = ['name', 'price']

class SyrupsForm(forms.ModelForm):
	class Meta:
		model = Syrups
		fields = ['name', 'price']

class PowderForm(forms.ModelForm):
	class Meta:
		model = Powder
		fields = ['name', 'price']

class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['name', 'price']
