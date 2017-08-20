from django.contrib import admin

from .models import *

class BeanModelAdmin(admin.ModelAdmin):
		list_display = ['name', 'price']
		search_fields = ['name']
		list_editable = ['price']
		class Meta:
			model = Bean


class RoastModelAdmin(admin.ModelAdmin):
		list_display = ['name', 'price']
		search_fields = ['name']
		list_editable = ['price']
		class Meta:
			model = Roast


class PowderModelAdmin(admin.ModelAdmin):
		list_display = ['name', 'price']
		search_fields = ['name']
		list_editable = ['price']
		class Meta:
			model = Powder


class SyrupModelAdmin(admin.ModelAdmin):
		list_display = ['name', 'price']
		search_fields = ['name']
		list_editable = ['price']
		class Meta:
			model = Syrup

class CoffeeModelAdmin(admin.ModelAdmin):
		list_display = ['name', 'price']
		search_fields = ['name']
		list_editable = ['price']
		class Meta:
			model = Coffee



admin.site.register(Bean, BeanModelAdmin)
admin.site.register(Roast, RoastModelAdmin)
admin.site.register(Powder, PowderModelAdmin)
admin.site.register(Syrup, SyrupModelAdmin)
admin.site.register(Coffee, CoffeeModelAdmin)

