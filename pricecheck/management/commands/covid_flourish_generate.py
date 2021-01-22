from django.core.management.base import BaseCommand, CommandError
import owid.service_race as service_race

class Command(BaseCommand):

    help = 'Generates CSV files for Flourish race charts.'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        service_race.generate_flourish_csv()
        self.stdout.write(self.style.SUCCESS('Successfully generated CSV files for race charts'))



