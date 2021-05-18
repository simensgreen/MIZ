from vfx.TkApp import TkApp
from vfx.parts import Table, Chart
import tkinter as tk
from tkinter import ttk


class App(TkApp):
    time = 0
    CANVAS_SIZE = 500, 500

    def _ready(self):
        self.root.title('MIZ')

        controls = tk.Frame(self.root)
        controls.pack(side=tk.RIGHT)

        self.deviation = ttk.Spinbox(controls, from_=-self.CANVAS_SIZE[0] / 2 * .7,
                                     to=self.CANVAS_SIZE[0] / 2 * .7, command=self.update_pos)
        self.cube_size = ttk.Spinbox(controls, from_=30, to=120, command=self.set_cube_size)
        self.spring_size = ttk.Spinbox(controls, from_=20, to=50, command=self.set_spring_size)
        self.spring_count = ttk.Spinbox(controls, from_=3, to=50, command=self.set_spring_turns)
        self.spring_count.pack()
        self.spring_size.pack()
        self.cube_size.pack()
        self.deviation.set(0)
        self.deviation.pack()
        ttk.Button(controls, text='Старт/стоп', command=self.toggle).pack()

        self.canvas = tk.Canvas(width=self.CANVAS_SIZE[0], height=self.CANVAS_SIZE[1])
        self.canvas.pack()
        self.table = Table((10, 50, 492, 150), self.canvas)
        self.table.draw()
        self.spring_size.set(self.table.left_spring.radius)
        self.cube_size.set(self.table.cube.side)
        self.spring_count.set(self.table.left_spring.turns)

        self.chart = Chart(self.canvas, self.CANVAS_SIZE[0], self.CANVAS_SIZE[1] - self.table.cube.side * 2)
        self.chart.pos = self.CANVAS_SIZE[0] / 2, self.table.cube.side * 2
        self.chart.draw()
        self.fps_on_top = True

    def set_spring_turns(self):
        self.table.left_spring.turns = int(self.spring_count.get())
        self.table.right_spring.turns = int(self.spring_count.get())

    def set_spring_size(self):
        size = float(self.spring_size.get())
        self.table.right_spring.radius = size
        self.table.left_spring.radius = size

    def set_cube_size(self):
        self.table.cube.side = float(self.cube_size.get())

    def toggle(self):
        self._phys_flag = not self._phys_flag

    def update_pos(self):
        self.table.cube.pos = float(self.deviation.get()) + self.CANVAS_SIZE[0] / 2, self.table.cube.pos[1]
        self.table.update()

    def _physics_process(self, delta):
        self.table.update()
        self.deviation.set(str(self.table.cube.pos[0] - self.CANVAS_SIZE[0] / 2))
        self.chart.add_value(self.table.cube.pos[0] - self.CANVAS_SIZE[0] / 2, delta)
        self.time += delta
        x, y = self.table.cube.pos
        a = self.CANVAS_SIZE[0] / 2
        omega = 1
        t = self.time / 10
        # self.table.cube.pos = a * math.exp(-beta * t) * math.cos(omega * t) + self.CANVAS_SIZE[0] / 2, y
        self.chart.update()


if __name__ == '__main__':
    app = App()
    app.run()
