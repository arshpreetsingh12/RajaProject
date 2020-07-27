from .views import *
from django.urls import path

urlpatterns = [
	path('register', Registartions.as_view(), name="register"),
	path('student-info', StudentInfo.as_view(), name="student_info"),
	path('payment', Payment.as_view(), name="payment"),
	path('login', LoginView.as_view(), name="web_login"),

	path('student-dashboard', StudentDashboard.as_view(), name="student-dashboard"),



]