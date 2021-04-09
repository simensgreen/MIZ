from src.spring import Spring
from vfx._drawable import Drawable


class DrawableSpring(Spring, Drawable):
    id = None

    def draw(self):
        self.id = self.canvas.create_line(self.add_pos(self.coords), tags=('spring', self))

    def delete(self):
        self.canvas.delete(self.id)
        self.id = None

    def update(self):
        self.canvas.coords(self.id, self.flatten(self.add_pos(self.coords)))
