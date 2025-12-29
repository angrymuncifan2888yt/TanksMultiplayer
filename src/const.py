from enum import Enum, auto


class ScreenSize:
    WIDTH = 1200
    HEIGHT = 800
    
class EventType(Enum):
    CHANGE_SCENE = auto()