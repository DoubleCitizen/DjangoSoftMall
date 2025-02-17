# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter.font import names

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Companies(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey('PropertyCodeDict', models.CASCADE, blank=True, null=True, verbose_name="Свойства")
    name = models.CharField(max_length=255, verbose_name="Компания", unique=True)
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    inn = models.CharField(max_length=16, verbose_name="ИНН", unique=True)
    kpp = models.CharField(max_length=9, verbose_name="КПП", unique=True)
    ogrn = models.CharField(max_length=13, blank=True, null=True, verbose_name="ОГРН", unique=True)
    bic = models.CharField(max_length=9, blank=True, null=True, verbose_name="БИК", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'companies'
        db_table_comment = 'Таблица с компаниями'
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        indexes = [
            models.Index(fields=['inn'], name='idx_companies_inn'),
            models.Index(fields=['kpp'], name='idx_companies_kpp'),
            models.Index(fields=['ogrn'], name='idx_companies_ogrn'),
            models.Index(fields=['bic'], name='idx_companies_bic'),
            models.Index(fields=['property'], name='idx_companies_property_id'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['inn'], name='companies_inn_unique'),
            models.UniqueConstraint(fields=['kpp'], name='companies_kpp_unique'),
            models.UniqueConstraint(fields=['ogrn'], name='companies_ogrn_unique'),
            models.UniqueConstraint(fields=['bic'], name='companies_bic_unique'),
        ]


class CompanyProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.CASCADE)
    property_code = models.OneToOneField('PropertyCodeDict', models.CASCADE)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.value

    class Meta:
        managed = True
        db_table = 'company_properties'
        db_table_comment = 'Таблица свойств компаний'
        indexes = [
            models.Index(fields=['company'], name='idx_comp_prop_comp_id'),
            models.Index(fields=['property_code'], name='idx_comp_prop_prop_code_id'),
            models.Index(fields=['company', 'property_code'], name='idx_c_proper_comp_prop'),
        ]


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.CASCADE)
    code = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'departments'
        db_table_comment = 'Таблица с подраздлений'
        indexes = [
            models.Index(fields=['company', 'code'], name='idx_depart_comp_id_code'),
            models.Index(fields=['company', 'name'], name='idx_depart_comp_id_name'),
            models.Index(fields=['code'], name='idx_departments_code'),
            models.Index(fields=['name'], name='idx_departments_name'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'code'],
                name='departments_company_id_code_unique'
            ),
        ]


class FunctionsDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=30, unique=True)
    version = models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.code

    class Meta:
        managed = True
        db_table = 'functions_dict'
        db_table_comment = 'Таблица справочник ролевых функций'
        indexes = [
            models.Index(fields=['code', 'version'], name='idx_func_dict_code_version'),
        ]



class License(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.CASCADE)
    lisense_key = models.CharField(max_length=1000)
    active_from = models.DateField()
    active_to = models.DateField()

    class Meta:
        managed = True
        db_table = 'license'
        db_table_comment = 'Таблица с лицензиями'
        indexes = [
            models.Index(fields=['company'], name='idx_license_company_id'),
            models.Index(fields=['active_from'], name='idx_license_active_from'),
            models.Index(fields=['active_to'], name='idx_license_active_to'),
            models.Index(fields=['company', 'active_from'], name='idx_lic_comp_id_active_from'),
            models.Index(
                fields=['company', 'active_from', 'active_to'],
                name='idx_l_co_i_act_fr_act_to'
            ),
        ]


class ModuleCompanyLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.ForeignKey('Modules', models.CASCADE)
    company = models.ForeignKey(Companies, models.CASCADE)
    position = models.IntegerField()
    active_from = models.DateField()
    active_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'module_company_links'
        db_table_comment = 'Таблица связей модулей и компаний'
        indexes = [
            models.Index(fields=['company'], name='idx_modul_comp_l_company_id'),
            models.Index(fields=['module'], name='idx_modul_comp_l_module_id'),
            models.Index(fields=['active_from'], name='idx_modul_comp_l_active_from'),
            models.Index(fields=['active_to'], name='idx_modul_comp_l_active_to'),
            models.Index(
                fields=['company', 'active_from', 'active_to'],
                name='idx_m_c_l_c_i_a_fr_active_to'
            ),
            models.Index(fields=['module', 'company'], name='idx_mod_com_l_mod_company'),
        ]


class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'modules'
        db_table_comment = 'Таблица дополнительных модулей'
        indexes = [
            models.Index(fields=['code'], name='idx_modules_code'),
            models.Index(fields=['name'], name='idx_modules_name'),
        ]


class PropertyCodeDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    group_code = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}({self.code})"

    class Meta:
        managed = True
        db_table = 'property_code_dict'
        db_table_comment = 'Таблица справочник кодов для свойств пользователя\nPROFILE_IMAGE - путь до картинки с профилем пользователя\nUSER_MOBILE - телефон пользователя\nUSER_NUMVER - индиыидуальный номер пользователя'
        constraints = [
            models.UniqueConstraint(
                fields=['group_code', 'code'],
                name='property_code_dict_group_code_code_unique'
            ),
        ]
        indexes = [
            models.Index(fields=['code'], name='idx_property_code_dict_code'),
            models.Index(fields=['group_code', 'code'], name='idx_prop_cod_d_gr_co_code'),
            models.Index(fields=['name'], name='idx_property_code_dict_name'),
        ]

class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField()
    version = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'reports'
        db_table_comment = 'Таблица справочник отчетов'
        indexes = [
            models.Index(fields=['code'], name='idx_reports_code'),
            models.Index(fields=['name'], name='idx_reports_name'),
            models.Index(fields=['code', 'version'], name='idx_reports_code_version'),
        ]


class RoleFunctions(models.Model):
    id = models.SmallAutoField(primary_key=True)
    role = models.ForeignKey('RolesDict', models.CASCADE)
    function_code = models.ForeignKey(FunctionsDict, models.CASCADE)

    def __str__(self):
        return self.function_code

    class Meta:
        managed = True
        db_table = 'role_functions'
        db_table_comment = 'Таблица с ролевыми функциями'
        indexes = [
            models.Index(fields=['role'], name='idx_role_functions_role_id'),
            models.Index(fields=['function_code'], name='idx_rol_func_func_cod_id'),
            models.Index(fields=['role', 'function_code'], name='idx_role_functions_role_func'),
        ]


class RolesDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=30, verbose_name='Код роли', unique=True)
    name = models.CharField(max_length=60, verbose_name='Имя роли', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'roles_dict'
        db_table_comment = 'Таблица справочник ролей пользователя'
        indexes = [
            models.Index(fields=['code'], name='idx_roles_dict_code'),
            models.Index(fields=['name'], name='idx_roles_dict_name'),
        ]


class Settings(models.Model):
    id = models.SmallAutoField(primary_key=True)
    setting_code = models.ForeignKey('SettingsDict', models.CASCADE)
    value = models.CharField(max_length=255)
    active_from = models.DateField()
    active_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'settings'
        db_table_comment = 'Таблица общих свойст'
        indexes = [
            models.Index(fields=['setting_code'], name='idx_settings_setting_code_id'),
            models.Index(fields=['active_from'], name='idx_settings_active_from'),
            models.Index(fields=['active_to'], name='idx_settings_active_to'),
            models.Index(fields=['active_from', 'active_to'], name='idx_sett_act_from_act_to'),
            models.Index(
                fields=['setting_code', 'active_from', 'active_to'],
                name='idx_set_set_c_id_act_fr_act_to'
            ),
            models.Index(
                fields=['setting_code', 'active_to'],
                name='idx_set_set_code_id_act_to'
            ),
        ]


class SettingsDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'settings_dict'
        db_table_comment = 'Таблица справочник кодов системы'
        indexes = [
            models.Index(fields=['code'], name='idx_settings_dict_code'),
            models.Index(fields=['name'], name='idx_settings_dict_name'),
        ]


class ShablonDict(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shablon_dict'
        db_table_comment = 'Таблици справочник шаблонов'
        indexes = [
            models.Index(fields=['code'], name='idx_shablon_dict_code'),
            models.Index(fields=['name'], name='idx_shablon_dict_name'),
        ]


class StatusDict(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'status_dict'
        indexes = [
            models.Index(fields=['code'], name='idx_status_dict_code'),
            models.Index(fields=['name'], name='idx_status_dict_name'),
        ]


class TimezoneDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    timezone_name = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.timezone_name

    class Meta:
        managed = True
        db_table = 'timezone_dict'
        db_table_comment = 'Таблица с справчоник таймзон'
        indexes = [
            models.Index(fields=['timezone_name'], name='idx_timezone_dict_name'),
            models.Index(fields=['timezone'], name='idx_timezone_dict_timezone'),
        ]


class UserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.CASCADE, verbose_name='Компания')
    group_name = models.CharField(max_length=255, verbose_name='Имя группы')
    comment = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Комментарий')

    def __str__(self):
        return f"{self.company}: {self.group_name}"

    class Meta:
        managed = True
        db_table = 'user_groups'
        db_table_comment = 'Таблица групп пользователей'
        indexes = [
            models.Index(fields=['group_name'], name='idx_user_groups_group_name'),
            models.Index(fields=['company', 'group_name'], name='idx_user_groups_company_group'),
        ]


class UserProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.CASCADE)
    property_code = models.OneToOneField(PropertyCodeDict, models.CASCADE)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_properties'
        db_table_comment = 'Таблица свойств пользователей'
        constraints = [
            models.UniqueConstraint(
                fields=['property_code'],
                name='user_properties_property_code_id_unique'
            ),
        ]
        indexes = [
            models.Index(fields=['user'], name='idx_user_properties_user_id'),
            models.Index(fields=['user', 'property_code'], name='id_us_prop_us_id_prop_cod_id'),
            models.Index(fields=['property_code'], name='idx_us_prop_prop_code'),
        ]


class UserReportLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.CASCADE)
    report = models.ForeignKey(Reports, models.CASCADE)
    created_date = models.DateField()
    acive_from = models.DateField()
    active_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_report_links'
        db_table_comment = 'Таблица связей отчетов и пользователей'
        indexes = [
            models.Index(fields=['user'], name='id_us_rep_lin_user_id'),
            models.Index(fields=['report'], name='id_us_rep_lin_report_id'),
            models.Index(fields=['created_date'], name='id_us_rep_lin_created_date'),
            models.Index(fields=['acive_from'], name='id_us_rep_lin_active_from'),
            models.Index(fields=['active_to'], name='id_us_rep_lin_active_to'),
            models.Index(fields=['user', 'report'], name='id_us_rep_lin_user_report'),
        ]


