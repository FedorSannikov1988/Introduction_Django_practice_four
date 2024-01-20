from datetime import date
from task_three_app.models import Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create fake author"

    def add_arguments(self, parser):
        parser.add_argument('number_fake_author', type=int, help='Number create fake author')

    def handle(self, *args, **kwargs):

        number_fake_author = kwargs.get('number_fake_author')

        for i in range(number_fake_author):
            fake_author = \
                Author(name=f'name_{i}',
                       surname=f'surname_{i}',
                       email=f'name_{i}_surname_{i}_@example.com',
                       biography=f'I am a great man...',
                       birthday=date.today())

            self.stdout.write(str(fake_author))

            fake_author.save()
