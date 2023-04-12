from django.urls import path
from .views import BaseRegisterView, BaseLoginView, BaseLogoutView, register_confirm_view

urlpatterns = [
    path('login/', BaseLoginView.as_view(), name='login'),
    path('logout/', BaseLogoutView.as_view(), name='logout'),
    path('signup/', BaseRegisterView.as_view(), name='signup'),
    path('signup_confirm/', register_confirm_view, name='signup_confirm'),
]
