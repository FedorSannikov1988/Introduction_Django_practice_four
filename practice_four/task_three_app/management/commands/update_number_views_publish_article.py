from task_three_app.models import Article
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update number views and publish status in article"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('number_views', type=int, help='Number views article')
        parser.add_argument('publish', type=bool, help='Publish article')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')
        publish: bool = kwargs.get('publish')
        number_views: int = kwargs.get('number_views')

        article = \
            Article.objects.filter(pk=pk).first()

        if article:
            article.publish = publish
            article.number_views = number_views
            article.save()

        self.stdout.write(f'{article}')
