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
    property = models.ForeignKey('PropertyCodeDict', models.DO_NOTHING, blank=True, null=True, verbose_name="Свойства")
    name = models.CharField(max_length=255, verbose_name="Компания")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    inn = models.CharField(max_length=16, verbose_name="ИНН")
    kpp = models.CharField(max_length=9, verbose_name="КПП")
    ogrn = models.CharField(max_length=13, blank=True, null=True, verbose_name="ОГРН")
    bic = models.CharField(max_length=9, blank=True, null=True, verbose_name="БИК")

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'companies'
        db_table_comment = 'Таблица с компаниями'
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class CompanyProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    property_code = models.OneToOneField('PropertyCodeDict', models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'company_properties'
        db_table_comment = 'Таблица свойств компаний'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    code = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'departments'
        db_table_comment = 'Таблица с подраздлений'


class FunctionsDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=30)
    version = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        # Если запись уже существует, увеличиваем version на 1
        if self.pk:
            self.version += 1
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'functions_dict'
        db_table_comment = 'Таблица справочник ролевых функций'


class License(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    lisense_key = models.CharField(max_length=1000)
    active_from = models.DateField()
    active_to = models.DateField()

    class Meta:
        managed = True
        db_table = 'license'
        db_table_comment = 'Таблица с лицензиями'


class ModuleCompanyLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.ForeignKey('Modules', models.DO_NOTHING)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    position = models.IntegerField()
    active_from = models.DateField()
    active_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'module_company_links'
        db_table_comment = 'Таблица связей модулей и компаний'


class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'modules'
        db_table_comment = 'Таблица дополнительных модулей'


class PropertyCodeDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    group_code = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'property_code_dict'
        db_table_comment = 'Таблица справочник кодов для свойств пользователя\nPROFILE_IMAGE - путь до картинки с профилем пользователя\nUSER_MOBILE - телефон пользователя\nUSER_NUMVER - индиыидуальный номер пользователя'


class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField()
    version = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'reports'
        db_table_comment = 'Таблица справочник отчетов'


class RoleFunctions(models.Model):
    id = models.SmallAutoField(primary_key=True)
    role = models.ForeignKey('RolesDict', models.DO_NOTHING)
    function_code = models.ForeignKey(FunctionsDict, models.DO_NOTHING)

    def __str__(self):
        return self.function_code

    class Meta:
        managed = True
        db_table = 'role_functions'
        db_table_comment = 'Таблица с ролевыми функциями'


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


class Settings(models.Model):
    id = models.SmallAutoField(primary_key=True)
    setting_code = models.ForeignKey('SettingsDict', models.DO_NOTHING)
    value = models.CharField(max_length=255)
    active_from = models.DateField()
    active_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'settings'
        db_table_comment = 'Таблица общих свойст'


class SettingsDict(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'settings_dict'
        db_table_comment = 'Таблица справочник кодов системы'


class ShablonDict(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shablon_dict'
        db_table_comment = 'Таблици справочник шаблонов'


class StatusDict(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'status_dict'


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


class UserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, verbose_name='Компания')
    group_name = models.CharField(max_length=255, verbose_name='Имя группы')
    comment = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Комментарий')

    def __str__(self):
        return self.group_name

    class Meta:
        managed = True
        db_table = 'user_groups'
        db_table_comment = 'Таблица групп пользователей'


class UserProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    property_code = models.OneToOneField(PropertyCodeDict, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_properties'
        db_table_comment = 'Таблица свойств пользователей'


class UserReportLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    report = models.ForeignKey(Reports, models.DO_NOTHING)
    created_date = models.DateField()
    acive_from = models.DateField()
    active_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_report_links'
        db_table_comment = 'Таблица связей отчетов и пользователей'

class UserRoles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, verbose_name='Пользователь')
    role = models.ForeignKey(RolesDict, models.DO_NOTHING, verbose_name='Роли')
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


class UserSendings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    status = models.ForeignKey(StatusDict, models.DO_NOTHING)
    created_date = models.DateField()
    message = models.CharField(max_length=4000)

    class Meta:
        managed = True
        db_table = 'user_sendings'
        db_table_comment = 'Таблица рассылки сообщений по пользователям'


class Users(AbstractUser):
    # Обнуляем ненужные поля из AbstractUser
    first_name = None
    last_name = None
    email = None
    date_joined = None
    is_staff = None

    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, null=True, blank=True, verbose_name="Компания")
    group = models.ForeignKey(UserGroups, models.DO_NOTHING, null=True, blank=True, verbose_name="Группа")
    timezone = models.ForeignKey(TimezoneDict, models.DO_NOTHING, null=True, blank=True, verbose_name="Часовой пояс")
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
        related_name='custom_user_set',  # Указываем уникальное имя для обратной ссылки
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Указываем уникальное имя для обратной ссылки
        blank=True,
    )

    class Meta:
        managed = True
        db_table = 'users'
        db_table_comment = 'Таблица пользователей'
