from app_prof_training.models import CategoryProfTrain, ProgramProfTrain
import csv
from django.core.management.base import BaseCommand


def import_data():
    with open('/Users/artemgoranskij/Desktop/1_37.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            ProgramProfTrain.objects.create(
                title=row[0],
                code_num=row[1],
                class_num=row[2],
                category=CategoryProfTrain.objects.get(pk=69)
            )


class Command(BaseCommand):
    def handle(self, *args, **options):
        import_data()
        print('success')
