from task_three_app.models import Article
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read all article"

    def handle(self, *args, **kwargs):

        articles = Article.objects.all()

        for article in articles:
            self.stdout.write(str(article))
