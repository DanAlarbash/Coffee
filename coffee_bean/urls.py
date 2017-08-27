
from django.conf.urls import url
from . import views



urlpatterns = [


	url(r'^signup/$', views.usersignup, name="signup"),
	url(r'^login/$', views.userlogin, name="login"),
	url(r'^logout/$', views.userlogout, name="logout"),

	url(r'^home/$', views.home, name="home"),
	url(r'^admin_home/$', views.admin_home, name="admin_home"),
	url(r'^user_home/$', views.user_home, name="user_home"),

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

	url(r'^powder_list/$', views.powder_list, name="powder_list"),
	url(r'^powder_create/$', views.powder_create, name="powder_create"),
	url(r'^powder_edit/(?P<slug>[-\w]+)/$', views.powder_edit, name="powder_edit"),
	url(r'^powder_detail/(?P<slug>[-\w]+)/$', views.powder_detail, name="powder_detail"),
	url(r'^powder_delete/(?P<slug>[-\w]+)/$', views.powder_delete, name="powder_delete"),

	url(r'^roast_list/$', views.roast_list, name="roast_list"),
	url(r'^roast_create/$', views.roast_create, name="roast_create"),
	url(r'^roast_edit/(?P<slug>[-\w]+)/$', views.roast_edit, name="roast_edit"),
	url(r'^roast_delete/(?P<slug>[-\w]+)/$', views.roast_delete, name="roast_delete"),
	url(r'^roast_detail/(?P<slug>[-\w]+)/$', views.roast_detail, name="roast_detail"),

	url(r'^coffee_list/$', views.coffee_list, name="coffee_list"),
	url(r'^coffee_create/$', views.coffee_create, name="coffee_create"),
	url(r'^coffee_edit/(?P<slug>[-\w]+)/$', views.coffee_edit, name="coffee_edit"),
	url(r'^coffee_delete/(?P<slug>[-\w]+)/$', views.coffee_delete, name="coffee_delete"),
	url(r'^coffee_detail/(?P<slug>[-\w]+)/$', views.coffee_detail, name="coffee_detail"),
	url(r'^my_coffee/$', views.my_coffee, name="my_coffee"),


	# url(r'^address/$', views.address, name="address"),
	# url(r'^address_edit/(?P<slug>[-\w]+)/$', views.address_edit, name="address_edit"),
	# url(r'^address_list/$', views.address_list, name="address_list"),
	# url(r'^address_delete/(?P<slug>[-\w]+)/$', views.address_delete, name="address_delete"),



	url(r'^city_create/$', views.city_create, name="city_create"),
	url(r'^city_list/$', views.city_list, name="city_list"),
	url(r'^city_delete/(?P<slug>[-\w]+)/$', views.city_delete, name="city_delete"),




	url(r'^price_calculation/$', views.price_calculation, name="price_calculation"),

]