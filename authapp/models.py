from django.db import models
from django.contrib.auth.models import User


class StudentDetail(models.Model):
	""" This table for store Student details. """
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	student_name = models.CharField(max_length=	200)
	country = models.CharField(max_length=50)
	state = models.CharField(max_length=200)
	grade = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.student_name



class BillingContact(models.Model):
	""" This table for store Billing contact details. """
	info = models.OneToOneField(StudentDetail, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=200)
	address_line1 = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.info.student_name


class Countries(models.Model):
	""" This table for store Country. """
	country_name = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.country_name

class States(models.Model):
	""" This table for store sates. """
	state_name = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.state_name

class Grades(models.Model):
	""" This table for store grades. """
	grade = models.CharField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.grade