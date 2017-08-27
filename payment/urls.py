from django.conf.urls import url
from . import views




urlpatterns = [


	url(r'^pay/(?P<order_id>[0-9]+)$', views.pay, name="pay"),
	url(r'^successful_payment/$', views.successful_payment, name="successful_payment"),
	url(r'^unsuccessful_payment/$', views.unsuccessful_payment, name="unsuccessful_payment"),


	
	]
