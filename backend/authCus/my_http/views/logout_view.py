from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class LogoutView(ViewSet):
    def logout(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'status': 0,
            'message': 'success'
        }
        return response
