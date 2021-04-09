from vfx.TkApp import TkApp
from vfx.parts import DrawableSpring
import tkinter as tk
import time
import math


class App(TkApp):
    def _ready(self):
        self.canvas = tk.Canvas(width=500, height=500)
        self.canvas.pack()
        self.spring = DrawableSpring(200, 300, 10, 30)
        self.spring.canvas = self.canvas
        self.spring.draw()
        self.spring.pos = 0, 200

    def _physics_process(self, delta):
        self.spring.pos = 0, (math.sin(time.time()) + 1) / 2 * 250
        self.spring.left = (math.cos(time.time()) + 1) / 2 * 250
        self.spring.right = (math.sin(time.time()) + 1) / 2 * 250 + 250


if __name__ == '__main__':
    app = App()
    app.run()
