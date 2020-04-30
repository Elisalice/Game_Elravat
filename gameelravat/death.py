from sys import exit
from random import randint
from .area import Area

class Death(Area):

    quips = [
        'Ты погиб. Как это печально',
        'Твоя мать будет грустить по тебе... надо было быть умнее.',
        'Надо же было быть таким придурком.',
        'Нормально делай, нормально будет.',
        'Бог дал, Бог взял...',
        'Даже мой маленький щенок соображает лучше!',
        'Когда ж ты повзрослешьь, как говорил твой папа?'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
