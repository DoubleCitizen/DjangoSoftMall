from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from core.consts import RolesFunctions
from core.forms import UserRegistrationForm, UserLoginForm, CompanyRegistrationForm, RegisterUserGroupsForm, \
    RoleForm
from core.models import Users, RolesDict, RoleFunctions, UserRoles
from core.permission import role_required

@login_required(redirect_field_name='')
@role_required(RolesFunctions.REGISTER_GROUP)  # Затем проверка роли
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
@role_required(RolesFunctions.REGISTER_COMPANY)
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
@role_required(RolesFunctions.CREATE_ROLE)
def create_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            role = form.save()
            # Сохраняем выбранные функции
            for function in form.cleaned_data["functions"]:
                RoleFunctions.objects.create(role=role, function_code=function)
            return redirect("/")
    else:
        form = RoleForm()
    return render(request, "user_roles/register.html", {"form": form})

@login_required(redirect_field_name='')
@role_required(RolesFunctions.ASSIGN_ROLE)
def assign_role(request):
    # Оптимизированные запросы с предварительной выборкой
    users = Users.objects.order_by('lastname', 'firstname')
    roles = RolesDict.objects.all()
    selected_user = None
    current_role = None

    if request.method == "POST":
        user_id = request.POST.get('user')
        role_id = request.POST.get('role')

        if user_id and role_id:
            try:
                user = Users.objects.get(id=user_id)
                role = RolesDict.objects.get(id=role_id)

                UserRoles.objects.update_or_create(
                    user=user,
                    defaults={'role': role}
                )
                return redirect('/user_role/assign_role')
            except (Users.DoesNotExist, RolesDict.DoesNotExist) as e:
                # Обработка ошибки
                pass

    # Обработка GET-параметра
    if 'user' in request.GET:
        user_id = request.GET.get('user')
        try:
            selected_user = Users.objects.get(id=user_id)
            try:
                current_role = UserRoles.objects.get(user=selected_user).role
            except UserRoles.DoesNotExist:
                current_role = None
        except Users.DoesNotExist:
            selected_user = None

    return render(request, "user_roles/assign_role.html", {
        'users': users,
        'roles': roles,
        'selected_user': selected_user,
        'current_role': current_role,
    })


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user is None:
                return redirect('/register/')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)  # Хешируем пароль
            user.save()
            user = authenticate(request, username=username, password=password)  # Использование authenticate
            if user is not None:
                login(request, user)  # Логин пользователя
                return redirect('/')  # Перенаправление на главную страницу
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль.')  # Общая ошибка
            return redirect('/')  # Перенаправление на страницу входа
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
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


def logout_user(request):
    logout(request)  # Выход из системы
    return redirect('login')  # Перенаправление на страницу входа


@login_required(redirect_field_name='')
def home_view(request):
    return render(request, 'home/home.html')
