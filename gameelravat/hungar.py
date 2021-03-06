from textwrap import dedent
from .heir import Heir


class Hungar(Heir):

    def enter(self):
        super(Hungar, self).phrase()
        print(dedent('''
        Вот перед тобой главный наследник престола! Его рост не
        более полутора метров, одна нога короче другой на 10 см и
        нет правого глаза. Ты смотришь на это жалкое зрелище и 
        понимаешь, что он безобиден. Что ты выберешь:
        1. сохранить ему жизнь и оставить жить во дворце вместе с тобой.
        2. сохранить жизнь и отпраивть его в вечное заточение.
        3. убить, вырвав второй глаз.
        '''))

        answer = input('> ')

        if answer == '1':
            print(dedent('''
            Твоя доброта подвела тебя. Он берет корону и кидает тебе в 
            голову. Ты умираешь...Надо было быть умнее.
            '''))
            return 'death'

        elif answer == '2':
            print(dedent('''
           Ты выполняешь все свои обещания и счастливо правишь до того,
           пока не появляется скрывшийся сын Хунгара со своей армией.
            '''))
            return 'finished'

        elif answer == '3':
            print(dedent('''
            Тебя теперь все боятся. Это мало кого устраивает, тебя с трона
            свергает дочь наместницы Галлада. В королевстве устанавливается
            матриархат.
            '''))
            return 'death'

        else:
            print('Нужно выбрать цифру!')
            return 'hungar'