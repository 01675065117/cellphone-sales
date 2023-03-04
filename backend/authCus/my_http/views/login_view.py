from django.http import JsonResponse
from rest_framework.response import Response
import json
from ..models.customer_model import Customer
from ..serializers.customer_serializer import CustomerSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password, check_password

class LoginView(ViewSet):
    def customerLogin(self, request):
        customer_data = json.load(request)
        email = customer_data['email_address']
        password = customer_data['password']

        user = Customer.objects.filter(email_address=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not check_password(password, user.password):
            raise AuthenticationFailed('Incorrect Password')
        
        results = {
            'status':0,
            'message':'Success'
        }
        return JsonResponse(results, safe=False)