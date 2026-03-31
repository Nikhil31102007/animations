from manim import *
import numpy as np

class PhotoelectricEffect(Scene):
    def construct(self):

        # ----------------------------
        # TITLE
        # ----------------------------
        title = Text("Photoelectric Effect").to_edge(UP)
        self.play(Write(title))

        # ----------------------------
        # METAL PLATE
        # ----------------------------
        plate = Rectangle(width=4, height=2, color=BLUE).shift(RIGHT*3)
        plate_label = Text("Metal", font_size=24).next_to(plate, DOWN)

        self.play(Create(plate), Write(plate_label))

        # ----------------------------
        # LOW FREQUENCY (NO EMISSION)
        # ----------------------------
        rays = VGroup(*[
            Arrow(LEFT*5 + UP*i, LEFT*1 + UP*i, color=RED, buff=0)
            for i in np.linspace(-1, 1, 5)
        ])

        low_label = Text("Low Frequency Light", font_size=24).next_to(title, DOWN)

        self.play(Create(rays), Write(low_label))
        self.play(rays.animate.shift(RIGHT*2), run_time=3)

        no_emission = Text("No Electrons Emitted", color=RED).to_edge(DOWN)
        self.play(Write(no_emission))
        self.wait(1.5)

        self.play(FadeOut(no_emission), FadeOut(rays), FadeOut(low_label))

        # ----------------------------
        # HIGH FREQUENCY (EMISSION)
        # ----------------------------
        rays_high = VGroup(*[
            Arrow(LEFT*5 + UP*i, LEFT*1 + UP*i, color=YELLOW, buff=0)
            for i in np.linspace(-1, 1, 5)
        ])

        high_label = Text("High Frequency Light", font_size=24).next_to(title, DOWN)

        self.play(Create(rays_high), Write(high_label))
        self.play(rays_high.animate.shift(RIGHT*2), run_time=3)

        # Controlled electrons (bounded region)
        electrons = VGroup(*[
            Dot(
                plate.get_left() + UP*np.random.uniform(-0.7, 0.7),
                radius=0.05,
                color=GREEN
            )
            for _ in range(6)
        ])

        self.play(FadeIn(electrons))

        animations = []
        for e in electrons:
            dx = np.random.uniform(1.5, 2.5)   # limited horizontal
            dy = np.random.uniform(-1, 1)      # limited vertical (avoid text)
            animations.append(
                e.animate.shift(LEFT*dx + UP*dy).set_run_time(2.5)
            )

        self.play(*animations)

        emission_label = Text("Electrons Emitted!", color=GREEN).to_edge(DOWN)
        self.play(Write(emission_label))
        self.wait(1.5)

        # REMOVE electrons before next phase
        self.play(
            FadeOut(emission_label),
            FadeOut(electrons),
            FadeOut(rays_high),
            FadeOut(high_label)
        )

        # ----------------------------
        # HIGH INTENSITY (MORE ELECTRONS)
        # ----------------------------
        rays_intense = VGroup(*[
            Arrow(LEFT*5 + UP*i, LEFT*1 + UP*i, color=YELLOW, buff=0)
            for i in np.linspace(-1.2, 1.2, 8)
        ])

        intensity_label = Text("Higher Intensity (More Photons)", font_size=24).next_to(title, DOWN)

        self.play(Create(rays_intense), Write(intensity_label))
        self.play(rays_intense.animate.shift(RIGHT*2), run_time=3)

        electrons_more = VGroup(*[
            Dot(
                plate.get_left() + UP*np.random.uniform(-0.7, 0.7),
                radius=0.05,
                color=GREEN
            )
            for _ in range(10)
        ])

        self.play(FadeIn(electrons_more))

        animations = []
        for e in electrons_more:
            dx = np.random.uniform(1.5, 3)
            dy = np.random.uniform(-1.2, 1.2)
            animations.append(
                e.animate.shift(LEFT*dx + UP*dy).set_run_time(2.5)
            )

        self.play(*animations)

        more_label = Text("More Electrons Emitted", color=GREEN).to_edge(DOWN)
        self.play(Write(more_label))
        self.wait(2)

        # Clean everything
        self.play(
            FadeOut(electrons_more),
            FadeOut(rays_intense),
            FadeOut(intensity_label),
            FadeOut(more_label)
        )

        # ----------------------------
        # FINAL SUMMARY (CLEAN SCREEN)
        # ----------------------------
        self.play(FadeOut(*self.mobjects))  # remove EVERYTHING on screen

        summary = VGroup(
            Text("Key Idea:", font_size=32),
            Text("Frequency → Energy of electrons", font_size=28),
            Text("Intensity → Number of electrons", font_size=28)
        ).arrange(DOWN)

        self.play(Write(summary))
        self.wait(3)