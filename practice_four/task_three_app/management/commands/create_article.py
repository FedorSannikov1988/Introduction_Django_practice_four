from datetime import datetime
from task_three_app.models import Article, Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create article"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title article')
        parser.add_argument('content', type=str, help='Сontent article')
        parser.add_argument('date_publication', type=str, help='Date publication article')
        parser.add_argument('author_id', type=int, help='ID author article')
        parser.add_argument('category', type=str, help='Category article')

    def handle(self, *args, **kwargs):

        title: str = kwargs.get('title')
        content: str = kwargs.get('content')

        date_publication: str = kwargs.get("date_publication")
        datetime_obj = datetime.strptime(date_publication, "%Y-%m-%d")
        date_obj = datetime_obj.date()

        author_id: int = kwargs.get('author_id')
        category: str = kwargs.get('category')

        author = Author.objects.filter(pk=author_id).first()

        if author:
            article = Article(title=title,
                              content=content,
                              date_publication=date_obj,
                              author=author,
                              category=category)
            article.save()
            self.stdout.write(str(article))
        else:
            self.stdout.write(str(None))
