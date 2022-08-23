from django.db import models


class CustomerModel(models.Model):
	userid = models.CharField(max_length=255)
	phone = models.CharField(max_length=10)

class FoodModel(models.Model):
	foodname = models.CharField(max_length=255)
	foodprice = models.CharField(max_length=4)

	class Meta:
		managed = False

class OrderModel(models.Model):
	username =  models.CharField(max_length=255)
	phone = models.CharField(max_length=10)
	orderitem = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	status = models.CharField(max_length=255)	
	



