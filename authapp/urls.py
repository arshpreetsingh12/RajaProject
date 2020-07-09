from .views import *
from django.urls import path

urlpatterns = [
	path('register', Registartions.as_view(), name="register"),
	path('student-info', StudentInfo.as_view(), name="student_info"),
	path('payment', Payment.as_view(), name="payment"),




]