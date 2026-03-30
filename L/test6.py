from manim import *

class test(Scene):
    def construct(self):
        
        text= MathTex("ln(2)")
        box = SurroundingRectangle(
            text, color=BLUE, fill_opacity= 0.4, fill_color= RED, buff= .5
        )
        text2= Tex("yes sirr").next_to(box, DOWN, buff=0.25)

        self.play(Create(VGroup(text,box, text2)))
        self.play(text.animate.shift(RIGHT*2),run_time=2)
        self.wait()