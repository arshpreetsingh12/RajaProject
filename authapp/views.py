from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.db.models import Q


"""
	First step of registration.
									"""
class Registartions(TemplateView):
	template_name = 'register.html'
	def get(self, request, *args, **kwargs):
		
		return render(request,self.template_name,locals())

	def post(self,request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm-password')
		try:
			user = User.objects.get(email = email)
			messages.info(request,"User already exist.")
			return HttpResponseRedirect(reverse('register'))
		except User.DoesNotExist:
			if email and password:
				if password == confirm_password:
					user = User.objects.create(username = email, email = email)
					user.set_password(password)
					user.save()
					request.session['user_id'] = user.id
					return HttpResponseRedirect(reverse('student_info'))
				else:
					messages.error(request,"Password does not match.")
					return HttpResponseRedirect(reverse('register'))
			else:
				messages.error(request,"Please enter email and password.")
				return HttpResponseRedirect(reverse('register'))
			

"""
	Second step of registration. Add student information.
															"""
class StudentInfo(TemplateView):
	template_name = 'student.html'
	def get(self, request, *args, **kwargs):
		countries = Countries.objects.all()
		states = States.objects.all()
		grades = Grades.objects.all()

		return render(request,self.template_name,locals())


	def post(self,request):
		student_name = request.POST.get('student_name')
		country_id = request.POST.get('country')
		state_id = request.POST.get('state')
		grade_id = request.POST.get('grade')
		user_id = request.session.get('user_id')
		if user_id:
			try:
				user = StudentDetail.objects.get(user_id = user_id)
				messages.info(request,"Please Register with another email.")
				return HttpResponseRedirect(reverse('register'))
			except  StudentDetail.DoesNotExist:
				country = Countries.objects.filter(id = country_id).last()
				state = States.objects.filter(id = state_id).last()
				grade = Grades.objects.filter(id = grade_id).last()

				user = StudentDetail.objects.create(
						user_id = user_id,
						student_name = student_name, 
						country = country, 
						state = state, 
						grade = grade
					)

				return HttpResponseRedirect(reverse('payment'))
		else:
			messages.info(request,"Please complete first register step.")
			return HttpResponseRedirect(reverse('register'))


"""
	Last step of registration. Add Billing contact infomation. 
															  """
class Payment(TemplateView):
	template_name = 'payment.html'
	def get(self, request, *args, **kwargs):
		states = States.objects.all()
		return render(request,self.template_name,locals())

	def post(self,request):
		full_name = request.POST.get('full-name')
		address = request.POST.get('address')
		apt_suite = request.POST.get('apt-suite')
		city = request.POST.get('city')
		country_id = request.POST.get('country')
		state_id = request.POST.get('state')
		zip_code = request.POST.get('zip_code')
		user_id = request.session.get('user_id')
		if user_id:	
			student_obj = StudentDetail.objects.filter(user_id = user_id).last()
			if student_obj:
				try:
					user = BillingContact.objects.get(info = student_obj)
					messages.info(request,"Please Register with another email.")
					return HttpResponseRedirect(reverse('register'))

				except  BillingContact.DoesNotExist:
					state = States.objects.filter(id = state_id).last()
					user = BillingContact.objects.create(
							info = student_obj,
							full_name = full_name, 
							address_line1 = address, 
							country = country_id,
							state = state, 
							city = city,
							zip_code = zip_code,
							apt = apt_suite
						)
					if 'user_id' in request.session:
						del request.session["user_id"]
					return HttpResponse("Registartion Successfully")
			else:
				messages.info(request,"Please complete second Student Details step.")
				return HttpResponseRedirect(reverse('student_info'))
		else:
			messages.info(request,"Please complete first register step.")
			return HttpResponseRedirect(reverse('register'))
		


""" 
	This view for user login  
								"""
class LoginView(View):
	template_name = "login.html"

	def get(self,request):
		return render(request,self.template_name,locals())

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			if email != "" and password != "": 
				user= User.objects.get(Q(email = email)|Q(username = email))
				if user.is_active == True:
					userauth = authenticate(username=user.username, password=password)
					if userauth:
						login(request, user,backend='django.contrib.auth.backends.ModelBackend')	
						return HttpResponse("Successfully login")
							
					else:
						messages.error(request,'Invalid credentials.')
						return HttpResponseRedirect(reverse('web_login'))
			else:
				messages.error(request,'Incorrect email and password.')
				return HttpResponseRedirect(reverse('web_login'))

		except Exception as e:
			print(str(e))
			messages.info(request,'No such account exist.')
			return HttpResponseRedirect(reverse('web_login'))

class StudentDashboard(TemplateView):
	template_name = 'student_dashboard.html'
	def get(self, request):
		return render(request, self.template_name, locals())
