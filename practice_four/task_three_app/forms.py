import datetime
from django import forms

from task_three_app.models import Author


class AddAuthor(forms.Form):

    name = forms.CharField(min_length=1,
                           max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
                               label='Имя пользователя'
    )

    surname = forms.CharField(min_length=1,
                              max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'Введите фамилию пользователя'}),
                                  label='Фамилия пользователя'
    )

    email = forms.EmailField(widget=forms.EmailInput(
                             attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}),
                             label='Email'
    )

    biography = forms.CharField(widget=forms.Textarea(
                                attrs={'class': 'form-control'}),
                                label='Биография'
    )

    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(
                               attrs={'class': 'form-control', 'type': 'date'})
    )


class AddArticle(forms.Form):

    title = forms.CharField(min_length=1,
                           max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
                               label='Название'
    )

    content = forms.CharField(widget=forms.Textarea(
                                attrs={'class': 'form-control'}),
                                label='Содержание'
    )

    date_publication = forms.DateField(initial=datetime.date.today,
                                       widget=forms.DateInput(
                                           attrs={'class': 'form-control', 'type': 'date'}),
                                           label='Дата публикации'
    )

    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    empty_label='Выберите автора',
                                    #to_field_name='name',
                                    widget=forms.Select(attrs={'class': 'form-control'}),
                                    label='Автор:'
    )

    category = forms.CharField(min_length=1,
                               max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
                                   label='Категория',
                                   required=True,
                                   error_messages= {
                                    'required': 'Пожалуйста, заполните поле "Категория".'
                                }
    )
