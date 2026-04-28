from manim import *
import numpy as np

class PolishedDiffraction(Scene):
    def construct(self):

        # -----------------------------------
        # AXES (for later graph, positioned early)
        # -----------------------------------
        graph_axes = Axes(
            x_range=[0, 4],
            y_range=[0, 1.5],
            x_length=3,
            y_length=2,
        ).to_corner(DR).shift(LEFT*0.5 + UP*0.5)

        # -----------------------------------
        # SCENE 1 — DIRECTED INCIDENT WAVES
        # -----------------------------------
        waves = VGroup()

        y_positions = np.linspace(-2, 2, 7)

        for y in y_positions:
            arrow = Arrow(
                start=[-7, y, 0],
                end=[-2, y, 0],
                buff=0,
                stroke_width=2
            )
            waves.add(arrow)

        text1 = Text("Incident Plane Wave").scale(0.5).to_edge(UP)

        self.play(LaggedStart(*[GrowArrow(w) for w in waves], lag_ratio=0.1))
        self.play(Write(text1))
        self.wait(2)

        # -----------------------------------
        # SCENE 2 — CLEAR SLIT
        # -----------------------------------
        top_barrier = Line([-2, 4, 0], [-2, 1, 0], color=WHITE)
        bottom_barrier = Line([-2, -1, 0], [-2, -4, 0], color=WHITE)

        slit_edges = VGroup(
            Line([-2, 1, 0], [-2, 0.8, 0], color=GREY),
            Line([-2, -1, 0], [-2, -0.8, 0], color=GREY),
        )

        text2 = Text("Wave passes through a narrow slit").scale(0.5).to_edge(UP)

        self.play(Create(top_barrier), Create(bottom_barrier))
        self.play(FadeTransform(text1, text2))
        self.wait(2)

        # Dim blocked waves
        self.play(waves.animate.set_opacity(0.2))

        # -----------------------------------
        # SCENE 3 — WAVELETS (HUYGENS)
        # -----------------------------------
        sources = VGroup()

        for y in np.linspace(-1, 1, 5):
            dot = Dot(point=[-2, y, 0], color=YELLOW)
            sources.add(dot)

        text3 = Text("Each point emits wavelets").scale(0.5).to_edge(UP)

        self.play(FadeTransform(text2, text3), FadeIn(sources))

        # Radius tracker for expansion
        r = ValueTracker(0.1)

        def make_wavelet(center):
            # Forward semicircle
            front = Arc(
                radius=r.get_value(),
                start_angle=-PI/2,
                angle=PI,
                arc_center=center,
                color=BLUE
            )

            # Back dotted semicircle
            back = DashedVMobject(
                Arc(
                    radius=r.get_value(),
                    start_angle=PI/2,
                    angle=PI,
                    arc_center=center,
                ),
                num_dashes=20
            )

            return VGroup(front, back)

        wavelets = always_redraw(
            lambda: VGroup(*[make_wavelet(s.get_center()) for s in sources])
        )

        self.play(Create(wavelets))
        self.play(r.animate.set_value(3), run_time=4, rate_func=linear)
        self.wait(1)

        # -----------------------------------
        # SCENE 4 — INTERFERENCE REGION
        # -----------------------------------
        text4 = Text("Interference creates diffraction").scale(0.5).to_edge(UP)

        self.play(FadeTransform(text3, text4))
        self.wait(2)

        # -----------------------------------
        # SCENE 5 — SCREEN + INTENSITY GRAPH
        # -----------------------------------
        screen = Line([5, -3, 0], [5, 3, 0], color=GREEN)

        self.play(Create(screen))

        # Intensity curve (sinc^2)
        intensity_curve = graph_axes.plot(
            lambda x: (np.sin(2*x)/(2*x))**2 if x != 0 else 1,
        )

        text5 = Text("Observed intensity pattern").scale(0.5).to_edge(UP)

        self.play(FadeTransform(text4, text5))
        self.play(Create(graph_axes), Create(intensity_curve))
        self.wait(3)

        # -----------------------------------
        # SCENE 6 — SLIT WIDTH EFFECT
        # -----------------------------------
        text6 = Text("Narrow slit → wider spread").scale(0.5).to_edge(UP)

        self.play(FadeTransform(text5, text6))

        # Animate slit narrowing
        self.play(
            top_barrier.animate.shift(DOWN*0.5),
            bottom_barrier.animate.shift(UP*0.5),
            run_time=2
        )

        self.wait(2)

        # -----------------------------------
        # END
        # -----------------------------------
        self.wait()