import linecache
import random
import string

from django.db import models
from players.models import Player


class Lobby(models.Model):
    lobby_id = models.CharField(
        'Id лобби',
        max_length=20
    )
    lobby_creater = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='creater',
        verbose_name='Создатель лобби',
    )
    used_words_player_one = models.CharField(
        'Указанные слова первого игрока',
        max_length=100,
        blank=True,
        default=""
    )
    lobby_player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='player',
        verbose_name='Второй игрок',
    )
    used_words_player_two = models.CharField(
        'Указанные слова второго игрока',
        max_length=100,
        blank=True,
        default=""
    )
    winner = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='winner',
        verbose_name='Победитель лобби',
    )
    win_word = models.CharField(
        'Загаданное слово',
        max_length=6
    )
    created_date = models.DateTimeField(
        'Дата создания лобби',
        null=True,
        blank=True
    )
    end_date = models.DateTimeField(
        'Дата победы',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Лобби игры'
        verbose_name_plural = 'Лобби игр'

    @staticmethod
    def create_lobby_id():
        while True:
            lobby_id = ''.join([random.choice(string.hexdigits)
                                for _ in range(20)])
            if Lobby.objects.filter(lobby_id=lobby_id):
                continue
            break
        return lobby_id

    @staticmethod
    def get_random_word(word_length):
        'Получаем случайное слово из выбранной длины'
        random_word = set(linecache.getline(
            'static/words/words.csv', word_length-3
        ).split(',')).pop()[:word_length]
        return random_word

    def __str__(self):
        return ('Лобби игрока ' +
                self.lobby_creater.username +
                ' с id: ' +
                self.lobby_id)
