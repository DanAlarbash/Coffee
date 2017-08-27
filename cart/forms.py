from django import forms
from coffee_bean.models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = '__all__'
		exclude = ['user', 'slug']

class AddressSelectForm(forms.Form):
	address = forms.ModelChoiceField(
		queryset = Address.objects.all(),
		empty_label=None
		)