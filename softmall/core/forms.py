from django import forms

from .models import Users, RolesDict, Companies, UserGroups, UserRoles


class RegisterUserGroupsForm(forms.ModelForm):

    class Meta:
        model = UserGroups
        fields = ['company', 'group_name', 'comment']

class RegisterUserRolesGroupsForm(forms.ModelForm):

    class Meta:
        model = UserRoles
        fields = ['user', 'role']

class RegisterRolesDict(forms.ModelForm): # todo

    class Meta:
        model = RolesDict
        fields = ['code', 'name']

class RegisterFunctionsDict(forms.ModelForm): # todo
    pass


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтверждение пароля')

    class Meta:
        model = Users
        fields =  ['username', 'firtsname', 'lastname', 'patronymic', 'company', 'group', 'timezone', 'password']

        # # Определяем поля формы
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     # Делаем поля company, group и timezone необязательными
        #     self.fields['company'].required = False
        #     self.fields['group'].required = False
        #     self.fields['timezone'].required = False

    class UserLoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

class CompanyRegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Companies
        fields = ['property', 'name', 'inn', 'kpp', 'ogrn', 'bic']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password_confirm = cleaned_data.get("password_confirm")
    #
    #     if password != password_confirm:
    #         raise forms.ValidationError("Passwords do not match.")

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
