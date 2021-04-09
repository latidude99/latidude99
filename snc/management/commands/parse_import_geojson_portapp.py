from django.core.management.base import BaseCommand, CommandError
import snc.service_parse as service_parse
import snc.service_geojson as service_geojson
from snc.const import *
import time


class Command(BaseCommand):

    help = 'Parses and imports the snc catalogue from data folder then generates geojson for all scale ranges ' \
           'and additionally port approaches.'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        #service_download.download_and_save_catalogue()
        #time.sleep(5)

        service_parse.import_catalogue_from_file(SNC_CATALOGUE_FILE)
        time.sleep(5)
        service_geojson.generate_geojson_and_save_db(SCALE_RANGE_ALL)
        time.sleep(5)
        service_geojson.generate_geojson_and_save_db_8XXX()

        self.stdout.write(self.style.SUCCESS('Successfully parsed - imported - geojson - portapp'))






