from manim import *

class LorentzDerivation(Scene):
    def construct(self):

        # ---------- SCENE 1 : FIRST QUADRANT FRAME S ----------
        axes = Axes(
            x_range=[0,5],
            y_range=[0,4],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True},
        ).to_corner(DL)

        labels = axes.get_axis_labels("x", "t")

        frame_S = Text("Frame S").scale(0.6).next_to(axes, UP)

        self.play(Create(axes), Write(labels))
        self.play(Write(frame_S))
        self.wait(2)


        # ---------- SCENE 2 : INTRODUCE FRAME S' ----------
        axes_p = axes.copy().set_color(BLUE)
        labels_p = axes_p.get_axis_labels("x'", "t'").set_color(BLUE)

        frame_Sp = Text("Frame S'").scale(0.6).set_color(BLUE)
        frame_Sp.next_to(axes_p, UP)

        self.play(Create(axes_p), Write(labels_p), Write(frame_Sp))
        self.wait(2)


        # ---------- SCENE 3 : MOTION ALONG X ----------
        velocity = MathTex("v").next_to(frame_Sp, RIGHT)

        self.play(Write(velocity))
        self.play(
            axes_p.animate.shift(RIGHT*1.8),
            labels_p.animate.shift(RIGHT*1.8),
            frame_Sp.animate.shift(RIGHT*1.8),
            velocity.animate.shift(RIGHT*1.8),
            run_time=4
        )
        self.wait(2)


        # ---------- SCENE 4 : Y AND Z INVARIANCE ----------
        yz = MathTex("y' = y", ",", "z' = z").to_edge(UP)

        self.play(Write(yz))
        self.wait(3)

        self.play(FadeOut(yz))


        # ---------- SCENE 5 : EVENT ----------
        event = Dot(color=RED).move_to(axes.c2p(3,2))
        event_label = Text("Event").scale(0.5).next_to(event, UP)

        self.play(FadeIn(event), Write(event_label))
        self.wait(2)


        # ---------- SCENE 6 : GALILEAN STEP ----------
        step1 = MathTex("x' = x - vt").to_edge(DOWN)

        self.play(Write(step1))
        self.wait(3)


        # ---------- STEP 2 : RELATIVITY CORRECTION ----------
        step2 = MathTex("x' = \\gamma(x - vt)").to_edge(DOWN)

        self.play(Transform(step1, step2))
        self.wait(4)


        # ---------- CLEAN ----------
        self.play(FadeOut(event), FadeOut(event_label))


        # ---------- SCENE 7 : TIME RELATION ----------
        time_step = MathTex(
            "t' = \\gamma\\left(t - \\frac{vx}{c^2}\\right)"
        ).next_to(step1, UP)

        self.play(Write(time_step))
        self.wait(5)


        # ---------- SCENE 8 : CLEAR SCREEN ----------
        self.play(
            FadeOut(step1),
            FadeOut(time_step),
            FadeOut(axes),
            FadeOut(axes_p),
            FadeOut(labels),
            FadeOut(labels_p),
            FadeOut(frame_S),
            FadeOut(frame_Sp),
            FadeOut(velocity)
        )


        # ---------- SCENE 9 : DERIVE GAMMA ----------
        gamma_title = Text("Lorentz Factor").to_edge(UP)

        gamma_step1 = MathTex(
            "\\gamma = ?"
        )

        gamma_step2 = MathTex(
            "\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}"
        )

        self.play(Write(gamma_title))
        self.play(Write(gamma_step1))
        self.wait(3)

        self.play(Transform(gamma_step1, gamma_step2))
        self.wait(5)


        # ---------- SCENE 10 : FINAL RESULT ----------
        final_eq = VGroup(
            MathTex("x' = \\gamma(x - vt)"),
            MathTex("t' = \\gamma\\left(t - \\frac{vx}{c^2}\\right)")
        ).arrange(DOWN)

        final_title = Text("Lorentz Transformations").to_edge(UP)

        self.play(
            FadeOut(gamma_step1),
            FadeOut(gamma_title)
        )

        self.play(Write(final_title))
        self.play(Write(final_eq))
        self.wait(6)