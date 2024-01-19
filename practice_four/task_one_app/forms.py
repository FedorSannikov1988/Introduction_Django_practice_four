from django import forms


class ChooseGame(forms.Form):

    GAME_CHOICES = [
        ('coin', 'Монета: орел или решка'),
        ('bones', 'Кости от 1 до 6'),
        ('numbers', 'Числа от 1 до 100'),
    ]

    type_game = forms.ChoiceField(choices=GAME_CHOICES)
    number_of_attempts = forms.IntegerField(min_value=1, max_value=64)
