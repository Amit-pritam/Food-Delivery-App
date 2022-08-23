from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def sign_up_user(request):
	username = request.POST["username"]
	password = request.POST["password"]
	phone = request.POST["phone"]

	if User.objects.filter(username = username).exists():
		messages.add_message(request,messages.ERROR,"username already exist")
		return redirect("homepage")
	User.objects.create_user(username = username,password = password)
	last_obj = len(User.objects.all()) - 1
	CustomerModel(userid = User.objects.all()[int(last_obj)].id,phone = phone).save()
	messages.add_message(request, messages.SUCCESS,'USER CREATED SUCCESSFULLY!!!!')
	return redirect("homepage")


def homepage(request):
	return render(request,"frontend/index.html")

def user_login_view(request):
	return render(request,"frontend/userlogin.html")

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']


	user = authenticate(username= username, password= password)
	if user is not None:
		login(request,  user)
		return redirect('customerview')

	if user is None:
		messages.add_message(request, messages.ERROR, "Invalid Credentials")
		return redirect('userlogin')		

def customer_view(request):
	if not request.user.is_authenticated:
		return redirect('userlogin')
	context = {"foods":FoodModel.objects.all()}	
	return render(request,"frontend/customer_home.html",context)
    

def admin_view(request):
	return render(request,"frontend/admin.html")


def adminauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']


	user = authenticate(username= username, password= password)
	if user is not None:
		login(request,  user)
		return redirect('adminview')

	if user is None:
		messages.add_message(request, messages.ERROR, "Invalid Credentials")
		return redirect('adminlogin')

def admin_home_view(request):
	if not request.user.is_authenticated:
		return redirect('adminlogin')
	context = {"items":FoodModel.objects.all()}	
	return render(request,"frontend/admin_home.html",context)

def addfood(request):
	foodname = request.POST['foodname']
	foodprice = request.POST['foodprice']
	FoodModel(foodname= foodname, foodprice= foodprice).save()
	return redirect('adminview')


def deletefood(request , idpk):
	FoodModel.objects.filter(id = idpk).delete()  
	return redirect('adminview')

def adminlogout(request):
	logout(request)
	return redirect('adminlogin')

def userlogout(request):
	logout(request)
	return redirect('userlogin')

def admin_order(request):
	context = {"orders":OrderModel.objects.all()}
	return render(request,"frontend/orderstatus.html",context)


def placed_order(request):
	if not request.user.is_authenticated:
		return redirect('userlogin')

	username = request.user.username
	phone = CustomerModel.objects.filter(userid = request.user.id).first().phone
	address = request.POST['address']
	orderitem = ""
	for i in FoodModel.objects.all():
		foodid = i.id
		name = i.foodname
		price = i.foodprice

		quantity = request.POST.get(str(foodid)," ")
		if str(quantity)!=0 and str(quantity)!=" ":
			orderitem = orderitem + name+" " + "price: " + str(int(quantity)*int(price)) +" "+ "quantity: "+ quantity+ " "
	print(orderitem)

	OrderModel(username= username, phone= phone, address= address, orderitem= orderitem).save()
	messages.add_message(request, messages.ERROR, 'Your Order Successfully placed')
	return redirect('customerview')

def user_cart(request):
	context = {"orders":OrderModel.objects.all()}
	return render(request,"frontend/user_order.html",context)

def order_accept(request, idpk):
	order = OrderModel.objects.filter(id = idpk)[0]
	order.status="Acccepted"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

def order_reject(request, idpk):
	order = OrderModel.objects.filter(id = idpk)[0]
	order.status="Rejected"
	order.save()
	return redirect(request.META['HTTP_REFERER'])
	   
