from django import forms
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from core.models import Users, RolesDict, Companies, UserGroups, UserRoles, FunctionsDict


class RegisterUserGroupsForm(forms.ModelForm):
    class Meta:
        model = UserGroups
        fields = ['company', 'group_name', 'comment']


class AssignRoleForm(forms.ModelForm):
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
        super().__init__(*args, **kwargs)
        self.fields['role'].queryset = RolesDict.objects.all()
        self.fields['role'].empty_label = None

        # Добавляем информацию о текущей роли
        if self.instance and self.instance.pk:
            self.fields['current_role'].initial = self.instance.role.id


class RoleForm(forms.ModelForm):
    functions = forms.ModelMultipleChoiceField(
        queryset=FunctionsDict.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = RolesDict
        fields = ["code", "name", "functions"]


class UserRegistrationForm(forms.ModelForm):
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

    company = forms.ModelChoiceField(
        queryset=Companies.objects.all(),
        widget=forms.Select,
        label='Компания',
        required=False,
        empty_label=None  # Убираем пустую опцию
    )

    group = forms.ModelChoiceField(
        queryset=UserGroups.objects.all(),
        widget=forms.Select,
        label='Группа',
        required=False,
        empty_label=None  # Убираем пустую опцию
    )

    class Meta:
        model = Users
        fields = [
            'roles', 'username', 'firstname', 'lastname', 'patronymic',
            'company', 'group', 'timezone', 'password'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Делаем поля необязательными
        self.fields['company'].required = False
        self.fields['group'].required = False
        self.fields['timezone'].required = False
        self.fields['patronymic'].required = False

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        group = cleaned_data.get('group')
        company = cleaned_data.get('company')

        if group.company != company:
            raise forms.ValidationError('Выбрана неправильная группа. Пожалуйста, смените группу.')

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data

    def save(self, commit=True):
        # Сохраняем пользователя


        user = super().save(commit=False)
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
    class Meta:
        model = Companies
        fields = ['property', 'name', 'inn', 'kpp', 'ogrn', 'bic']


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
