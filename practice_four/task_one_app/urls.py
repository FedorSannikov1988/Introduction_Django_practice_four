from django.urls import path
from .views import heads_or_tails, playing_dice, random_number, form_for_choice_game


urlpatterns = [
    path('heads_or_tails/<int:number_throws>/', heads_or_tails, name='heads_or_tails'),
    path('playing_dice/<int:number_throws>/', playing_dice, name='playing_dice'),
    path('random_number/<int:number_throws>/', random_number, name='random_number'),
    path('form_for_choice_game', form_for_choice_game, name='form_for_choice_game'),
]
