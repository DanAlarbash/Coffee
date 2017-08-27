from django.conf.urls import url
from . import views




urlpatterns = [


	url(r'^mycart/$', views.mycart, name="mycart"),

	url(r'^create_address/$', views.create_address, name="create_address"),
	url(r'^select_address/$', views.select_address, name="select_address"),
	url(r'^address_list/$', views.address_list, name="address_list"),
	url(r'^address_edit/(?P<slug>[-\w]+)/$', views.address_edit, name="address_edit"),
	url(r'^address_delete/(?P<slug>[-\w]+)/$', views.address_delete, name="address_delete"),

	url(r'^checkout/$', views.checkout, name="checkout"),




]

