from manim import *

class Intro(Scene):
    def construct(self):
        # Title
        title = Text("Physics").scale(0.9)
        subtitle = Text("A Visual Exploration", font_size=32).next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP*0.3))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )

        # Credits
        credit_title = Text("Created by PRANSHU RAWAT, NIKHIL MISHRA", font_size=36)

        name1 = Text("Name 1 (Roll No: 25BTCS100)", font_size=28)
        name2 = Text("Name 2 (Roll No: 25BTCS088)", font_size=28)

        names = VGroup(name1, name2).arrange(DOWN, buff=0.4)

        group = VGroup(credit_title, names).arrange(DOWN, buff=0.6)

        self.play(FadeIn(group, shift=UP))
        self.wait(2)

        self.play(FadeOut(group))