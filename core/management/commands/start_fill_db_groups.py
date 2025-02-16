import json

from django.core.management import BaseCommand

from ...models import Companies


#todo
# class Command(BaseCommand):
#     help = 'Заполнение базы данных компаниями'
#
#     def handle(self, *args, **options):
#         Companies.objects.all().delete()
#
#         with open('core/management/commands/companies_data.json', 'r', encoding='utf-8') as file:
#             datas = json.loads(file.read())
#
#         companies_data = []
#
#         for data in datas:
#             companies_data.append(Companies(**data))
#
#         Companies.objects.bulk_create(companies_data)
#
#         self.stdout.write(self.style.SUCCESS('Успешное заполнение базы данных компаниями.'))