from manim import *
class tutorial(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        circle.set_fill(PINK,opacity=.5)
        self.play(Create(square))
        self.play(Transform(square,circle))
        self.wait()