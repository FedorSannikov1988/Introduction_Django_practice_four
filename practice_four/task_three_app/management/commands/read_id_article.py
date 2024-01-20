from task_three_app.models import Article
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read article by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID article')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')

        article = \
            Article.objects.filter(pk=pk).first()

        if article:
            text: str = str(article)
        else:
            text: str = 'Статьи с таким ID нет в базе данных'

        self.stdout.write(text)