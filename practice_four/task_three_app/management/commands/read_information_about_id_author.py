from task_three_app.models import Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read information about author by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID author')

    def handle(self, *args, **kwargs):

        # pk: int = kwargs['pk']
        pk: int = kwargs.get('pk')

        # author = Author.objects.get(pk=pk)
        author = Author.objects.filter(pk=pk).first()

        if author:
            text: str = str(author)
        else:
            text: str = 'Автора с таким ID нет в базе данных'

        self.stdout.write(text)