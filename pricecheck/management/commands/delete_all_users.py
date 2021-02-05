from django.core.management.base import BaseCommand, CommandError
import pricecheck.commands as commands

class Command(BaseCommand):

    help = 'Deletes all users'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        commands.delete_all_users()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users'))



