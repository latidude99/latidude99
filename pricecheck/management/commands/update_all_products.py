from django.core.management.base import BaseCommand, CommandError
import pricecheck.commands as commands

class Command(BaseCommand):

    help = 'Updates prices for all tracked products'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        commands.update_all_products()
        self.stdout.write(self.style.SUCCESS('Successfully downloaded json data and updated owid db'))



