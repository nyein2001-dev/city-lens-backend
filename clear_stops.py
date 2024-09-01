import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
django.setup()

from django.core.management.base import BaseCommand
from dashboard.models import Stop

class Command(BaseCommand):
    help = 'Clear all Stop data'

    def handle(self, *args, **kwargs):
        Stop.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all Stop data'))


if __name__ == "__main__":
    Command().handle()
