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
        # LOW FREQUENCY LIGHT (NO EMISSION)
        # ----------------------------
        rays = VGroup(*[
            Arrow(LEFT*5 + UP*i, LEFT*1 + UP*i, color=RED, buff=0)
            for i in np.linspace(-1, 1, 5)
        ])

        low_freq_label = Text("Low Frequency Light", font_size=24).to_edge(LEFT)

        self.play(Create(rays), Write(low_freq_label))
        self.play(rays.animate.shift(RIGHT*2), run_time=2)

        no_emission = Text("No Electrons Emitted", color=RED).to_edge(DOWN)
        self.play(Write(no_emission))
        self.wait(1.5)

        self.play(FadeOut(no_emission), FadeOut(rays), FadeOut(low_freq_label))

        # ----------------------------
        # HIGH FREQUENCY LIGHT (EMISSION)
        # ----------------------------
        rays_high = VGroup(*[
            Arrow(LEFT*5 + UP*i, LEFT*1 + UP*i, color=YELLOW, buff=0)
            for i in np.linspace(-1, 1, 5)
        ])

        high_freq_label = Text("High Frequency Light", font_size=24).to_edge(LEFT)

        self.play(Create(rays_high), Write(high_freq_label))
        self.play(rays_high.animate.shift(RIGHT*2), run_time=2)

        # Electrons emitted
        electrons = VGroup(*[
            Dot(plate.get_left() + UP*np.random.uniform(-0.8, 0.8), color=GREEN)
            for _ in range(5)
        ])

        self.play(FadeIn(electrons))

        self.play(*[
            e.animate.shift(LEFT*np.random.uniform(2, 3) + UP*np.random.uniform(-1, 1))
            for e in electrons
        ], run_time=2)

        emission_label = Text("Electrons Emitted!", color=GREEN).to_edge(DOWN)
        self.play(Write(emission_label))
        self.wait(1.5)

        self.play(FadeOut(emission_label), FadeOut(rays_high), FadeOut(high_freq_label))

        # ----------------------------
        # INCREASE INTENSITY (MORE ELECTRONS)
        # ----------------------------
        rays_intense = VGroup(*[
            Arrow(LEFT*5 + UP*i, LEFT*1 + UP*i, color=YELLOW, buff=0)
            for i in np.linspace(-1.5, 1.5, 9)
        ])

        intensity_label = Text("Higher Intensity (More Photons)", font_size=24).to_edge(LEFT)

        self.play(Create(rays_intense), Write(intensity_label))
        self.play(rays_intense.animate.shift(RIGHT*2), run_time=2)

        electrons_more = VGroup(*[
            Dot(plate.get_left() + UP*np.random.uniform(-0.9, 0.9), color=GREEN)
            for _ in range(10)
        ])

        self.play(FadeIn(electrons_more))

        self.play(*[
            e.animate.shift(LEFT*np.random.uniform(2, 3) + UP*np.random.uniform(-1, 1))
            for e in electrons_more
        ], run_time=2)

        more_label = Text("More Electrons Emitted", color=GREEN).to_edge(DOWN)
        self.play(Write(more_label))
        self.wait(2)

        # ----------------------------
        # FINAL SUMMARY
        # ----------------------------
        self.play(FadeOut(*self.mobjects))

        summary = VGroup(
            Text("Key Idea:", font_size=32),
            Text("Frequency → Energy of electrons", font_size=28),
            Text("Intensity → Number of electrons", font_size=28)
        ).arrange(DOWN)

        self.play(Write(summary))
        self.wait(3)