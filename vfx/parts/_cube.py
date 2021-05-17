from src.cube import Cube
from vfx._drawable import Drawable


class DrawableCube(Cube, Drawable):
    id = None
    __old = None
    freeze_y = True

    def draw(self):
        self.id = self.canvas.create_rectangle(self.add_pos(self.coords), fill='lightgrey', **self.opts, tags=('cube', self))
        self.canvas.tag_bind(self, '<Enter>', self.__cursor_to_arrow)
        self.canvas.tag_bind(self, '<Leave>', self.__cursor_to_normal)
        self.canvas.tag_bind(self, '<B1-Motion>', self.__l_motion)
        self.canvas.tag_bind(self, '<B1-ButtonRelease>', self.__stop_motion)

    def delete(self):
        self.canvas.delete(self.id)

    def update(self):
        self.canvas.coords(self.id, self.flatten(self.add_pos(self.coords)))

    def __cursor_to_arrow(self, event):
        self.canvas['cursor'] = 'sb_h_double_arrow'

    def __cursor_to_normal(self, event):
        self.canvas['cursor'] = ''

    def __l_motion(self, event):
        x, y = event.x, event.y
        if self.__old is None:
            self.__old = x, y
        else:
            dx = x - self.__old[0]
            dy = 0 if self.freeze_y else y - self.__old[1]
            self.pos = self.pos[0] + dx, self.pos[1] + dy
            self.__old = x, y

    def __stop_motion(self, event):
        self.__old = None

    @property
    def left(self):
        return self.add_pos(self.coords)[0][0]

    @property
    def right(self):
        return self.add_pos(self.coords)[1][0]
