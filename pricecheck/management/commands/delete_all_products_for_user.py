from django.core.management.base import BaseCommand, CommandError
import pricecheck.commands as commands

class Command(BaseCommand):

    help = 'Deletes all tracked products for predefined users'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        commands.delete_all_products_for_user('latidude99test@gmail.com')
        commands.delete_all_products_for_user('latidude99@gmail.com')
        self.stdout.write(self.style.SUCCESS('Successfully deleted tracked products for latidude99 and latidude99test'))



