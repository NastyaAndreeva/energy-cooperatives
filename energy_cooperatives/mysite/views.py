# views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SignupForm, CustomLoginForm

@csrf_exempt
def signup_form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        for field in form:
            print(field.value)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        if not form.is_valid():
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {'form': form})

@csrf_exempt
def login_form(request):
    if request.method == 'POST':
        password = request.POST.get("password1")
        user_name = request.POST.get("username")
        user = authenticate(request=request, user_name=user_name, password=password)
        login(request, user)
        return redirect('/')
    context = {}
    return render(request, 'login_form.html', context=context)
