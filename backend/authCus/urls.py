from django.urls import path
from .my_http.views.register_view import RegisterView
from .my_http.views.login_view import LoginView
from .my_http.views.customer_view import CustomerView
from .my_http.views.logout_view import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view({'post': 'registerCustomer'})),
    path('login/', LoginView.as_view({'post': 'customerLogin'})),
    path('customerview/', CustomerView.as_view({'get': 'authenticatedCustomer'})),
    path('logout/', LogoutView.as_view({'post': 'logout'})),
]