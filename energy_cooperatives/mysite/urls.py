# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fruit_list, name='fruits'),
    path('login', views.login_form, name='login'),
    path('signup', views.signup_form, name='signup'),
]
