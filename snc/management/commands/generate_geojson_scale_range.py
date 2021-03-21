from django.core.management.base import BaseCommand, CommandError
import snc.service_parse as service_parse
import snc.service_geojson as service_geojson
from snc.const import *
import time


class Command(BaseCommand):

    help = 'Generates and saves geojson for all scale ranges'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        #service_download.download_and_save_catalogue()
        time.sleep(10)
        service_geojson.generate_geojson_and_save_db(SCALE_RANGE_ALL)
        self.stdout.write(self.style.SUCCESS('Successfully generated and saved geojson for all scale ranges'))





