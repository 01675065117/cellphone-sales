# This file is used to translate models into a JSON respond
from rest_framework import serializers

from ..models.CustomerModel import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'