from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import UserRegistrationForm, UserLoginForm, CompanyRegistrationForm, RegisterUserGroupsForm, \
    RegisterUserRolesGroupsForm, RegisterRolesDict
from .models import Users

@login_required(redirect_field_name='')
def register_group(request):
    if request.method == 'POST':
        form = RegisterUserGroupsForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('/')  # Перенаправление на страницу входа
    else:
        form = RegisterUserGroupsForm()
    return render(request, 'groups/register.html', {'form': form})

@login_required(redirect_field_name='')
def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('/')  # Перенаправление на страницу входа
    else:
        form = CompanyRegistrationForm()
    return render(request, 'companies/register.html', {'form': form})

@login_required(redirect_field_name='')
def register_user_roles(request):
    if request.method == 'POST':
        form = RegisterRolesDict(request.POST)
        if form.is_valid():
            user_role = form.save(commit=False)
            user_role.save()
            return redirect('/')  # Перенаправление на страницу входа
    else:
        form = RegisterRolesDict()
    return render(request, 'user_roles/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Хешируем пароль
            user.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Использование authenticate
            if user is not None:
                login(request, user)  # Логин пользователя
                return redirect('/')  # Перенаправление на главную страницу
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль.')  # Общая ошибка
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required(redirect_field_name='')
def home_view(request):
    return render(request, 'home/home.html')