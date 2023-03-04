# This file is used to translate models into a JSON respond
from rest_framework import serializers
from ..models.customer_model import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['cus_code', 'first_name', 'last_name',
                   'email_address', 'phone_number', 'password',
                     'gender', 'address']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         make_password(password)
    #     instance.save()
    #     return instance