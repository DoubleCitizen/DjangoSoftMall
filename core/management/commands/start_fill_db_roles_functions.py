from django.core.management import BaseCommand

from ...models import FunctionsDict, RolesDict, RoleFunctions
from ...consts import RolesFunctions, RolesFunctionsViewSet


class Command(BaseCommand):
    help = 'Заполнение базы данных ролями'

    def handle(self, *args, **options):
        RoleFunctions.objects.all().delete()
        FunctionsDict.objects.all().delete()
        RolesDict.objects.all().delete()
        functions_dict_data = []
        for i, role in enumerate(RolesFunctions):
            functions_dict_data.append(FunctionsDict(code=role.value, version=str(i + 1)))
        for i, role in enumerate(RolesFunctionsViewSet):
            functions_dict_data.append(FunctionsDict(code=role.value, version=str((i + 1) * (-1))))
        FunctionsDict.objects.bulk_create(functions_dict_data)
        RolesDict.objects.create(name="Пользователь", code='1')
        role = RolesDict.objects.create(name="Супер админ", code='2')
        role_functions_data = []
        for function_code in FunctionsDict.objects.all():
            role_functions_data.append(RoleFunctions(
                role=role,
                function_code=function_code
            ))
        RoleFunctions.objects.bulk_create(role_functions_data)

        self.stdout.write(self.style.SUCCESS('Успешное заполнение базы данных ролями.'))
