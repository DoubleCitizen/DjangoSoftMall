from django import forms
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from core.models import Users, RolesDict, Companies, UserGroups, UserRoles, FunctionsDict


class RegisterUserGroupsForm(forms.ModelForm):
    """Форма для регистрации новых пользовательских групп"""

    class Meta:
        model = UserGroups
        fields = ['company', 'group_name', 'comment']


class AssignRoleForm(forms.ModelForm):
    """Форма для назначения ролей пользователям"""
    current_role = forms.CharField(required=False, widget=forms.HiddenInput())
    user = forms.ModelChoiceField(
        queryset=Users.objects.all(),
        widget=forms.Select(attrs={'class': 'user-select'})
    )

    class Meta:
        model = UserRoles
        fields = ['user', 'role']
        widgets = {
            'role': forms.RadioSelect(),
            'user': forms.Select(attrs={'class': 'user-select'})
        }

    def __init__(self, *args, **kwargs):
        """Инициализация формы с настройкой выбора ролей"""
        super().__init__(*args, **kwargs)
        self.fields['role'].queryset = RolesDict.objects.all()
        self.fields['role'].empty_label = None

        # Добавляем информацию о текущей роли
        if self.instance and self.instance.pk:
            self.fields['current_role'].initial = self.instance.role.id


class RoleForm(forms.ModelForm):
    """Форма для создания и редактирования ролей"""
    functions = forms.ModelMultipleChoiceField(
        queryset=FunctionsDict.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = RolesDict
        fields = ["code", "name", "functions"]


class UserRegistrationForm(forms.ModelForm):
    """Форма регистрации новых пользователей с расширенной функциональностью"""
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтверждение пароля')

    # Поле для выбора ролей
    roles = forms.ModelChoiceField(  # Изменено на ModelChoiceField
        queryset=RolesDict.objects.all(),
        widget=forms.Select,
        label='Установка роли при регистрации (для отладки)',
        required=False,
        empty_label=None  # Убираем пустую опцию
    )

    group = forms.ModelChoiceField(
        queryset=UserGroups.objects.all(),
        widget=forms.Select,
        label='Компания - Группа',
        required=False,
        empty_label=None  # Убираем пустую опцию
    )

    class Meta:
        model = Users
        fields = [
            'roles', 'username', 'firstname', 'lastname', 'patronymic',
            'group', 'timezone', 'password'
        ]

    def __init__(self, *args, **kwargs):
        """Настройка обязательности полей при инициализации"""
        super().__init__(*args, **kwargs)
        # Делаем поля необязательными
        self.fields['group'].required = False
        self.fields['timezone'].required = False
        self.fields['patronymic'].required = False

    def clean(self):
        """Валидация данных формы"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        group = cleaned_data.get('group')

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data

    def save(self, commit=True):
        """Сохранение пользователя с дополнительной логикой"""
        group = self.cleaned_data.get('group')
        if group is not None:
            company = Companies.objects.get(id=group.company.id)

        user = super().save(commit=False)
        if group is not None:
            user.company = company
        user.password = make_password(self.cleaned_data["password"])

        user.save()

        # Сохраняем выбранные роли через модель UserRoles
        role = self.cleaned_data.get('roles')
        if role is None:
            role = RolesDict.objects.get(name='Пользователь')
        if role:
            UserRoles.objects.create(
                user=user,
                role=role,
                active_from=timezone.now().date(),
                active_to=None
            )
        return user


class CompanyRegistrationForm(forms.ModelForm):
    """Форма регистрации новых компаний"""

    class Meta:
        model = Companies
        fields = ['property', 'name', 'inn', 'kpp', 'ogrn', 'bic']


class UserLoginForm(forms.Form):
    """Форма авторизации пользователей"""
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
