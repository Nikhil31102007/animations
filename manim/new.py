# from manim import *
# import numpy as np

# class WaveParticleDuality(Scene):
#     def construct(self):

#         # -------------------------------
#         # ACT 1 — Particle Behavior
#         # -------------------------------

#         title = Text("Wave–Particle Duality").scale(0.9)
#         subtitle = Text("Do particles behave like waves?").scale(0.5)
#         subtitle.next_to(title, DOWN)

#         self.play(FadeIn(title), FadeIn(subtitle))
#         self.wait(2)
#         self.play(FadeOut(title), FadeOut(subtitle))

#         # Source and screen
#         source = Dot(LEFT * 5, color=BLUE)
#         screen = Line(UP * 3 + RIGHT * 5, DOWN * 3 + RIGHT * 5)

#         self.play(FadeIn(source), Create(screen))

#         # Emit particles
#         particles = VGroup()
#         for _ in range(30):
#             y = np.random.uniform(-2.5, 2.5)
#             dot = Dot(source.get_center(), color=YELLOW, radius=0.06)
#             particles.add(dot)

#             self.add(dot)
#             self.play(dot.animate.move_to(RIGHT * 5 + UP * y), run_time=0.1)

#         self.wait(1)

#         label1 = Text("Particles hit at definite positions").scale(0.5)
#         label1.to_edge(DOWN)
#         self.play(Write(label1))
#         self.wait(2)
#         self.play(FadeOut(label1))

#         self.play(FadeOut(particles), FadeOut(source), FadeOut(screen))


#         # -------------------------------
#         # ACT 2 — Double Slit Setup
#         # -------------------------------

#         barrier = Rectangle(height=6, width=0.3).move_to(ORIGIN)
#         slit1 = Rectangle(height=1, width=0.35, color=BLACK).move_to(UP * 1.5)
#         slit2 = Rectangle(height=1, width=0.35, color=BLACK).move_to(DOWN * 1.5)

#         barrier = Difference(barrier, VGroup(slit1, slit2))

#         source = Dot(LEFT * 5, color=BLUE)
#         screen = Line(UP * 3 + RIGHT * 5, DOWN * 3 + RIGHT * 5)

#         self.play(FadeIn(source), Create(barrier), Create(screen))
#         self.wait(1)

#         # -------------------------------
#         # ACT 3 — Particle through slits
#         # -------------------------------

#         hits = VGroup()

#         for _ in range(40):
#             y = np.random.choice([np.random.uniform(0.5, 2.5),
#                                   np.random.uniform(-2.5, -0.5)])

#             dot = Dot(source.get_center(), color=YELLOW, radius=0.05)
#             self.add(dot)

#             self.play(dot.animate.move_to(RIGHT * 5 + UP * y), run_time=0.08)
#             hits.add(dot)

#         label2 = Text("Two clusters form (particle expectation)").scale(0.5)
#         label2.to_edge(DOWN)
#         self.play(Write(label2))
#         self.wait(2)
#         self.play(FadeOut(label2))


#         # -------------------------------
#         # ACT 4 — Wave Behavior
#         # -------------------------------

#         self.play(FadeOut(hits))

#         def wave_func(x, shift):
#             return 0.7 * np.sin(3 * x + shift)

#         wave1 = FunctionGraph(lambda x: wave_func(x, 0),
#                               x_range=[-5, 5], color=BLUE)
#         wave2 = FunctionGraph(lambda x: wave_func(x, PI/2),
#                               x_range=[-5, 5], color=GREEN)

#         wave_group = VGroup(wave1, wave2)

#         self.play(Create(wave_group))
#         self.wait(1)

#         # Interference pattern (dots)
#         interference = VGroup()
#         for i in range(80):
#             y = np.sin(i * 0.3) * 2
#             dot = Dot(RIGHT * 5 + UP * y, radius=0.05)
#             interference.add(dot)

#         self.play(FadeOut(wave_group), FadeIn(interference))

#         label3 = Text("Interference pattern appears (wave behavior)").scale(0.5)
#         label3.to_edge(DOWN)
#         self.play(Write(label3))
#         self.wait(2)
#         self.play(FadeOut(label3))


