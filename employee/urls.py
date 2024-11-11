from django.urls import path,include
from . import views  # Import views from the current app

urlpatterns = [

    
    path('', views.home, name='employee-home'),
    path('list/', views.list_employees, name='list-employees'),  
    path('<int:id>/', views.employee_detail, name='employee-detail'),
]
