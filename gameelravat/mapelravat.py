from .urband import Urband
from .galaad import Galaad
from .him import Him
from .halet import Halet
from .hungar import Hungar
from .death import Death
from .finished import Finished


class Map(object):

    scenes = {
        'urband': Urband(),
        'galaad': Galaad(),
        'him': Him(),
        'halet': Halet(),
        'hungar': Hungar(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
