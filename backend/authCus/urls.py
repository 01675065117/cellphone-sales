from django.urls import path
from .my_http.views.register_view import RegisterView
from .my_http.views.login_view import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view({'post': 'insertCustomer'})),
    path('login/', LoginView.as_view({'post': 'customerLogin'})),
]