from django.db import models
from django.contrib.auth.models import User


class Countries(models.Model):
	""" This table for store Country. """
	country_name = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.country_name

class States(models.Model):
	""" This table for store sates. """
	country = models.ForeignKey(Countries, on_delete=models.CASCADE,null = True,blank = True)
	state_name = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.state_name

class Cities(models.Model):
	""" This table for store sates. """
	state = models.ForeignKey(States, on_delete=models.CASCADE,null = True,blank = True)
	city_name = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.city_name

class Grades(models.Model):
	""" This table for store grades. """
	grade = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.grade

class Payments(models.Model):
	""" This table for set payments. """
	payment_per_student = models.FloatField(default = 0)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class StudentDetail(models.Model):
	""" This table for store Student details. """
	user = models.ForeignKey(User, on_delete=models.CASCADE,null = True,blank = True)
	student_name = models.CharField(max_length=	200)
	country = models.ForeignKey(Countries, null = True,blank = True, on_delete=models.CASCADE)
	state = models.ForeignKey(States, null = True,blank = True, on_delete=models.CASCADE)
	grade = models.ForeignKey(Grades, null = True,blank = True, on_delete=models.CASCADE)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.student_name



class BillingContact(models.Model):
	""" This table for store Billing contact details. """
	info = models.ForeignKey(User, on_delete=models.CASCADE,null = True,blank = True)
	student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE,null = True,blank = True)
	full_name = models.CharField(max_length=200)
	address_line1 = models.CharField(max_length=200)
	country = models.ForeignKey(Countries, null = True,blank = True, on_delete=models.CASCADE)
	state = models.ForeignKey(States, null = True, blank = True, on_delete=models.CASCADE)
	city = models.ForeignKey(Cities, null = True,blank = True, on_delete=models.CASCADE)
	apt = models.CharField(max_length=200, null = True)
	amount = models.FloatField(default = 0.0)
	zip_code = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.full_name

