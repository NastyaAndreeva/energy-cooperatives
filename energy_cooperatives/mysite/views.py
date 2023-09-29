# views.py
from django.shortcuts import render
# example
def fruit_list(request):
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    return render(request, 'index.html', {'fruits': fruits})
