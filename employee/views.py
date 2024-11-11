from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def employee_dashboard(request):
    return render(request, 'employee/home.html')
def home(request):
    return render(request, 'employee/home.html')

def list_employees(request):
    # Logic to list employees
    return render(request, 'employee/list.html')

def employee_detail(request, id):
    # Logic to show details of a specific employee
    return render(request, 'employee/detail.html', {'id': id})

