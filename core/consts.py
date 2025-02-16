from enum import Enum


class RolesFunctions(Enum):
    REGISTER_GROUP = 'register_group'
    REGISTER_COMPANY = 'register_company'
    CREATE_ROLE = 'create_role'
    ASSIGN_ROLE = 'assign_role'
    LOGIN_USER = 'login_user'

class RolesFunctionsViewSet(Enum):
    #VIEW_SET
    COMPANIES_VIEW_SET = 'companies_view_set'
    COMPANY_PROPERTIES_VIEW_SET = 'company_properties_view_set'
    DEPARTMENTS_VIEW_SET = 'departments_view_set'
    FUNCTIONS_DICT_VIEW_SET = 'functions_dict_view_set'
    LICENSE_VIEW_SET = 'license_view_set'
    MODULE_COMPANY_LINKS_VIEW_SET = 'module_company_links'
    MODULES_VIEW_SET = 'modules_view_set'
    PROPERTY_CODE_DICT_VIEW_SET = 'property_code_dict_view_set'
    REPORTS_VIEW_SET = 'reports_view_set'
    ROLE_FUNCTIONS_VIEW_SET = 'role_functions_view_set'
    ROLE_VIEW_SET = 'role_view_set'
    ROLES_DICT_VIEW_SET = 'roles_dict_view_set'
    SETTINGS_VIEW_SET = 'settings_view_set'
    SETTINGS_DICT_VIEW_SET = 'settings_dict_view_set'
    SHABLON_DICT_VIEW_SET = 'shablon_dict_view_set'
    STATUS_DICT_VIEW_SET = 'status_dict_view_set'
    TIMEZONE_DICT_VIEW_SET = 'timezone_dict_view_set'
    USER_GROUPS_VIEW_SET = 'user_groups_view_set'
    USER_PROPERTIES_VIEW_SET = 'user_properties_view_set'
    USER_REPORT_LINKS_VIEW_SET = 'user_report_links_view_set'
    USER_ROLES_VIEW_SET = 'user_roles_view_set'
    USER_SENDINGS_VIEW_SET = 'user_sendings_view_set'
    USERS_VIEW_SET = 'users_view_set'