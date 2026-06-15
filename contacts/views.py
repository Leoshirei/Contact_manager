from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .models import  Contact

# Create your views here.
def register_site(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_site(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_panel')
        else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_site(request):
    logout(request)
    return redirect('login')

@login_required
def main_panel(request):
    contacts = Contact.objects.filter(owner = request.user)
    return render(request, 'main_panel.html', {'contacts': contacts})

@login_required
def create_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact.objects.create(owner = request.user, name = name, surname = surname, email = email, phone = phone)
        contact.save()
        return redirect('main_panel')
    return render(request, 'create_contact.html')
