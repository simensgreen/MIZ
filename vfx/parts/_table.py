from vfx.parts import DrawableSpring
from vfx.parts import DrawableCube
from vfx._drawable import Drawable
from tkinter import Canvas


class Table(Drawable):
    id = None

    def draw(self):
        self.id = self.canvas.create_line(
            self.coords[0], self.coords[1],
            self.coords[0], self.coords[3],
            self.coords[2], self.coords[3],
            self.coords[2], self.coords[1],
            tags=("table", self),
            **self.opts,
        )
        self.cube.draw()
        self.left_spring.draw()
        self.right_spring.draw()

    def update(self):
        x_max = self.right - self.cube.side / 2
        x_min = self.left + self.cube.side / 2
        cube_x = self.cube.pos[0]
        self.cube.pos = min(max(x_min, cube_x), x_max), self.cube.pos[1]
        self.cube.update()
        self.left_spring.right = self.cube.left
        self.left_spring.left = self.left
        self.left_spring.update()
        self.right_spring.left = self.cube.right
        self.right_spring.right = self.right
        self.right_spring.update()

    def delete(self):
        self.cube.delete()
        self.left_spring.delete()
        self.right_spring.delete()
        self.canvas.delete(self.id)
        self.id = None

    def __init__(self, coords, canvas: Canvas):
        self.opts = {'width': 3}
        self.coords = coords
        self.canvas = canvas
        self.cube = DrawableCube(self.coords[3] - self.coords[1])
        self.cube.canvas = canvas
        self.cube.pos = self.center
        self.left_spring = DrawableSpring(self.left, self.cube.left, 10, self.cube.side * .25)
        self.left_spring.canvas = canvas
        self.left_spring.pos = self.left_spring.pos[0], self.center[1]
        self.right_spring = DrawableSpring(self.cube.right, self.right, 10, self.cube.side * .25)
        self.right_spring.canvas = canvas
        self.right_spring.pos = self.right_spring.pos[0], self.center[1]

    @property
    def center(self):
        return (self.coords[2] + self.coords[0]) / 2, (self.coords[3] + self.coords[1]) / 2

    @property
    def left(self):
        return self.coords[0]

    @property
    def right(self):
        return self.coords[2]
