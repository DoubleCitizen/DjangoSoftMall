import json
import os
from datetime import datetime, timedelta, time

from django.core.management import BaseCommand
from django.db import migrations

from ...models import TimezoneDict


class Command(BaseCommand):
    help = 'Заполнение базы данных таймзонами'

    def handle(self, *args, **options):
        TimezoneDict.objects.all().delete()
        time_zone_dict = []
        with open('core/management/commands/time_zones.json', 'r') as file:
            datas = json.loads(file.read())
        for item in datas:
            timezone_str = item['timezone']
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

            item['timezone'] = formatted_time
            time_zone_dict.append(TimezoneDict(**item))
        TimezoneDict.objects.bulk_create(time_zone_dict)

        self.stdout.write(self.style.SUCCESS('Успешное заполнение БД таймзонами.'))
