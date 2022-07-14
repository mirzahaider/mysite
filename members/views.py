from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            return redirect('members:login')

    else:
        return render(request, 'members/login.html')


def logout_user(request):
    logout(request)
    return redirect('polls:index')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('polls:index')
        messages.error(request, "Error in registration")
    form = CustomUserCreationForm()
    return render(request, 'members/register.html', {'form': form})

