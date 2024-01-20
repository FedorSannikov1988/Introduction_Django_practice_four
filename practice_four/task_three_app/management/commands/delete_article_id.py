from task_three_app.models import Article
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete article."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):

        pk = kwargs.get('pk')
        article = \
            Article.objects.filter(pk=pk).first()
        if article:
            article.delete()
        self.stdout.write(f'{article}')
