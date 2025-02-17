import json

from django.core.management import BaseCommand

from ...models import Companies, UserGroups


class Command(BaseCommand):
    help = 'Заполнение базы данных группами'

    def handle(self, *args, **options):
        UserGroups.objects.all().delete()

        with open('core/management/commands/groups_data.json', 'r', encoding='utf-8') as file:
            datas = json.loads(file.read())

        companies_data = []
        first_entry, second_entry = Companies.objects.all()[0:2]
        count_datas = len(datas)
        for i, data in enumerate(datas):
            if count_datas // 2 > i:
                data['company_id'] = first_entry.id
            else:
                data['company_id'] = second_entry.id
            companies_data.append(UserGroups(**data))

        UserGroups.objects.bulk_create(companies_data)

        self.stdout.write(self.style.SUCCESS('Успешное заполнение базы данных группами.'))