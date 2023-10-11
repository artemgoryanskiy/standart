from app_prof_retraining.models import ProgramProfRetrain, CategoryProfRetrain
import csv
from django.core.management.base import BaseCommand


def import_data():
    with open('/Users/artemgoranskij/Desktop/25.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            ProgramProfRetrain.objects.create(
                category=CategoryProfRetrain.objects.get(pk=26),
                title=row[2],
                hours=row[1],
                qualification=row[0]
            )


class Command(BaseCommand):
    def handle(self, *args, **options):
        import_data()
        print('success')
