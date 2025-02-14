# Generated by Django 5.1.6 on 2025-02-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_rolesdict_code_alter_rolesdict_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolesdict',
            name='code',
            field=models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], max_length=30, unique=True, verbose_name='Права роли'),
        ),
    ]
