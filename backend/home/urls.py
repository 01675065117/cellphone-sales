from django.urls import path

from .my_http.views.home_view import Test

urlpatterns = [
    path('home/', Test.as_view({'get': 'index'})),
    path('insert/', Test.as_view({'post': 'insert'})),
]