#         # -------------------------------
#         # ACT 5 — Single Particle Build-up
#         # -------------------------------

#         self.play(FadeOut(interference))

#         buildup = VGroup()

#         for i in range(120):
#             y = np.sin(i * 0.2) * 2 + np.random.uniform(-0.2, 0.2)
#             dot = Dot(source.get_center(), color=YELLOW, radius=0.04)
#             self.add(dot)

#             self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
#                       run_time=0.05)
#             buildup.add(dot)

#         label4 = Text("Single particles... building a wave pattern").scale(0.5)
#         label4.to_edge(DOWN)
#         self.play(Write(label4))
#         self.wait(2)
#         self.play(FadeOut(label4))


#         # -------------------------------
#         # ACT 6 — Wavefunction Visualization
#         # -------------------------------

#         self.play(FadeOut(buildup))

#         wave_packet = FunctionGraph(
#             lambda x: np.exp(-0.3 * x**2) * np.sin(5 * x),
#             x_range=[-4, 4],
#             color=BLUE
#         )

#         self.play(Create(wave_packet))
#         self.wait(1)

#         collapse_dot = Dot(color=YELLOW).move_to(RIGHT * 2)

#         self.play(Transform(wave_packet, collapse_dot))
#         self.wait(1)

#         label5 = Text("Wave collapses upon observation").scale(0.5)
#         label5.to_edge(DOWN)
#         self.play(Write(label5))
#         self.wait(2)
#         self.play(FadeOut(label5))


#         # -------------------------------
#         # FINAL SCENE
#         # -------------------------------

#         final_text = Text(
#             "Particles behave like waves...\nuntil observed.",
#             line_spacing=1.2
#         ).scale(0.6)

#         self.play(FadeIn(final_text))
#         self.wait(3)
#         self.play(FadeOut(final_text))
        
# from manim import *                       hereehrehrehrheh
# import numpy as np

# class WaveParticleDuality(Scene):
#     def construct(self):

#         # -----------------------------------
#         # Utility: Interference Distribution
#         # -----------------------------------
#         def interference_y():
#             while True:
#                 y = np.random.uniform(-3, 3)
#                 prob = (np.cos(2 * y) ** 2)
#                 if np.random.random() < prob:
#                     return y

#         # -----------------------------------
#         # ACT 1 — Particle Behavior
#         # -----------------------------------

#         title = Text("Wave–Particle Duality").scale(0.9)
#         self.play(Write(title))
#         self.wait(1.5)
#         self.play(FadeOut(title))

#         explanation1 = Text(
#             "Electrons behave like particles\n"
#             "→ They travel in straight paths\n"
#             "→ They hit at definite positions",
#             line_spacing=1.2
#         ).scale(0.5).to_edge(DOWN)

#         source = Dot(LEFT * 5, color=BLUE)
#         screen = Line(UP * 3 + RIGHT * 5, DOWN * 3 + RIGHT * 5)

#         self.play(FadeIn(source), Create(screen))
#         self.play(Write(explanation1))

#         for _ in range(20):
#             y = np.random.uniform(-2.5, 2.5)

#             dot = Dot(source.get_center(), color=YELLOW, radius=0.06)
#             trail = TracedPath(dot.get_center, stroke_opacity=[0.3, 0])

#             self.add(dot, trail)

#             self.play(
#                 dot.animate.move_to(RIGHT * 5 + UP * y),
#                 run_time=0.5,
#                 rate_func=linear
#             )

#         self.wait(1)
#         self.play(FadeOut(explanation1), FadeOut(source), FadeOut(screen))


#         # -----------------------------------
#         # ACT 2 — Double Slit Setup
#         # -----------------------------------

#         explanation2 = Text(
#             "Now electrons are fired toward two narrow slits",
#         ).scale(0.5).to_edge(DOWN)

#         barrier = Rectangle(height=6, width=0.4, color=GREY, fill_opacity=1)

#         slit1 = Rectangle(height=1.2, width=0.5, fill_color=BLACK, fill_opacity=1)
#         slit2 = Rectangle(height=1.2, width=0.5, fill_color=BLACK, fill_opacity=1)

#         slit1.move_to(UP * 1.5)
#         slit2.move_to(DOWN * 1.5)

