
from django.conf.urls import url
from . import views



urlpatterns = [


	url(r'^signup/$', views.usersignup, name="signup"),
	url(r'^login/$', views.userlogin, name="login"),
	url(r'^logout/$', views.userlogout, name="logout"),

	url(r'^home/$', views.home, name="home"),
	# url(r'^admim_home/$', views.admim_home, name="admim_home"),
	# url(r'^user_home/$', views.user_home, name="user_home"),

	url(r'^bean_list/$', views.bean_list, name="bean_list"),
	url(r'^bean_create/$', views.bean_create, name="bean_create"),
	url(r'^bean_edit/(?P<slug>[-\w]+)/$', views.bean_edit, name="bean_edit"),
	url(r'^bean_detail/(?P<slug>[-\w]+)/$', views.bean_detail, name="bean_detail"),
	url(r'^bean_delete/(?P<slug>[-\w]+)/$', views.bean_delete, name="bean_delete"),

	url(r'^syrup_list/$', views.syrup_list, name="syrup_list"),
	url(r'^syrup_create/$', views.syrup_create, name="syrup_create"),
	url(r'^syrup_edit/(?P<slug>[-\w]+)/$', views.syrup_edit, name="syrup_edit"),
	url(r'^syrup_detail/(?P<slug>[-\w]+)/$', views.syrup_detail, name="syrup_detail"),
	url(r'^syrup_delete/(?P<slug>[-\w]+)/$', views.syrup_delete, name="syrup_delete"),

	# url(r'^powder_list/$', views.powder_list, name="powder_list"),
	# url(r'^powder_create/$', views.powder_create, name="powder_create"),
	# url(r'^powder_edit/(?P<slug>[-\w]+)/$', views.powder_edit, name="powder_edit"),
	# url(r'^powder_delete/(?P<slug>[-\w]+)/$', views.powder_delete, name="powder_delete"),

	# url(r'^roast_list/$', views.roast_list, name="roast_list"),
	# url(r'^roast_create/$', views.roast_create, name="roast_create"),
	# url(r'^roast_edit/(?P<slug>[-\w]+)/$', views.roast_edit, name="roast_edit"),
	# url(r'^roast_delete/(?P<slug>[-\w]+)/$', views.roast_delete, name="roast_delete"),

	

]