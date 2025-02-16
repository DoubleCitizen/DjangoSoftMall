from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Заполнить все таблицы в базе данных, начальными данными'

    def handle(self, *args, **options):
        commands = [
            ('start_fill_db_timezones', {}),
            ('start_fill_db_roles_functions', {}),
            ('start_fill_db_companies', {}),
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