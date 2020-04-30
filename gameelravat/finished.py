from .area import Area

class Finished(Area):

    def enter(self):
        print('Достойный человек достоин трона!')
        return 'finished'