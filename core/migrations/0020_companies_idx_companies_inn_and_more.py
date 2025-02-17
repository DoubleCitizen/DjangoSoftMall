# Generated by Django 5.1.6 on 2025-02-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0019_alter_companies_property_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='companies',
            index=models.Index(fields=['inn'], name='idx_companies_inn'),
        ),
        migrations.AddIndex(
            model_name='companies',
            index=models.Index(fields=['kpp'], name='idx_companies_kpp'),
        ),
        migrations.AddIndex(
            model_name='companies',
            index=models.Index(fields=['ogrn'], name='idx_companies_ogrn'),
        ),
        migrations.AddIndex(
            model_name='companies',
            index=models.Index(fields=['bic'], name='idx_companies_bic'),
        ),
        migrations.AddIndex(
            model_name='companies',
            index=models.Index(fields=['property'], name='idx_companies_property_id'),
        ),
        migrations.AddIndex(
            model_name='departments',
            index=models.Index(fields=['company'], name='idx_departments_company_id'),
        ),
        migrations.AddIndex(
            model_name='departments',
            index=models.Index(fields=['code'], name='idx_departments_code'),
        ),
        migrations.AddIndex(
            model_name='usergroups',
            index=models.Index(fields=['company'], name='idx_user_groups_company_id'),
        ),
        migrations.AddIndex(
            model_name='userroles',
            index=models.Index(fields=['user'], name='idx_user_roles_user_id'),
        ),
        migrations.AddIndex(
            model_name='userroles',
            index=models.Index(fields=['role'], name='idx_user_roles_role_id'),
        ),
        migrations.AddIndex(
            model_name='userroles',
            index=models.Index(fields=['user', 'role', 'active_to'], name='idx_user_r_u_i_r_i_active_to'),
        ),
        migrations.AddIndex(
            model_name='userroles',
            index=models.Index(fields=['active_from'], name='idx_user_roles_active_from'),
        ),
        migrations.AddIndex(
            model_name='userroles',
            index=models.Index(fields=['active_to'], name='idx_user_roles_active_to'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['group'], name='idx_users_group_id'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['timezone'], name='idx_users_timezone_id'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['company'], name='idx_users_company_id'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['username'], name='idx_users_username'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['company', 'group'], name='idx_users_company_id_group_id'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['username', 'user_lock'], name='idx_users_username_user_lock'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['id', 'company'], name='idx_users_id_company_id'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['id', 'group'], name='idx_users_id_group_id'),
        ),
    ]
