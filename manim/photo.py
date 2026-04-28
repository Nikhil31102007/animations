from manim import *
import numpy as np

class PhotoelectricEffectSlanted(Scene):
    def construct(self):

        # ----------------------------
        # TITLE
        # ----------------------------
        title = Text("Photoelectric Effect").to_edge(UP)
        self.play(Write(title))

        # Reference Y just below title (so rays don't overlap it)
        top_y = title.get_bottom()[1] - 1

        # ----------------------------
        # METAL PLATE (BOTTOM)
        # ----------------------------
        plate = Rectangle(width=6, height=1, color=BLUE).to_edge(DOWN)
        plate_label = Text("Metal Surface", font_size=24).next_to(plate, DOWN)

        self.play(Create(plate), Write(plate_label))

        # ----------------------------
        # HELPER: SLANTED RAYS (FIXED)
        # ----------------------------
        def create_slanted_rays(n, color, spread=2.5):
            rays = VGroup()
            xs = np.linspace(-spread, spread, n)

            for x in xs:
                start = np.array([x - 1, top_y, 0])     # starts BELOW title
                end = np.array([x + 0.5, -1.5, 0])      # shorter + angled

                ray = Arrow(start, end, buff=0, color=color)
                rays.add(ray)

            return rays

        # ----------------------------
        # LOW FREQUENCY (NO EMISSION)
        # ----------------------------
        rays_low = create_slanted_rays(6, RED)

        low_label = Text("Low Frequency Light", font_size=24).next_to(title, DOWN)

        self.play(Create(rays_low), Write(low_label))
        self.wait(2)

        no_emission = Text("No Electrons Emitted", color=RED).next_to(plate, UP, buff=0.5)
        self.play(Write(no_emission))
        self.wait(2)

        self.play(FadeOut(rays_low), FadeOut(low_label), FadeOut(no_emission))

        # ----------------------------
        # HIGH FREQUENCY (EMISSION)
        # ----------------------------
        rays_high = create_slanted_rays(6, YELLOW)

        high_label = Text("High Frequency Light", font_size=24).next_to(title, DOWN)

        self.play(Create(rays_high), Write(high_label))
        self.wait(1.5)

        electrons = VGroup(*[
            Dot(
                plate.get_top() + RIGHT*np.random.uniform(-2.5, 2.5),
                radius=0.05,
                color=GREEN
            )
            for _ in range(6)
        ])

        self.play(FadeIn(electrons))

        animations = []
        for e in electrons:
            dx = np.random.uniform(-2, 2)
            dy = np.random.uniform(1.5, 3)

            animations.append(
                e.animate.shift(RIGHT*dx + UP*dy).set_run_time(2.5)
            )

        self.play(*animations)

        emission_label = Text("Electrons Emitted!", color=GREEN).next_to(plate, UP, buff=0.5)
        self.play(Write(emission_label))
        self.wait(2)

        self.play(
            FadeOut(electrons),
            FadeOut(rays_high),
            FadeOut(high_label),
            FadeOut(emission_label)
        )

        # ----------------------------
        # HIGH INTENSITY (MORE ELECTRONS)
        # ----------------------------
        rays_intense = create_slanted_rays(10, YELLOW, spread=3)

        intensity_label = Text("Higher Intensity (More Photons)", font_size=24).next_to(title, DOWN)

        self.play(Create(rays_intense), Write(intensity_label))
        self.wait(1.5)

        electrons_more = VGroup(*[
            Dot(
                plate.get_top() + RIGHT*np.random.uniform(-3, 3),
                radius=0.05,
                color=GREEN
            )
            for _ in range(10)
        ])

        self.play(FadeIn(electrons_more))

        animations = []
        for e in electrons_more:
            dx = np.random.uniform(-2.5, 2.5)
            dy = np.random.uniform(1.5, 3.5)

            animations.append(
                e.animate.shift(RIGHT*dx + UP*dy).set_run_time(2.5)
            )

        self.play(*animations)

        more_label = Text("More Electrons Emitted", color=GREEN).next_to(plate, UP, buff=0.5)
        self.play(Write(more_label))
        self.wait(2)

        self.play(
            FadeOut(electrons_more),
            FadeOut(rays_intense),
            FadeOut(intensity_label),
            FadeOut(more_label)
        )

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
