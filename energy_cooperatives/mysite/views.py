# views.py
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm
# example
def fruit_list(request):
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    return render(request, 'index.html', {'fruits': fruits})

def login_form(request):
    return render(request, 'login_form.html')

# def signup_form(request):
#     return render(request, 'signup_form.html')

def signup_form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # Redirect to the homepage after signup
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {'form': form})
