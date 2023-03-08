from django.http import JsonResponse
from rest_framework.response import Response
import json
from ..models.customer_model import Customer
from ..serializers.customer_serializer import CustomerSerializer
from rest_framework.viewsets import ViewSet
# from django.contrib.auth.hashers import make_password

class RegisterView(ViewSet):
    def registerCustomer(self, request):
        customer_data = json.load(request)
        customer_data['email_address'] = customer_data['email']
        customer_data['phone_number'] = customer_data['phonenumber']
        customer_data['first_name'] = customer_data['firstname']
        customer_data['last_name'] = customer_data['lastname']
        serializer_class = CustomerSerializer(data=customer_data)
        results = {
            "status": 0,
            "message": "success",
            "data": None
        }
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(results, safe=False)
        
        results['message'] = "failed"
        return JsonResponse(results, safe=False)