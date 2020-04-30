from textwrap import dedent
from .heir import Heir

class Halet(Heir):

    def enter(self):
        super(Halet, self).phrase()
        print(dedent('''
        Ты договорился о тайной встрече с дочерью короля Халет.
        Она сообщает, что король скончался от болезни, и её брат
        готов занять перстол. Она любит брата Хунгара. И боится,
        что ты его убьешь. И предлагает за сохранение его жизни
        женитьбу на себе, обещает с ним договориться и всё объяснить.
        Согласишься?
        '''))

        answer = input('> ')

        if answer == 'да':
            print(dedent('''
            Ты проходишь с ней к брату. Но оказывается она тебя обманула.
            Хунгар хватает корону отца и кидает тебе в глаз.
            '''))
            return 'death'

        elif answer == 'нет':
            print(dedent('''
            Тебе уже понравилась дочь наместницы Галаада. Поэтому
            договориться не получилась. Идёшь напрямую к Хунгару.
            '''))
            return 'hungar'

        else:
            print('Так нельзя поступить!')
            return 'halet'