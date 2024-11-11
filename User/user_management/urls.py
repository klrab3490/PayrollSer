# PayrollSer/User/User/user_management/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    

    # Other URLs can be added here for employee details, payroll, etc.
]