#         slits = VGroup(slit1, slit2)

#         source = Dot(LEFT * 5, color=BLUE)
#         screen = Line(UP * 3 + RIGHT * 5, DOWN * 3 + RIGHT * 5)

#         self.play(FadeIn(source), FadeIn(barrier), FadeIn(slits), Create(screen))
#         self.play(Write(explanation2))
#         self.wait(2)
#         self.play(FadeOut(explanation2))


#         # -----------------------------------
#         # ACT 3 — Particle Expectation
#         # -----------------------------------

#         explanation3 = Text(
#             "If electrons were only particles,\n"
#             "they would form two clusters",
#             line_spacing=1.2
#         ).scale(0.5).to_edge(DOWN)

#         self.play(Write(explanation3))

#         for _ in range(30):
#             y = np.random.choice([
#                 np.random.uniform(0.8, 2.5),
#                 np.random.uniform(-2.5, -0.8)
#             ])

#             dot = Dot(source.get_center(), color=YELLOW, radius=0.05)
#             trail = TracedPath(dot.get_center, stroke_opacity=[0.3, 0])

#             self.add(dot, trail)

#             mid = UP * y * 0.3

#             self.play(dot.animate.move_to(mid), run_time=0.25, rate_func=linear)
#             self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
#                       run_time=0.35, rate_func=linear)

#         self.wait(1.5)
#         self.play(FadeOut(explanation3))


#         # -----------------------------------
#         # ACT 4 — Reality: Interference
#         # -----------------------------------

#         explanation4 = Text(
#             "But instead, an interference pattern appears\n"
#             "→ A signature of wave behavior",
#             line_spacing=1.2
#         ).scale(0.5).to_edge(DOWN)

#         self.play(Write(explanation4))

#         dots = VGroup()

#         for _ in range(120):
#             y = interference_y()

#             dot = Dot(source.get_center(), color=YELLOW, radius=0.04)
#             trail = TracedPath(dot.get_center, stroke_opacity=[0.2, 0])

#             self.add(dot, trail)

#             mid = UP * y * 0.3

#             self.play(dot.animate.move_to(mid), run_time=0.2, rate_func=linear)
#             self.play(dot.animate.move_to(RIGHT * 5 + UP * y),
#                       run_time=0.3, rate_func=linear)

#             dots.add(dot)

#         self.wait(2)
#         self.play(FadeOut(explanation4))


#         # -----------------------------------
#         # ACT 5 — Single Particle Build-Up
#         # -----------------------------------

#         explanation5 = Text(
#             "Even when fired one at a time...\n"
#             "they gradually build the same pattern",
#             line_spacing=1.2
#         ).scale(0.5).to_edge(DOWN)

#         self.play(Write(explanation5))

#         self.wait(2)
#         self.play(FadeOut(explanation5))


#         # -----------------------------------
#         # ACT 6 — Wavefunction Idea
#         # -----------------------------------

#         explanation6 = Text(
#             "Each electron behaves like a wave\n"
#             "passing through both slits simultaneously",
#             line_spacing=1.2
#         ).scale(0.5).to_edge(DOWN)

#         wave_packet = FunctionGraph(
#             lambda x: np.exp(-0.3 * x**2) * np.sin(5 * x),
#             x_range=[-4, 4],
#             color=BLUE
#         )

#         self.play(Create(wave_packet))
#         self.play(Write(explanation6))
#         self.wait(2)

#         collapse_dot = Dot(color=YELLOW).move_to(RIGHT * 2)

#         self.play(Transform(wave_packet, collapse_dot))
#         self.wait(1)

#         self.play(FadeOut(explanation6))


#         # -----------------------------------
#         # FINAL MESSAGE
#         # -----------------------------------

#         final_text = Text(
#             "Electrons behave like waves...\n"
#             "until we observe them.",
#             line_spacing=1.2
#         ).scale(0.6)

#         self.play(FadeIn(final_text))
#         self.wait(3)
#         self.play(FadeOut(final_text))


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

        self.play(LaggedStart(*[Create(w) for w in waves], lag_ratio=0.2))
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
            LaggedStart(*[Create(w) for w in slit_waves], lag_ratio=0.1)
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