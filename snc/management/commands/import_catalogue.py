from django.core.management.base import BaseCommand, CommandError
import snc.service_parse as service_parse
from snc.const import *
import time


class Command(BaseCommand):

    help = 'Downloads and parses the latest snc catalogue from the UKHO website.'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        #service_download.download_and_save_catalogue()
        time.sleep(10)
        service_parse.import_catalogue_from_file(SNC_CATALOGUE_FILE)
        self.stdout.write(self.style.SUCCESS('Successfully downloaded and imported the latest snc catalogue'))





