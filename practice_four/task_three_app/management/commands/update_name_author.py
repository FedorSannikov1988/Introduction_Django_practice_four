from task_three_app.models import Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update author name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('name', type=str, help='Author name')

    def handle(self, *args, **kwargs):

        pk = kwargs.get('pk')
        name = kwargs.get('name')
        author = \
            Author.objects.filter(pk=pk).first()
        if author:
            author.name = name
            author.save()
        self.stdout.write(f'{author}')
