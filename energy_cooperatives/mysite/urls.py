# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('baza', views.baza_view, name='baza'),
    path('cooperatives', views.cooperatives_view, name='cooperatives'),
    path('courses', views.courses_view, name='courses'),
    path('mentors', views.mentors_view, name='mentors'),
    path('news', views.news_view, name='news'),
    path('animations', views.animations_view, name='animations'),
    path('login', views.login_form, name='login'),
    path('signup', views.signup_form, name='signup'),
]
