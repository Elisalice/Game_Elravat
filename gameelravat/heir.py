from sys import exit
from textwrap import dedent


class Heir(object):

    def phrase(self): 
        print(dedent('''
        Ты решаешь обратится к наследникам, входишь в комнату и
        слышишь крик: "Что за нахальство заявляться ко мне"!
        '''))

    def enter(self): # эта функция будет переопределяться
        print('Здесь будет сцена с каждым наследником')
        exit(1)
