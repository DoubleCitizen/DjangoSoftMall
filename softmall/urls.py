"""
URL configuration for softmall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *

router = DefaultRouter()
router.register(r'companies', CompaniesViewSet)
router.register(r'company_properties', CompanyPropertiesViewSet)
router.register(r'departments', DepartmentsViewSet)
router.register(r'functions_dict', FunctionsDictViewSet)
router.register(r'license', LicenseViewSet)
router.register(r'module_company_links', ModuleCompanyLinksViewSet)
router.register(r'module', ModulesViewSet)
router.register(r'property_code_dict', PropertyCodeDictViewSet)
router.register(r'reports', ReportsViewSet)
router.register(r'role_functions', RoleFunctionsViewSet)
router.register(r'role_dict', RolesDictViewSet)
router.register(r'settings', SettingsViewSet)
router.register(r'settings_dict', SettingsDictViewSet)
router.register(r'shablon_dict', ShablonDictViewSet)
router.register(r'status_dict', StatusDictViewSet)
router.register(r'timezone_dict', TimezoneDictViewSet)
router.register(r'user_groups', UserGroupsViewSet)
router.register(r'user_properties', UserPropertiesViewSet)
router.register(r'user_report_links', UserReportLinksViewSet)
router.register(r'user_roles', UserRolesViewSet)
router.register(r'user_sendings', UserSendingsViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include(router.urls)),
]
