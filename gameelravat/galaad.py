from textwrap import dedent
from .area import Area


class Galaad(Area):

    def enter(self):
        super(Galaad, self).phrase()
        print(dedent('''
        Это Галаад. Здесь всем управляют женщины. Тебя
        встречает наместница со своей дочерью. Она готова
        помочь тебе армией в количестве 7 тысяч выносливых и сильных женщин,
        но взамен просит жениться на её дочери. Она достойная дочь наместницы -
        высокая, имеет крепкие руки и строгий характер. Согласишься?
        '''))

        answer = input('> ')

        if answer == 'да':
            print('Ты получаешь армию. удачи!')
            return 'halet'

        elif answer == 'нет':
            print(dedent('''
            Наместница Галаада в ярости. Она решает 
            рассказать обо всем нынешнему королю Эльравата и помочь ему!
            '''))
            return 'him'

        else:
            print('Так нельзя поступить!')
            return 'galaad'