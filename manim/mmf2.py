from manim import *
import numpy as np

class MichelsonMorley(Scene):
    def construct(self):

        # ------------------------------------------------
        # Scene 1 — Ether Hypothesis
        # ------------------------------------------------

        title = Text("The Michelson–Morley Experiment")
        subtitle = Text("Testing the 'Ether Wind' Hypothesis").scale(0.6)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        ether_label = Text("Ether Wind").to_edge(UP)

        arrows = VGroup()
        for y in range(-3, 3):
            arrows.add(Arrow(LEFT*6 + UP*y, RIGHT*6 + UP*y, buff=0))

        self.play(Write(ether_label))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(arrows), FadeOut(ether_label))


        # ------------------------------------------------
        # Scene 2 — Apparatus Setup
        # ------------------------------------------------

        center = np.array([0, -2, 0])
        L = 3

        splitter = Square(0.3).rotate(PI/4).move_to(center)
        
        arm_right = Line(center, center + RIGHT*L)
        arm_up = Line(center, center + UP*L)

        mirror_right = Square(0.3).move_to(arm_right.get_end())
        mirror_up = Square(0.3).move_to(arm_up.get_end())

        source = Dot(center + LEFT*2)
        source_label = Text("Light Source").scale(0.45).next_to(source, DOWN)

        apparatus = VGroup(
            splitter, arm_right, arm_up,
            mirror_right, mirror_up,
            source_label
        )

        self.play(Create(apparatus))
        self.wait(2)


        # ------------------------------------------------
        # Scene 3 — Wave Propagation (REPLACED BEAMS)
        # ------------------------------------------------

        t_tracker = ValueTracker(0)

        A = 0.15
        k = 8

        def wave(x, t):
            return A * np.sin(k * (x - t))

        incoming_wave = always_redraw(lambda:
            ParametricFunction(
                lambda x: np.array([
                    x,
                    wave(x, t_tracker.get_value()),
                    0
                ]),
                t_range=[-L, min(0, -L + t_tracker.get_value())],
                color=YELLOW,
                stroke_opacity=0.7
            ).shift(center)
        )

        wave_right = always_redraw(lambda:
            ParametricFunction(
                lambda x: np.array([
                    x,
                    wave(x, t_tracker.get_value()),
                    0
                ]),
                t_range=[0, min(L, max(0, t_tracker.get_value() - 2))],
                color=BLUE,
                stroke_opacity=0.8
            ).shift(center)
        )

        wave_up = always_redraw(lambda:
            ParametricFunction(
                lambda y: np.array([
                    -wave(y, t_tracker.get_value()),
                    y,
                    0
                ]),
                t_range=[0, min(L, max(0, t_tracker.get_value() - 3))],
                color=GREEN,
                stroke_opacity=0.8
            ).shift(center)
        )

        self.add(incoming_wave)
        self.play(t_tracker.animate.set_value(4), run_time=4, rate_func=linear)

        self.add(wave_right, wave_up)
        self.play(t_tracker.animate.set_value(8), run_time=4, rate_func=linear)

        self.wait(2)


        # ------------------------------------------------
        # Scene 4 — Expected Fringe Shift
        # ------------------------------------------------

        prediction = Text("If ether exists → Fringe shift expected").scale(0.6)
        prediction.to_edge(DOWN)

        self.play(Write(prediction))
        self.wait(2)
        self.play(FadeOut(prediction))


        # ------------------------------------------------
        # Scene 5 — Rotate Apparatus (FIXED)
        # ------------------------------------------------

        rotate_text = Text("Rotate the apparatus").scale(0.6)
        rotate_text.to_edge(UP)

        self.play(Write(rotate_text))

        # dim waves (not remove)
        self.play(
            incoming_wave.animate.set_stroke(opacity=0.3),
            wave_right.animate.set_stroke(opacity=0.3),
            wave_up.animate.set_stroke(opacity=0.3),
            run_time=1
        )

        # rotate about splitter (correct pivot)
        self.play(
            Rotate(apparatus, angle=PI/2, about_point=splitter.get_center()),
            run_time=4,
            rate_func=smooth
        )

        self.wait(2)
        self.play(FadeOut(rotate_text))


        # ------------------------------------------------
        # Scene 6 — Null Result
        # ------------------------------------------------

        result = Text("No fringe shift detected").scale(0.8)
        conclusion = Text("No ether detected").scale(0.8)

        self.play(Write(result))
        self.wait(2)
        self.play(Transform(result, conclusion))
        self.wait(2)

        self.play(
            FadeOut(result),
            FadeOut(apparatus),
            FadeOut(incoming_wave),
            FadeOut(wave_right),
            FadeOut(wave_up)
        )


        # ------------------------------------------------
        # Scene 7 — Impact
        # ------------------------------------------------

        final = Text("Speed of light is the same in all directions.")
        final.scale(0.7)

        self.play(Write(final))
        self.wait(3)