class UserRoles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.CASCADE, verbose_name='Пользователь')
    role = models.ForeignKey(RolesDict, models.CASCADE, verbose_name='Роли')
    active_from = models.DateField(auto_now=True)
    active_to = models.DateField(blank=True, null=True)

    @classmethod
    def get_current_roles_dict(cls):
        return dict(
            cls.objects.select_related('role')
            .values_list('user_id', 'role__name')
        )

    class Meta:
        managed = True
        db_table = 'user_roles'
        db_table_comment = 'Таблица ролей пользователей'
        indexes = [
            models.Index(fields=['user'], name='idx_user_roles_user_id'),
            models.Index(fields=['role'], name='idx_user_roles_role_id'),
            models.Index(fields=['user', 'role', 'active_to'], name='idx_user_r_u_i_r_i_active_to'),
            models.Index(fields=['active_from'], name='idx_user_roles_active_from'),
            models.Index(fields=['active_to'], name='idx_user_roles_active_to'),
        ]


class UserSendings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('Users', models.CASCADE)
    status = models.ForeignKey(StatusDict, models.CASCADE)
    created_date = models.DateField()
    message = models.CharField(max_length=4000)

    class Meta:
        managed = True
        db_table = 'user_sendings'
        db_table_comment = 'Таблица рассылки сообщений по пользователям'
        indexes = [
            models.Index(fields=['user'], name='idx_user_sendings_user_id'),
            models.Index(fields=['status'], name='idx_user_sendings_status_id'),
            models.Index(fields=['created_date'], name='idx_user_sendings_created_date'),
            models.Index(fields=['user', 'status'], name='idx_user_sendings_user_status'),
        ]


class Users(AbstractUser):
    # Обнуляем ненужные поля из AbstractUser
    first_name = None
    last_name = None
    email = None
    date_joined = None
    is_staff = None

    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.CASCADE, null=True, blank=True, verbose_name="Компания")
    group = models.ForeignKey(UserGroups, models.CASCADE, null=True, blank=True, verbose_name="Группа")
    timezone = models.ForeignKey(TimezoneDict, models.CASCADE, null=True, blank=True, verbose_name="Часовой пояс")
    username = models.CharField(max_length=60, verbose_name="Логин", unique=True)
    firstname = models.CharField(max_length=60, verbose_name="Имя")
    lastname = models.CharField(max_length=60, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=60, blank=True, null=True, verbose_name="Отчество")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    user_lock = models.BooleanField(default=False, verbose_name="Блокировка пользователя")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    comment = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Комментарий")

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
    )

    class Meta:
        managed = True
        db_table = 'users'
        db_table_comment = 'Таблица пользователей'
        indexes = [
            models.Index(fields=['firstname'], name='idx_users_firstname'),
            models.Index(fields=['lastname'], name='idx_users_lastname'),
            models.Index(fields=['firstname', 'lastname'], name='idx_users_fullname'),
            models.Index(fields=['group'], name='idx_users_group_id'),
            models.Index(fields=['timezone'], name='idx_users_timezone_id'),
            models.Index(fields=['company'], name='idx_users_company_id'),
            models.Index(fields=['username'], name='idx_users_username'),
            models.Index(fields=['company', 'group'], name='idx_users_company_id_group_id'),
            models.Index(fields=['username', 'user_lock'], name='idx_users_username_user_lock'),
            models.Index(fields=['id', 'company'], name='idx_users_id_company_id'),
            models.Index(fields=['id', 'group'], name='idx_users_id_group_id'),
            models.Index(fields=['user_lock'], name='idx_users_user_lock'),
            models.Index(fields=['company', 'user_lock'], name='idx_users_company_lock_status'),
        ]
