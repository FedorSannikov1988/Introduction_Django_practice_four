from task_three_app.models import Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read information about all author"

    def handle(self, *args, **kwargs):

        authors = Author.objects.all()

        for author in authors:
            self.stdout.write(str(author))
