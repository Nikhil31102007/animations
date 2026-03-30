from manim import *

class LorentzTransformationDemo(Scene):
    def construct(self):

        # ---------- Scene 1 : Two Frames ----------
        axes_S = Axes(
            x_range=[-5,5],
            y_range=[-3,3],
            axis_config={"include_tip": True},
        )

        labels_S = axes_S.get_axis_labels("x", "t")

        frame_label = Text("Frame S").scale(0.6).next_to(axes_S, UP)

        self.play(Create(axes_S), Write(labels_S))
        self.play(Write(frame_label))
        self.wait(2)

        # ---------- Create S' frame ----------
        axes_Sp = Axes(
            x_range=[-5,5],
            y_range=[-3,3],
            axis_config={"include_tip": True},
        ).set_color(BLUE)

        axes_Sp.move_to(axes_S)

        labels_Sp = axes_Sp.get_axis_labels("x'", "t'")
        labels_Sp.set_color(BLUE)

        frame_label_p = Text("Frame S'").scale(0.6).set_color(BLUE)
        frame_label_p.next_to(axes_Sp, UP)

        self.play(Create(axes_Sp), Write(labels_Sp), Write(frame_label_p))
        self.wait(2)

        # ---------- Scene 2 : Move S' along x ----------
        velocity_text = MathTex("v").next_to(frame_label_p, RIGHT)

        self.play(Write(velocity_text))
        self.play(axes_Sp.animate.shift(RIGHT*2),
                  labels_Sp.animate.shift(RIGHT*2),
                  frame_label_p.animate.shift(RIGHT*2),
                  velocity_text.animate.shift(RIGHT*2),
                  run_time=5)

        self.wait(2)

        # ---------- Scene 3 : Y and Z unchanged ----------
        yz_relation = MathTex("y' = y", ",", "z' = z").to_edge(UP)

        self.play(Write(yz_relation))
        self.wait(4)

        # ---------- Scene 4 : Event point ----------
        event = Dot(color=RED)
        event.move_to(axes_S.c2p(2,1))

        event_label = Text("Event").scale(0.5).next_to(event, UP)

        self.play(FadeIn(event), Write(event_label))
        self.wait(3)

        # ---------- Scene 5 : Galilean relation ----------
        galilean = MathTex("x' = x - vt").to_edge(DOWN)

        self.play(Write(galilean))
        self.wait(4)

        # ---------- Scene 6 : Lorentz correction ----------
        lorentz_x = MathTex("x' = \\gamma (x - vt)").to_edge(DOWN)

        self.play(Transform(galilean, lorentz_x))
        self.wait(6)

        # ---------- Scene 7 : Time transformation ----------
        time_eq = MathTex(
            "t' = \\gamma \\left(t - \\frac{vx}{c^2}\\right)"
        ).next_to(galilean, UP)

        self.play(Write(time_eq))
        self.wait(6)

        # ---------- Scene 8 : Lorentz factor ----------
        gamma_eq = MathTex(
            "\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}"
        ).scale(1.2)

        gamma_title = Text("Lorentz Factor").scale(0.7).to_edge(UP)

        self.play(FadeOut(yz_relation),
                  FadeOut(event),
                  FadeOut(event_label),
                  FadeOut(galilean),
                  FadeOut(time_eq))

        self.play(Write(gamma_title))
        self.play(Write(gamma_eq))
        self.wait(6)

        # ---------- Scene 9 : Final equations ----------
        final_eq = VGroup(
            MathTex("x' = \\gamma (x - vt)"),
            MathTex("t' = \\gamma \\left(t - \\frac{vx}{c^2}\\right)")
        ).arrange(DOWN)

        final_title = Text("Lorentz Transformations").to_edge(UP)

        self.play(FadeOut(gamma_eq), FadeOut(gamma_title))
        self.play(Write(final_title))
        self.play(Write(final_eq))

        self.wait(5)