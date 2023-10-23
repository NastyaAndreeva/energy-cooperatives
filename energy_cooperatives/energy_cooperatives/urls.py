"""
URL configuration for energy_cooperatives project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('baza.html', views.baza_view, name='baza'),
    path('cooperatives.html', views.cooperatives_view, name='cooperatives'),
    path('courses.html', views.courses_view, name='courses'),
    path('mentors.html', views.mentors_view, name='mentors'),
    path('news.html', views.news_view, name='news'),
    path('animations.html', views.animations_view, name='animations'),
    path('', include('mysite.urls'))
]
