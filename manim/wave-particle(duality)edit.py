
from manim import *
import numpy as np

class WaveParticleDuality(Scene):
    def construct(self):

        # -------------------------------
        # Utility: Interference Function
        # -------------------------------
        def interference_y():
            while True:
                y = np.random.uniform(-3, 3)
                prob = (np.cos(2 * y) ** 2)
                if np.random.random() < prob:
                    return y

        # -------------------------------
        # Setup Static Elements
        # -------------------------------
        source = Dot(LEFT * 5, color=BLUE)
        screen = Line(UP * 3 + RIGHT * 5, DOWN * 3 + RIGHT * 5)

        barrier = Rectangle(height=6, width=0.4, color=GREY, fill_opacity=1)

        slit1 = Rectangle(height=1.2, width=0.5, fill_color=BLACK, fill_opacity=1)
        slit2 = Rectangle(height=1.2, width=0.5, fill_color=BLACK, fill_opacity=1)

        slit1.move_to(UP * 1.5)
        slit2.move_to(DOWN * 1.5)

        slits = VGroup(slit1, slit2)

        self.play(FadeIn(source), Create(screen))
        self.wait(1)

        # =========================================================
        # ACT 1 — PARTICLE BEHAVIOR
        # =========================================================

        explanation1 = Text(
            "Electrons behave like particles\n→ Definite impacts",
            line_spacing=1.2
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation1))

        temp_group = VGroup()
        final_hits = VGroup()

        # Slow start
        for _ in range(8):
            y = np.random.uniform(-2.5, 2.5)
            dot = Dot(source.get_center(), color=YELLOW, radius=0.06)
            trail = TracedPath(dot.get_center, stroke_opacity=[0.3, 0])

            self.add(dot, trail)
            temp_group.add(dot, trail)

            self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
                      run_time=0.5, rate_func=linear)

            final_hits.add(Dot(RIGHT * 5 + UP * y, radius=0.05, color=YELLOW))

        # Fast phase
        for _ in range(25):
            y = np.random.uniform(-2.5, 2.5)
            dot = Dot(source.get_center(), color=YELLOW, radius=0.05)

            self.add(dot)
            temp_group.add(dot)

            self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
                      run_time=0.08, rate_func=linear)

            final_hits.add(Dot(RIGHT * 5 + UP * y, radius=0.04, color=YELLOW))

        self.wait(1)

        # Clean moving elements, keep result
        self.play(FadeOut(temp_group))
        self.play(FadeIn(final_hits))
        self.wait(2)
        self.play(FadeOut(explanation1))


        # =========================================================
        # ACT 2 — DOUBLE SLIT SETUP
        # =========================================================

        self.play(FadeIn(barrier), FadeIn(slits))

        explanation2 = Text(
            "Electrons pass through two slits",
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation2))
        self.wait(2)
        self.play(FadeOut(explanation2))


        # =========================================================
        # ACT 3 — PARTICLE EXPECTATION
        # =========================================================

        explanation3 = Text(
            "If purely particles → two clusters",
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation3))

        temp_group = VGroup()
        cluster_hits = VGroup()

        # Slow
        for _ in range(8):
            y = np.random.choice([
                np.random.uniform(1, 2.5),
                np.random.uniform(-2.5, -1)
            ])

            dot = Dot(source.get_center(), color=YELLOW)
            trail = TracedPath(dot.get_center, stroke_opacity=[0.3, 0])

            self.add(dot, trail)
            temp_group.add(dot, trail)

            mid = UP * y * 0.3

            self.play(dot.animate.move_to(mid), run_time=0.3)
            self.play(dot.animate.move_to(RIGHT * 5 + UP * y), run_time=0.4)

            cluster_hits.add(Dot(RIGHT * 5 + UP * y, radius=0.05))

        # Fast
        for _ in range(30):
            y = np.random.choice([
                np.random.uniform(1, 2.5),
                np.random.uniform(-2.5, -1)
            ])

            dot = Dot(source.get_center(), color=YELLOW)
            self.add(dot)
            temp_group.add(dot)

            self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
                      run_time=0.08)

            cluster_hits.add(Dot(RIGHT * 5 + UP * y, radius=0.04))

        self.wait(1)

        self.play(FadeOut(temp_group))
        self.play(FadeOut(final_hits))  # remove previous experiment result
        self.play(FadeIn(cluster_hits))
        self.wait(2)
        self.play(FadeOut(explanation3))


        # =========================================================
        # ACT 4 — INTERFERENCE REALITY
        # =========================================================

        explanation4 = Text(
            "Reality → Interference Pattern (wave behavior)",
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation4))

        temp_group = VGroup()
        interference_hits = VGroup()

        # Slow build (important)
        for _ in range(10):
            y = interference_y()

            dot = Dot(source.get_center(), color=YELLOW)
            trail = TracedPath(dot.get_center, stroke_opacity=[0.2, 0])

            self.add(dot, trail)
            temp_group.add(dot, trail)

            mid = UP * y * 0.3

            self.play(dot.animate.move_to(mid), run_time=0.25)
            self.play(dot.animate.move_to(RIGHT * 5 + UP * y), run_time=0.35)

            interference_hits.add(Dot(RIGHT * 5 + UP * y, radius=0.05))

        # Fast accumulation
        for _ in range(120):
            y = interference_y()

            dot = Dot(source.get_center(), color=YELLOW)
            self.add(dot)
            temp_group.add(dot)

            self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
                      run_time=0.03)

            interference_hits.add(Dot(RIGHT * 5 + UP * y, radius=0.035))

        self.wait(1)

        self.play(FadeOut(temp_group))
        self.play(FadeOut(cluster_hits))
        self.play(FadeIn(interference_hits))
        # Highlight: enlarge + glow + color shift
        self.play(
            *[
                dot.animate.scale(1.5).set_color(YELLOW)
                for dot in interference_hits
            ],
            run_time=1
        )

        # Add glow (done outside animation for stability)
        for dot in interference_hits:
            dot.set_glow_factor(2.5)

        self.wait(1)

        # -----------------------------------
        # HIGHLIGHT THE PATTERN
        # -----------------------------------

        # Dim background elements
        self.play(
            barrier.animate.set_opacity(0.2),
            slits.animate.set_opacity(0.2),
            source.animate.set_opacity(0.2),
            run_time=1
        )

        # Add glow effect to pattern
        for dot in interference_hits:
            dot.set_glow_factor(2)

        # Slight scale pulse (subtle but powerful)
        self.play(
            interference_hits.animate.scale(1.1),
            run_time=0.5
        )
        self.play(
            interference_hits.animate.scale(1/1.1),
            run_time=0.5
        )

        # Add label
        pattern_label = Text("Interference Pattern", color=YELLOW)\
            .scale(0.6)\
            .to_edge(UP)

        self.play(Write(pattern_label))

        self.wait(2)
        bands = VGroup()

        for y in np.linspace(-2.5, 2.5, 7):
            line = Line(
                RIGHT * 4.5 + UP * y,
                RIGHT * 5.5 + UP * y,
                color=YELLOW,
                stroke_width=3
            )
            bands.add(line)

        self.play(LaggedStart(*[Create(b) for b in bands], lag_ratio=0.1))
        self.wait(1)

        self.play(FadeOut(explanation4))

        #trial
        # After interference pattern is shown

        self.wavefront_scene(source, slit1, slit2, screen)

        self.detector_scene(source, slit1, slit2, screen)

        # =========================================================
        # FINAL MESSAGE
        # =========================================================

        final_text = Text(
            "Particles behave like waves...\nuntil observed.",
            line_spacing=1.2
        ).scale(0.6)

        self.play(FadeIn(final_text))
        self.wait(3)
        self.play(FadeOut(final_text))
    def wavefront_scene(self, source, slit1, slit2, screen):

        explanation = Text(
            "As a wave, it spreads out...\n"
            "Each slit becomes a new wave source",
            line_spacing=1.2
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation))

        # Initial wave from source
        waves = VGroup()

        for r in np.linspace(0.5, 5, 8):
            arc = Arc(
                radius=r,
                start_angle=-PI/2,
                angle=PI,
                arc_center=source.get_center(),
                color=BLUE
            )
            waves.add(arc)

        self.play(LaggedStart(*[FadeIn(w) for w in waves], lag_ratio=0.2))
        self.wait(1)

        # Waves from slits
        slit_waves = VGroup()

        for r in np.linspace(0.3, 4, 10):
            w1 = Arc(radius=r, start_angle=-PI/2, angle=PI,
                    arc_center=slit1.get_center(), color=GREEN)
            w2 = Arc(radius=r, start_angle=-PI/2, angle=PI,
                    arc_center=slit2.get_center(), color=GREEN)
            slit_waves.add(w1, w2)

        self.play(
            FadeOut(waves),
            LaggedStart(*[FadeIn(w) for w in slit_waves], lag_ratio=0.1) 
        )

        self.wait(2)

        self.play(FadeOut(slit_waves), FadeOut(explanation))
    
    def detector_scene(self, source, slit1, slit2, screen):

        explanation = Text(
            "Now we observe which slit the electron passes through...",
            line_spacing=1.2
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation))

        # Detector visuals
        detector1 = Square(side_length=0.3, color=RED).next_to(slit1, LEFT, buff=0.2)
        detector2 = Square(side_length=0.3, color=RED).next_to(slit2, LEFT, buff=0.2)

        self.play(FadeIn(detector1), FadeIn(detector2))
        self.wait(1)

        # Result pattern (two clusters again)
        hits = VGroup()
        temp = VGroup()

        for _ in range(60):
            y = np.random.choice([
                np.random.uniform(1, 2.5),
                np.random.uniform(-2.5, -1)
            ])

            dot = Dot(source.get_center(), color=YELLOW, radius=0.05)
            self.add(dot)
            temp.add(dot)

            self.play(
                dot.animate.move_to(RIGHT * 5 + UP * y),
                run_time=0.05,
                rate_func=linear
            )

            hits.add(Dot(RIGHT * 5 + UP * y, radius=0.04, color=YELLOW))

        self.wait(1)

        # Clean moving particles, keep final result
        self.play(FadeOut(temp))
        self.play(FadeIn(hits))

        final_text = Text(
            "Observation destroys the interference pattern",
            line_spacing=1.2
        ).scale(0.5).to_edge(DOWN)

        self.play(Transform(explanation, final_text))
        self.wait(2)

        self.play(FadeOut(explanation), FadeOut(detector1), FadeOut(detector2))