from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Author(' \
               f'name:{self.name}, ' \
               f'surname: {self.surname}, ' \
               f'email: {self.email}, ' \
               f'birthday: {self.birthday}' \
               f')'


    def get_name_and_surname(self):
        name = self.name
        surname = self.surname
        return f'{name} {surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_publication = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    number_views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'Article(' \
               f'title:{self.title}, ' \
               f'date_publication:{self.date_publication}, ' \
               f'author:{self.author}, ' \
               f'category: {self.category}' \
               f'number views: {self.number_views}' \
               f'publish: {self.publish}' \
               f')'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment(' \
               f'author:{self.author}, ' \
               f'article:{self.article}, ' \
               f'date creation: {self.date_creation}, ' \
               f'date change: {self.date_change}' \
               f')'
