from django.core.management.base import BaseCommand, CommandError
import owid.service as service

class Command(BaseCommand):

    help = 'Downloads covid json data and updates owid database'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        service.download_and_update_covid()
        self.stdout.write(self.style.SUCCESS('Successfully downloaded json data and updated owid db'))



