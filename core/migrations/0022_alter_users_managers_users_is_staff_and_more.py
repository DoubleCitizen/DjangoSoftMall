# Generated by Django 5.1.6 on 2025-02-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_departments_idx_departments_company_id_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='users',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
