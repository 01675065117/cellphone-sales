from rest_framework import generics

from ..models.EmpModel import Employee
from ...serializers import EmployeeSerializer

class EmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer