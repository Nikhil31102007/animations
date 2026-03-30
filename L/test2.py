from manim import *

class test(Scene):
    # def construct(self):

    #     sq=Square(
    #         side_length=5, stroke_color = GREEN, fill_color=BLUE, fill_opacity=0.89
    #         )
    #     self.play(Create(sq),run_time=8)
    #     self.wait() 
    def construct(self):
        rect1=RoundedRectangle(corner_radius=0.8,height=4,width=1)
        rect2=Rectangle(stroke_color= YELLOW,fill_opacity=.5,height=2, width= 7, fill_color=YELLOW)

        rect_g = Group(rect1, rect2).arrange(buff=1)
        self.play(Create(rect2), run_time=3)
        
