from django.contrib import admin

from .models import Bean

class BeanModelAdmin(admin.ModelAdmin):
		list_display = ['name', 'price']
		search_fields = ['name']
		list_editable = ['price']
		class Meta:
			model = Bean

admin.site.register(Bean, BeanModelAdmin)