from tkinter import Canvas


class Drawable:
    opts = {}
    canvas: Canvas = None
    __pos = 0, 0

    def draw(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, new_value):
        self.__pos = new_value

    def add_pos(self, coords):
        return [(x + self.__pos[0], y + self.__pos[1]) for x, y in coords]

    @staticmethod
    def flatten(sequence):
        out = ()
        for item in sequence:
            if isinstance(item, (tuple, list)):
                out = out + Drawable.flatten(item)
            elif item is not None:
                out = out + (item,)
        return out
