from .spring import Spring

class Table:
    __left_spring = None
    __right_spring = None
    __cube = None

    def __init__(self):
        pass

    @property
    def left_spring(self):
        return self.__left_spring

    @left_spring.setter
    def left_spring(self, new_value):
        self.__left_spring = Spring