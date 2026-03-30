from manim import *

class test(Scene):
    def construct(self):
        
        sq=Circle(radius=1, fill_color=RED, fill_opacity=.8)
        r1=Rectangle(color=WHITE, height=3, width=4, fill_color=WHITE, fill_opacity=0.5).to_edge(UL)

        arrow = always_redraw(lambda:Line(start=r1.get_center(), end= sq.get_top(), buff=0.1).add_tip())

        self.play(Create(VGroup(sq,r1,arrow)), run_time=1)
        self.wait()

        self.play(r1.animate.to_edge(UR),sq.animate.scale(0.5), run_time=4)

        