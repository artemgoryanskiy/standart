from app_prof_training.models import ProgramProfTrain
from django.core.management.base import BaseCommand


def add_hours():
    hours = '160-680'
    programs = ProgramProfTrain.objects.all()
    for program in programs:
        program.hours = hours
        program.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        add_hours()
        print('success')
