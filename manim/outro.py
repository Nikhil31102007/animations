from manim import *

class Outro(Scene):
    def construct(self):
        # ----------------------------
        # MAIN CLOSING THOUGHT
        # ----------------------------
        text1 = Text("From certainty to probability...").scale(0.8)
        text2 = Text("From particles to waves...").scale(0.8)
        text3 = Text("Physics reshaped reality itself.").scale(0.8)

        group = VGroup(text1, text2, text3).arrange(DOWN, buff=0.6)

        self.play(Write(text1))
        self.wait(1)

        self.play(Write(text2))
        self.wait(1)

        self.play(Write(text3))
        self.wait(2)

        self.play(FadeOut(group))

        # ----------------------------
        # TECH STACK
        # ----------------------------
        tech_title = Text("Built Using", font_size=36)

        tech_list = VGroup(
            Text("Python", font_size=28),
            Text("Manim (Mathematical Animation Engine)", font_size=28),
            Text("NumPy (Numerical Computation)", font_size=28),
            Text("LaTeX (Mathematical Typesetting)", font_size=28)
        ).arrange(DOWN, buff=0.4)

        tech_group = VGroup(tech_title, tech_list).arrange(DOWN, buff=0.6)

        self.play(FadeIn(tech_group, shift=UP))
        self.wait(2)

        self.play(FadeOut(tech_group))

        # ----------------------------
        # FINAL CREDITS
        # ----------------------------
        credit_title = Text("Project by PRANSHU RAWAT, NIKHIL MISHRA", font_size=36)

        name1 = Text("Name 1 (Roll No: 25BTCS100)", font_size=28)
        name2 = Text("Name 2 (Roll No: 25BTCS088)", font_size=28)

        names = VGroup(name1, name2).arrange(DOWN, buff=0.4)
        group2 = VGroup(credit_title, names).arrange(DOWN, buff=0.6)

        self.play(FadeIn(group2))
        self.wait(2)

        self.play(FadeOut(group2))
