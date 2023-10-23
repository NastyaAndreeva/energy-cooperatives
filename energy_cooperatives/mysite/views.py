from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def baza_view(request):
    return render(request, 'baza.html')

def cooperatives_view(request):
    return render(request, 'cooperatives.html')

def courses_view(request):
    return render(request, 'courses.html')

def mentors_view(request):
    return render(request, 'mentors.html')

def news_view(request):
    return render(request, 'news.html')

def animations_view(request):
    return render(request, 'animations.html')


