from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='vvd.2209@bk.ru',
            country='Russia',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('1234')
        user.save()
