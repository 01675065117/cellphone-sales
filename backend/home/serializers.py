# This file is used to translate models into a JSON respond
from rest_framework import serializers

from .my_http.models.EmpModel import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'code', 'full_name', 'phone', 'create_at')