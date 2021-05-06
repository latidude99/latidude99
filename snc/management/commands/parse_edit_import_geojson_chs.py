from django.core.management.base import BaseCommand, CommandError

import snc.service_geojson_chs as service_geojson_chs
import snc.service_download_chs as service_download_chs
from snc.const import *
import time


class Command(BaseCommand):

    help = 'Parses and imports the chs geojson data from data folder to db.'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        service_download_chs.download_catalogue()
        time.sleep(5)
        service_geojson_chs.parse_edit_import_to_db_geojson_chs(CHS_GEOJSON_FILE)

        self.stdout.write(self.style.SUCCESS('Successfully parsed - imported - geojson chs'))






