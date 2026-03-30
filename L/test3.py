from manim import * 

class  test(Scene): 
    def construct(self):
        
        text= Tex("this nigga be straight up trash").to_edge(UL, buff=0.5)
        sq1= Square(side_length=1, fill_color= ORANGE, stroke_color = GREEN, fill_opacity= .9).shift(LEFT*3)
        tri = Triangle().scale(0.6).to_edge(DR).rotate(47*DEGREES)

        leaf=ImageMobject("assets/images/1n.png")
        blackman=ImageMobject("assets/images/surprised.png")
        self.play(blackman.animate.fade(1))

        blackman.to_edge(UR)

        leaf.scale(.3)

        self.play(Write(text))
        self.play(DrawBorderThenFill(sq1), run_time=2)
        self.play(Create(tri))
        self.play(FadeIn(leaf))
        self.play(blackman.animate.fade(0))

        self.wait()

        blackman.fade(0)
        self.play(text.animate.to_edge(UR), run_time=2)
        self.play(sq1.animate.scale(2), tri.animate.to_edge(DL), run_time=2)
        self.wait()