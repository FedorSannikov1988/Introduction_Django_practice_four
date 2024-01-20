from django.shortcuts import render, get_object_or_404
from task_three_app.models import Article, Author, Comment
from task_three_app.forms import AddAuthor, AddArticle, AddComment


def get_all_articles(request):

    articles = Article.objects.all()

    context = {
        "title": "Все статьи из базы данных",
        "articles": articles
    }

    return render(request, "get_all_articles.html", context)


def get_all_articles_author_name(request, author_name: str):

    author = Author.objects.filter(name=author_name).first()

    articles = None

    if author:

        articles = \
            Article.objects.filter(author=
                                   author).order_by('date_publication').all()

    context = {
        "title": "Все статьи автора",
        "author_name": author_name,
        "articles": articles
    }

    return render(request, "get_all_articles_author_name.html", context)


def see_article_by_id(request, id_article: int):

    article = get_object_or_404(Article, pk=id_article)

    if request.method == 'POST':

        form_add_comment = AddComment(request.POST)

        if form_add_comment.is_valid():

            author = form_add_comment.cleaned_data['author']
            comment = form_add_comment.cleaned_data['comment']

            comment_for_save_db = \
                Comment(author=author,
                        article=article,
                        comment=comment)
            comment_for_save_db.save()

    else:
        form_add_comment = AddComment()

    article.number_views += 1
    article.save()

    comments = \
        Comment.objects.filter(article=article).order_by('-date_change').all()

    context = {
        "article": article,
        "comments": comments,
        "form_add_comment": form_add_comment,
    }

    return render(request, "see_article_by_id.html", context)


def add_author_in_db(request):

    if request.method == 'POST':

        form = AddAuthor(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']

            author = \
                Author(name=name,
                       surname=surname,
                       email=email,
                       biography=biography,
                       birthday=birthday)

            author.save()

    else:
        form = AddAuthor()

    context = {
        "title": "Добавить автора в базу данных",
        "form": form
    }

    return render(request, "add_author_in_db.html", context)


def add_article_in_db(request):

    if request.method == 'POST':

        form = AddArticle(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            date_publication = form.cleaned_data['date_publication']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']

            article = Article(title=title,
                              content=content,
                              date_publication=date_publication,
                              author=author,
                              category=category)
            article.save()

    else:
        form = AddArticle()

    context = {
        "title": "Добавить статью в базу данных",
        "form": form
    }

    return render(request, "add_article_in_db.html", context)
