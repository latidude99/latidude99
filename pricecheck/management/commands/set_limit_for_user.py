from django.core.management.base import BaseCommand, CommandError
import pricecheck.commands as commands

class Command(BaseCommand):

    help = 'Sets max tracked products limit for predefined users'

    def add_arguments(self, parser):
        parser.add_argument('db', nargs='+')

    def handle(self, *args, **options):
        commands.set_limit_for_user('latidude99test@gmail.com', 50)
        cmmands.set_limit_for_user('latidude99@gmail.com', 50)
        self.stdout.write(self.style.SUCCESS('Successfully set new limit of 50 for latidude99 and latidude99test'))



