from django.core.management.base import BaseCommand, CommandError
import snc.service_download as service_download
from snc.const import *
import time


class Command(BaseCommand):

    help = 'Downloads the latest snc catalogue from the UKHO website.'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        #service_download.download_and_save_catalogue()
        time.sleep(10)
        service_download.download_catalogue(secrets.UKHO_U, secrets.UKHO_P)
        self.stdout.write(self.style.SUCCESS('Successfully downloaded the latest snc catalogue'))





