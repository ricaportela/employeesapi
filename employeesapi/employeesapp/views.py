from models import Employees
from serializer import EmployeesSerializer
from rest_framework import viewsets


class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API Endpoint allows views and edit
    """
    employees = Employees.objects.all()
    serializer_class = EmployeesSerializer


