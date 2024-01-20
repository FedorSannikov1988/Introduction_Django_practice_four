from task_three_app.models import Comment, Article
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Search for all comments by article title"

    def add_arguments(self, parser):
        parser.add_argument('title_article', type=str, help='Title article')
        parser.add_argument('order_grading', type=str, help='Order grading comments')
        parser.add_argument('number_results', type=int, help='Number output results')

    def handle(self, *args, **kwargs):

        title_article: str = kwargs.get('title_article')
        order_grading: str = kwargs.get('order_grading')
        number_results: int = kwargs.get('number_results')

        article = \
            Article.objects.filter(title=title_article).first()

        if article:

            if order_grading == 'True':
                param_sort: str = 'date_creation'
            else:
                param_sort: str = '-date_creation'

            comments = \
                Comment.objects.filter(article=
                                       article).order_by(param_sort).all()

            if comments:
                for comment in comments[:number_results]:
                    self.stdout.write(str(comment))
            else:
                self.stdout.write(str(None))
        else:
            self.stdout.write(str(None))