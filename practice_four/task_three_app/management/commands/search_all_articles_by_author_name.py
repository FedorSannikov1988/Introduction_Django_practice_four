from task_three_app.models import Article, Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Search for all articles by the author by his name"

    def add_arguments(self, parser):
        parser.add_argument('name_author', type=str, help='Name author')
        parser.add_argument('order_grading', type=str, help='Order grading article')
        parser.add_argument('number_results', type=int, help='Number output results')

    def handle(self, *args, **kwargs):

        name_author: str = kwargs.get('name_author')
        order_grading: str = kwargs.get('order_grading')
        number_results: int = kwargs.get('number_results')

        author = \
            Author.objects.filter(name=name_author).first()

        if author:
            if order_grading == 'True':
                param_sort: str = 'date_publication'
            else:
                param_sort: str = '-date_publication'

            articles = \
                Article.objects.filter(author=author).order_by(param_sort).all()

            for article in articles[:number_results]:
                self.stdout.write(str(article))

        else:
            self.stdout.write(str(None))