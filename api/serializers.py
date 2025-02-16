from rest_framework import serializers
from core.models import (
    Companies,
    CompanyProperties,
    Departments,
    FunctionsDict,
    License,
    ModuleCompanyLinks,
    Modules,
    PropertyCodeDict,
    Reports,
    RoleFunctions,
    RolesDict,
    Settings,
    SettingsDict,
    ShablonDict,
    StatusDict,
    TimezoneDict,
    UserGroups,
    UserProperties,
    UserReportLinks,
    UserRoles,
    UserSendings,
    Users,
)

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'  # Или укажите конкретные поля, если нужно

class CompanyPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProperties
        fields = '__all__'

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class FunctionsDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionsDict
        fields = '__all__'

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

class ModuleCompanyLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleCompanyLinks
        fields = '__all__'

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'

class PropertyCodeDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCodeDict
        fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class RoleFunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleFunctions
        fields = '__all__'

class RolesDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesDict
        fields = '__all__'

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class SettingsDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsDict
        fields = '__all__'

class ShablonDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShablonDict
        fields = '__all__'

class StatusDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDict
        fields = '__all__'

class TimezoneDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimezoneDict
        fields = '__all__'

class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroups
        fields = '__all__'

class UserPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProperties
        fields = '__all__'

class UserReportLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReportLinks
        fields = '__all__'

class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'

class UserSendingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSendings
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'