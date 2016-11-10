from rest_framework import serializers
from models import Employees


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('name', 'email', 'departament')