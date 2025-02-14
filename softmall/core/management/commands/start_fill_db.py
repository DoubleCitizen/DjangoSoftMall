import json
import os
from datetime import datetime, timedelta, time

from django.core.management import BaseCommand
from django.db import migrations

from core.models import TimezoneDict


class Command(BaseCommand):
    help = 'Fill the database with timezone data'

    def handle(self, *args, **options):
        time_zone_dict = []
        print(f"os.getcwd() = {os.getcwd()}")
        with open('core/management/commands/time_zones.json', 'r') as file:
            datas = json.loads(file.read())
        for item  in datas:
            timezone_str = item['timezone']
            # Преобразуем строку временной зоны в timedelta
            if timezone_str.startswith('-'):
                hours, minutes = map(int, timezone_str[1:].split(':'))
                time_offset = timedelta(hours=-hours, minutes=-minutes)
            else:
                hours, minutes = map(int, timezone_str.split(':'))
                time_offset = timedelta(hours=hours, minutes=minutes)

            # Преобразуем timedelta в datetime.time
            total_seconds = int(time_offset.total_seconds())
            abs_seconds = abs(total_seconds)
            hours = abs_seconds // 3600
            minutes = (abs_seconds % 3600) // 60

            # Создаем объект time без знака
            formatted_time = time(hour=hours, minute=minutes)

            item['timezone'] = formatted_time  # Сохраняем time в словаре
            print(f"item = {item}")
            time_zone_dict.append(TimezoneDict(**item))
        TimezoneDict.objects.bulk_create(time_zone_dict)

        self.stdout.write(self.style.SUCCESS('Successfully filled the database with timezone data.'))

# def create_timezones(apps, schema_editor):
#     TimezoneDict = apps.get_model('your_app_name', 'TimezoneDict')
#     timezones = [
#         {'timezone_name': 'UTC', 'timezone': '00:00'},
#         {'timezone_name': 'Europe/Moscow', 'timezone': '03:00'},
#         {'timezone_name': 'America/New_York', 'timezone': '-05:00'},
#         {'timezone_name': 'Asia/Tokyo', 'timezone': '09:00'},
#         # Добавьте другие временные зоны по мере необходимости
#     ]
#     TimezoneDict.objects.bulk_create([TimezoneDict(**tz) for tz in timezones])
#
# class Migration(migrations.Migration):
#     dependencies = [
#         ('your_app_name', 'previous_migration_file_name'),
#     ]
#
#     operations = [
#         migrations.RunPython(create_timezones),
#     ]
