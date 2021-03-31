from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from store.forms import UserForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/index.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def faq(request):
    context = {}
    return render(request, 'store/faq.html', context)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'store/register.html',
                  context={'user_form': user_form,  'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            messages.info(request, 'invalid username OR password')

    context = {}
    return render(request, 'store/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse('index'))
    else:
        edit_form = EditProfileForm(instance=request.user)
        context = {'edit_form': edit_form}
        return render(request, 'store/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect(reverse('edit profile'))

    else:
        password_form = PasswordChangeForm(user=request.user)
        context = {'password_form': password_form}
        return render(request, 'store/change_password.html', context)

