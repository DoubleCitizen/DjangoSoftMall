# Generated by Django 5.1.6 on 2025-02-13 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_companies_bic_alter_companies_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.propertycodedict', verbose_name='Свойства'),
        ),
    ]
