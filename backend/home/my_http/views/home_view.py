from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# Create your views here.
class Test(ViewSet):
    def index(self, request):
        dict_test = {
            "name": "test",
            "index": 0
        }
        return Response(dict_test)

    # def getAll(self, request):
    #     dict_test = Data.objects.all()
    #     serializer = DataSerializer(dict_test)
    #     # serializer is json
    #     return Response(serializer)

    def insert(self, request):
        try:
            getData = request.data
            hasValidate = True

            result = {
                "status": 0,
                "message": "succes",
                "data": getData['name']
            }

            # if seriliazer.is_valid():
            #     pass

            if not hasValidate:
                result['message'] = "faild"

            # serializer is json
            return Response(result)
        except:
            result = {
                "status": 0,
                "message": "lỗi hệ thống",
                "data": getData['name']
            }
            return Response(result)
