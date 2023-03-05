from django.http import JsonResponse
from rest_framework.response import Response
import json
from ..models.customer_model import Customer
from ..serializers.customer_serializer import CustomerSerializer
from rest_framework.viewsets import ViewSet
import jwt
from rest_framework.exceptions import AuthenticationFailed
# from django.contrib.auth.hashers import make_password

class CustomerView(ViewSet):
    def authenticatedCustomer(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        customer = Customer.objects.filter(id=payload['id']).first()
        serializer_class = CustomerSerializer(customer)
        return Response(serializer_class.data)