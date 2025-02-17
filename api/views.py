from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from core.consts import RolesFunctionsViewSet
from core.models import *
from api.serializers import *
from core.permission import CustomPermission, PermissionClasses


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.COMPANIES_VIEW_SET.value)]


class CompanyPropertiesViewSet(viewsets.ModelViewSet):
    queryset = CompanyProperties.objects.all()
    serializer_class = CompanyPropertiesSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.COMPANY_PROPERTIES_VIEW_SET.value)]

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.DEPARTMENTS_VIEW_SET.value)]

class FunctionsDictViewSet(viewsets.ModelViewSet):
    queryset = FunctionsDict.objects.all()
    serializer_class = FunctionsDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.FUNCTIONS_DICT_VIEW_SET.value)]

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.LICENSE_VIEW_SET.value)]

class ModuleCompanyLinksViewSet(viewsets.ModelViewSet):
    queryset = ModuleCompanyLinks.objects.all()
    serializer_class = ModuleCompanyLinksSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.MODULE_COMPANY_LINKS_VIEW_SET.value)]

class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.MODULES_VIEW_SET.value)]

class PropertyCodeDictViewSet(viewsets.ModelViewSet):
    queryset = PropertyCodeDict.objects.all()
    serializer_class = PropertyCodeDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.PROPERTY_CODE_DICT_VIEW_SET.value)]

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.REPORTS_VIEW_SET.value)]

class RoleFunctionsViewSet(viewsets.ModelViewSet):
    queryset = RoleFunctions.objects.all()
    serializer_class = RoleFunctionsSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.ROLE_FUNCTIONS_VIEW_SET.value)]

class RolesDictViewSet(viewsets.ModelViewSet):
    queryset = RolesDict.objects.all()
    serializer_class = RolesDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.ROLES_DICT_VIEW_SET.value)]

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.SETTINGS_VIEW_SET.value)]

class SettingsDictViewSet(viewsets.ModelViewSet):
    queryset = SettingsDict.objects.all()
    serializer_class = SettingsDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.SETTINGS_DICT_VIEW_SET.value)]

class ShablonDictViewSet(viewsets.ModelViewSet):
    queryset = ShablonDict.objects.all()
    serializer_class = ShablonDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.SHABLON_DICT_VIEW_SET.value)]

class StatusDictViewSet(viewsets.ModelViewSet):
    queryset = StatusDict.objects.all()
    serializer_class = StatusDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.STATUS_DICT_VIEW_SET.value)]

class TimezoneDictViewSet(viewsets.ModelViewSet):
    queryset = TimezoneDict.objects.all()
    serializer_class = TimezoneDictSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.TIMEZONE_DICT_VIEW_SET.value)]

class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.USER_GROUPS_VIEW_SET.value)]

class UserPropertiesViewSet(viewsets.ModelViewSet):
    queryset = UserProperties.objects.all()
    serializer_class = UserPropertiesSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.USER_PROPERTIES_VIEW_SET.value)]

class UserReportLinksViewSet(viewsets.ModelViewSet):
    queryset = UserReportLinks.objects.all()
    serializer_class = UserReportLinksSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.USER_REPORT_LINKS_VIEW_SET.value)]

class UserRolesViewSet(viewsets.ModelViewSet):
    queryset = UserRoles.objects.all()
    serializer_class = UserRolesSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.USER_ROLES_VIEW_SET.value)]

class UserSendingsViewSet(viewsets.ModelViewSet):
    queryset = UserSendings.objects.all()
    serializer_class = UserSendingsSerializer
    permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.USER_SENDINGS_VIEW_SET.value)]

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = [PermissionClasses.permission_classes.get(RolesFunctionsViewSet.USERS_VIEW_SET.value)]

