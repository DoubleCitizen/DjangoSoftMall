from django.core.management import BaseCommand, call_command

from core.models import RoleFunctions


class Command(BaseCommand):
    help = 'Заполнить все таблицы в базе данных, начальными данными'

    def handle(self, *args, **options):
        if len(RoleFunctions.objects.all()) == 0:
            commands = [
                ('start_fill_db_companies', {}),
                ('start_fill_db_timezones', {}),
                ('start_fill_db_roles_functions', {}),
                ('start_fill_db_groups', {}),
                ('start_fill_db_company_property', {}),
            ]
            for command, params in commands:
                self.stdout.write(f'Запуск команды: {command}')
                try:
                    call_command(command, **params)
                    self.stdout.write(self.style.SUCCESS(f'Команда {command} выполнена успешно'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Ошибка в команде {command}: {str(e)}'))
                    if not options.get('force'):
                        raise