
from django.conf.urls import url
from . import views



urlpatterns = [


	url(r'^signup/$', views.usersignup, name="signup"),
	url(r'^login/$', views.userlogin, name="login"),
	url(r'^logout/$', views.userlogout, name="logout"),
	url(r'^home/$', views.home, name="home"),
	url(r'^bean_list/$', views.bean_list, name="bean_list"),
	
	

]