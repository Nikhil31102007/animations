from manim import *

class FullLorentzDerivation(Scene):
    def construct(self):

        # ------------------------------------------------
        # FRAME SETUP
        # ------------------------------------------------
        axes = Axes(
            x_range=[0,6],
            y_range=[0,4],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True},
        ).to_corner(DL)

        labels = axes.get_axis_labels("x","t")
        frameS = Text("Frame S").scale(0.6).next_to(axes,UP)

        self.play(Create(axes),Write(labels))
        self.play(Write(frameS))
        self.wait(2)

        axes_p = axes.copy().set_color(BLUE)
        labels_p = axes_p.get_axis_labels("x'","t'").set_color(BLUE)
        frameSp = Text("Frame S'").scale(0.6).set_color(BLUE).next_to(axes_p,UP)

        self.play(Create(axes_p),Write(labels_p),Write(frameSp))
        self.wait(2)

        velocity = MathTex("v").next_to(frameSp,RIGHT)
        self.play(Write(velocity))

        self.play(
            axes_p.animate.shift(RIGHT*1.6),
            labels_p.animate.shift(RIGHT*1.6),
            frameSp.animate.shift(RIGHT*1.6),
            velocity.animate.shift(RIGHT*1.6),
            run_time=4
        )
        self.wait(2)

        # ------------------------------------------------
        # EVENT WITH COORDINATES
        # ------------------------------------------------
        event = Dot(color=RED).move_to(axes.c2p(3,2))

        coordS = MathTex("(x,t)").next_to(event,UP)
        coordSp = MathTex("(x',t')").set_color(BLUE).next_to(coordS,UP)

        self.play(FadeIn(event))
        self.play(Write(coordS))
        self.play(Write(coordSp))
        self.wait(4)

        self.play(FadeOut(coordS),FadeOut(coordSp),FadeOut(event))

        # ------------------------------------------------
        # GENERAL LINEAR TRANSFORMATION
        # ------------------------------------------------
        general = VGroup(
            MathTex("x' = Ax + Bt"),
            MathTex("t' = Dx + Et")
        ).arrange(DOWN)

        title = Text("General Linear Transformation").to_edge(UP)

        self.play(Write(title))
        self.play(Write(general))
        self.wait(4)

        # ------------------------------------------------
        # RELATIVE MOTION CONDITION
        # ------------------------------------------------
        cond1 = MathTex("x = vt")
        cond2 = MathTex("x' = 0")

        cond = VGroup(cond1,cond2).arrange(DOWN).next_to(general,DOWN)

        self.play(Write(cond))
        self.wait(3)

        derive1 = MathTex("0 = A(vt) + Bt")
        derive2 = MathTex("0 = t(Av + B)")
        derive3 = MathTex("B = -Av")

        derivation = VGroup(derive1,derive2,derive3).arrange(DOWN).to_edge(DOWN)

        self.play(Write(derive1))
        self.wait(2)
        self.play(Transform(derive1,derive2))
        self.wait(2)
        self.play(Transform(derive1,derive3))
        self.wait(3)

        finalx = MathTex("x' = A(x - vt)").to_edge(DOWN)

        self.play(Transform(derive1,finalx))
        self.wait(4)

        self.play(
            FadeOut(cond),
            FadeOut(general),
            FadeOut(derive1),
            FadeOut(title)
        )

        # ------------------------------------------------
        # LIGHT POSTULATE
        # ------------------------------------------------
        light_title = Text("Light moves with speed c in all frames").scale(0.7).to_edge(UP)

        light1 = MathTex("x = ct")
        light2 = MathTex("x' = ct'")

        light = VGroup(light1,light2).arrange(DOWN)

        self.play(Write(light_title))
        self.play(Write(light))
        self.wait(3)

        # ------------------------------------------------
        # SUBSTITUTE INTO TRANSFORM
        # ------------------------------------------------
        step1 = MathTex("x' = A(ct - vt)")
        step2 = MathTex("x' = At(c - v)")
        step3 = MathTex("t' = t(Dc + E)")

        steps = VGroup(step1,step2,step3).arrange(DOWN).next_to(light,DOWN)

        self.play(Write(step1))
        self.wait(2)
        self.play(Transform(step1,step2))
        self.wait(2)
        self.play(Write(step3))
        self.wait(3)

        condlight = MathTex("x' = ct'").to_edge(DOWN)

        self.play(Write(condlight))
        self.wait(3)

        eq1 = MathTex("A(c-v) = c(Dc + E)")
        eq2 = MathTex("-A(c+v) = c(-Dc + E)")

        eqs = VGroup(eq1,eq2).arrange(DOWN)

        self.play(FadeOut(step1),FadeOut(step3))
        self.play(Write(eqs))
        self.wait(4)

        # ------------------------------------------------
        # SOLVE EQUATIONS
        # ------------------------------------------------
        solve1 = MathTex("-2Av = 2cE")
        solve2 = MathTex("E = -\\frac{Av}{c}")

        solve3 = MathTex("2Ac = 2cDc")
        solve4 = MathTex("D = \\frac{A}{c}")

        solving = VGroup(solve1,solve2,solve3,solve4).arrange(DOWN)

        self.play(Transform(eqs,solving))
        self.wait(5)

        self.play(FadeOut(eqs),FadeOut(light),FadeOut(condlight),FadeOut(light_title))

        # ------------------------------------------------
        # SYMMETRY STEP
        # ------------------------------------------------
        sym = Text("Symmetry between frames").to_edge(UP)

        gamma1 = MathTex("A = \\frac{1}{\\sqrt{1 - v^2/c^2}}")

        self.play(Write(sym))
        self.play(Write(gamma1))
        self.wait(5)

        # ------------------------------------------------
        # DEFINE GAMMA
        # ------------------------------------------------
        gamma = MathTex("\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}")

        gamma_title = Text("Lorentz Factor").to_edge(UP)

        self.play(FadeOut(sym),FadeOut(gamma1))
        self.play(Write(gamma_title))
        self.play(Write(gamma))
        self.wait(4)

        # ------------------------------------------------
        # FINAL TRANSFORMATIONS
        # ------------------------------------------------
        final = VGroup(
            MathTex("x' = \\gamma(x - vt)"),
            MathTex("t' = \\gamma\\left(t - \\frac{vx}{c^2}\\right)")
        ).arrange(DOWN)

        self.play(FadeOut(gamma),FadeOut(gamma_title))
        self.play(Write(final))
        self.wait(4)

        # ------------------------------------------------
        # SIGNIFICANCE OF GAMMA
        # ------------------------------------------------
        significance_title = Text("Where γ appears in Relativity").to_edge(UP)

        formulas = VGroup(
            MathTex("t' = \\gamma t"),
            MathTex("L = \\frac{L_0}{\\gamma}"),
            MathTex("E = \\gamma mc^2"),
            MathTex("p = \\gamma mv")
        ).arrange(DOWN)

        self.play(FadeOut(final))
        self.play(Write(significance_title))
        self.play(Write(formulas))
        self.wait(6)