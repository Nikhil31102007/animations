from manim import *
class LorentzConceptAnimation(Scene):
    def construct(self):

        # SCENE 1 : FRAME S

        axes = Axes(
            x_range=[0,6],
            y_range=[0,4],
            x_length=5,
            y_length=3,
            axis_config={"include_tip": True},
        ).to_corner(DL)

        labels = axes.get_axis_labels("x","t")
        frameS = Text("Frame S").scale(0.6).next_to(axes,UP)

        self.play(Create(axes),Write(labels),Write(frameS))
        self.wait(2)

        # SCENE 2 : FRAME S'

        axes_p = axes.copy().set_color(BLUE)
        labels_p = axes_p.get_axis_labels("x'","t'").set_color(BLUE)
        frameSp = Text("Frame S'").scale(0.6).set_color(BLUE).next_to(frameS,RIGHT)

        self.play(Create(axes_p))
        self.wait(2)

        velocity = MathTex("v").next_to(frameS,RIGHT)
        self.play(Write(velocity))

        self.play(
            axes_p.animate.shift(RIGHT*3.5),
            labels_p.animate.shift(RIGHT*3.5),
            frameSp.animate.shift(RIGHT*3.5),
            velocity.animate.shift(RIGHT*3.5),
            Write(labels_p),Write(frameSp),
            run_time=3
        )
        self.wait(2)

        # SCENE 3 : EVENT
        event = Dot(color=RED).move_to(axes.c2p(5,2))

        coordS = MathTex("(x,y,z,t)").next_to(event,UP)
        coordSp = MathTex("(x',y',z',t')").set_color(BLUE).next_to(coordS,UP)

        self.play(FadeIn(event),Write(coordS),Write(coordSp))
        self.wait(3)

        self.play(FadeOut(coordS),FadeOut(coordSp),FadeOut(event),FadeOut(velocity))

        # SCENE 4 : SPATIAL TRANSFORMATION
        eq_x = MathTex("x' = \\lambda (x - vt)").to_edge(RIGHT,buff=4)
        title_x = Text("Spatial Transformation").to_edge(UP)

        self.play(Write(title_x))
        self.play(Write(eq_x))
        self.wait(4)

        self.play(FadeOut(eq_x),FadeOut(title_x))

        # SCENE 5 : TIME TRANSFORMATION
        eq_t = MathTex("t' = \\lambda \\left(t - \\frac{vx}{c^2}\\right)").to_edge(RIGHT,buff=4)
        title_t = Text("Time Transformation").to_edge(UP)

        self.play(Write(title_t))
        self.play(Write(eq_t))
        self.wait(4)

        self.play(FadeOut(eq_t),FadeOut(title_t))

        # SCENE 6 : LORENTZ FACTOR
        lambda_title = Text("Lorentz Factor").to_edge(UP)
        lambd = MathTex("\\lambda = \\frac{1}{\\sqrt{1 - v^2/c^2}}").to_edge(RIGHT,buff=4)

        self.play(Write(lambda_title))
        self.play(Write(lambd))
        self.wait(4)

        self.play(FadeOut(lambd),FadeOut(lambda_title))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # SCENE 7 : SIGNIFICANCE
        title2 = Text("Where λ Appears in Relativity").to_edge(UP)

        formulas = VGroup(
            MathTex("t' = \\lambda t"),
            MathTex("L = \\frac{L_0}{\\lambda}"),
            MathTex("E = \\lambda mc^2"),
            MathTex("p = \\lambda mv")
        ).arrange(DOWN)
        what_are= Text("(Time Dilation)\n\n\n(Length Contraction)\n\n\n(Relativistic Energy)\n\n\n(Momentum)").next_to(formulas)
        what_are.scale(0.5)

        self.play(Write(title2))
        self.play(Write(formulas))

        self.wait(3)
        self.play(Write(what_are))
        self.wait(3)

        self.play(FadeOut(formulas),FadeOut(title2))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # END
        end = Text("Pranshu Rawat 25BTCS100\nNikhil Mishra 25BTCS088").scale(1.2)

        self.play(Write(end))
        self.wait(4)