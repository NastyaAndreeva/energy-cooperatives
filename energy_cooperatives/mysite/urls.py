# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fruit_list, name='fruits'),
]
