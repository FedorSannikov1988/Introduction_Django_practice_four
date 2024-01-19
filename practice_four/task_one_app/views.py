import random
import logging
from .forms import ChooseGame
from django.shortcuts import render, redirect


logger = logging.getLogger(__name__)


def heads_or_tails(request, number_throws: int):

    coin: list = ["heads", "tails"]

    resalt: list[str] = []

    for _ in range(number_throws):
        resalt.append(random.choice(coin))

    logger.info(f'heads_or_tails page accessed, get message: {resalt}')

    context = {
        "title": "Игра орел или решка",
        "resalt": resalt,
        "number_throws": number_throws
    }

    return render(request, "heads_or_tails.html", context)


def playing_dice(request, number_throws: int):

    start: int = 1
    stop: int = 6

    resalt: list[int] = []

    for _ in range(number_throws):
        resalt.append(get_random_number(start=start, stop=stop))

    logger.info(f'playing_dice page accessed, get message: {str(resalt)}')

    context = {
        "title": "Игра брось игральный кубик",
        "resalt": resalt,
        "number_throws": number_throws
    }

    return render(request, "playing_dice.html", context)


def random_number(request, number_throws: int):

    start: int = 0
    stop: int = 100

    resalt: list[int] = []

    for _ in range(number_throws):
        resalt.append(get_random_number(start=start, stop=stop))

    logger.info(f'playing_dice page accessed, get message: {str(resalt)}')

    context = {
        "title": f"Игра получи случайное число от {start} до {stop}",
        "resalt": resalt,
        "number_throws": number_throws
    }

    return render(request, "random_number.html", context)


def get_random_number(start: int, stop: int) -> int:
    return random.randint(start, stop)


def form_for_choice_game(request):

    if request.method == 'POST':
        form = ChooseGame(request.POST)

        if form.is_valid():

            type_game = form.cleaned_data['type_game']
            number_of_attempts = form.cleaned_data['number_of_attempts']

            if type_game == 'coin':
                return redirect('heads_or_tails',
                                number_throws=number_of_attempts)

            elif type_game == 'bones':
                return redirect('playing_dice',
                                number_throws=number_of_attempts)

            else:
                return redirect('random_number',
                                number_throws=number_of_attempts)
    else:
        form = ChooseGame()

    context = {
        "title": "Выбор игры",
        "form": form
    }

    return render(request, "form_for_choice_game.html", context)
