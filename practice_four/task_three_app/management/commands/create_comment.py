from django.core.management.base import BaseCommand
from task_three_app.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Create comment"

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=int, help='ID author article')
        parser.add_argument('article_id', type=int, help='ID article')
        parser.add_argument('comment', type=str, help='Comment')

    def handle(self, *args, **kwargs):

        comment: int = kwargs.get('comment')
        author_id: int = kwargs.get('author_id')
        article_id: int = kwargs.get('article_id')

        author = \
            Author.objects.filter(pk=author_id).first()

        article = \
            Article.objects.filter(pk=article_id).first()

        if author and article:
            comment_for_db = \
                Comment(author=author,
                        article=article,
                        comment=comment)
            comment_for_db.save()
            self.stdout.write(str(comment_for_db))
        else:
            self.stdout.write(str(None))
