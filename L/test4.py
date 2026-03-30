from manim import *

class test(Scene):
    def construct(self): 
        
        sq=Square(side_length=4, fill_color=YELLOW, fill_opacity=.3)
        c1=Circle(radius=2, fill_color=RED, fill_opacity=1)

        ax=Axes()
        self.play(Create(ax))

        self.play(Transform(sq,c1),run_time=2)        