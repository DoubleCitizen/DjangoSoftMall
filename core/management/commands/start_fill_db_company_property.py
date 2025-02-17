import json

from django.core.management import BaseCommand

from ...models import PropertyCodeDict, Companies, CompanyProperties


class Command(BaseCommand):
    help = 'Заполнение базы данных свойствами компаний'

    def handle(self, *args, **options):
        PropertyCodeDict.objects.all().delete()
        CompanyProperties.objects.all().delete()

        with open('core/management/commands/company_properties.json', 'r', encoding='utf-8') as file:
            datas = json.loads(file.read())

        properties_code_dict_data = []

        for data in datas:
            properties_code_dict_data.append(PropertyCodeDict(**data))

        PropertyCodeDict.objects.bulk_create(properties_code_dict_data)

        company_properties_data = []
        for company, property_code_dict in zip(Companies.objects.all(), PropertyCodeDict.objects.all()):
            company_properties_data.append(
                CompanyProperties(
                    company_id=company.id,
                    property_code_id=property_code_dict.id,
                    value=property_code_dict.name
                )
            )
        CompanyProperties.objects.bulk_create(company_properties_data)

        self.stdout.write(self.style.SUCCESS('Успешное заполнение базы данных свойствами компаний.'))