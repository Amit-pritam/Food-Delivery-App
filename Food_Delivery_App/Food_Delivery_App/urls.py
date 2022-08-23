from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
	path('',homepage,name="homepage"),
 	path('signup/',sign_up_user),
 	path('login/',user_login_view,name="userlogin"),
 	path('userauthenticate/',userauthenticate),
 	path('customerview/',customer_view,name="customerview"),
 	path('admin/',admin_view,name="adminlogin"),
 	path('adminauthenticate/',adminauthenticate),
 	path('adminhome/',admin_home_view,name="adminview"),
 	path('addfood/',addfood,name="addfood"),
 	path('delete/<int:idpk>/',deletefood,name="deletefoood"),
 	path('logout/',adminlogout),
 	path('logout/',userlogout),
 	path('checkorder/',admin_order),
 	path('placeorder/',placed_order),
 	path('userorder/',user_cart),
 	path('accept/<int:idpk>/',order_accept),
 	path('reject/<int:idpk>/',order_reject)
]
