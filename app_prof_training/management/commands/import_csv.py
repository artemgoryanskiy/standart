from app_prof_training.models import Program, Category
import csv
from django.core.management.base import BaseCommand


def import_data():
    with open('/Users/artemgoranskij/Desktop/1_32.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            Program.objects.create(
                code_num=row[0],
                title=row[1],
                class_num=row[2],
                category=Category.objects.get(pk=32)
            )


class Command(BaseCommand):
    def handle(self, *args, **options):
        import_data()
        print('success')
