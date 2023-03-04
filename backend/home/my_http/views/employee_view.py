# from django.http import JsonResponse
# from rest_framework import generics
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# import json
# from ..models.CustomerModel import Customer
# from ..serializers.EmpSerializers import CustomerSerializer
# from rest_framework.viewsets import ViewSet

# class CustomerView(ViewSet):
#     def showCustomer(self, request):
#         customers = Customer.objects.all()
#         serializer_class = CustomerSerializer(customers, many=True)
#         # results = {
#         #     "status": 0,
#         #     "message": "succes",
#         #     "data": serializer_class.data
#         # }
#         return Response(serializer_class.data)

#     def insertCustomer(self, request):
#         customer_data = json.load(request)
#         serializer_class = CustomerSerializer(data=customer_data)
#         results = {
#             "status": 0,
#             "message": "succes",
#             "data": None
#         }
#         if serializer_class.is_valid():
#             serializer_class.save()

#             return JsonResponse(results, safe=False)
#         results['message'] = "failed"
#         return JsonResponse(results, safe=False)

#     def updateCustomer(self, request):
#         customer_data = json.load(request)
#         customer = Customer.objects.get(id=customer_data['id'])
#         serializer_class = CustomerSerializer(customer,data=customer_data)
#         results = {
#             "status": 0,
#             "message": "succes",
#             "data": None
#         }
#         if serializer_class.is_valid():
#             serializer_class.save()
#             results['data'] = serializer_class.data
#             return JsonResponse(results, safe=False)
#         results['message'] = "failed"
#         return JsonResponse(results, safe=False)

#     def deleteCustomer(self, request):
#         customer_data = json.load(request)
#         customer = Customer.objects.get(id=customer_data['id'])
#         customer.delete()
#         results = {
#             "status": 0,
#             "message": "succes",
#             "data": None
#         }
#         return JsonResponse(results, safe=False)
