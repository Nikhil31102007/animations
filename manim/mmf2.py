from manim import *
import numpy as np


class MichelsonMorley(Scene):
    def construct(self):

        # ----------------------------
        # Scene 1 — Intro
        # ----------------------------

        title = Text("The Michelson–Morley Experiment")
        subtitle = Text("Testing the 'Ether Wind' Hypothesis").scale(0.6)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ----------------------------
        # Scene 2 — Ether
        # ----------------------------

        ether_label = Text("Ether Wind").to_edge(UP)

        arrows = VGroup(*[
            Arrow(LEFT * 6 + UP * y, RIGHT * 6 + UP * y, buff=0)
            for y in range(-3, 3)
        ])

        self.play(Write(ether_label))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(arrows), FadeOut(ether_label))

        # ----------------------------
        # Scene 3 — Apparatus
        # FIX 1: Moved entire setup UP by 1.5 units so there's clear space
        # below the source dot for the label without overlapping waves.
        # Original center was [0,-2,0] → now [0,-0.5,0]
        # ----------------------------

        center = np.array([0, -0.5, 0])
        L = 3

        splitter = Square(0.3).rotate(PI / 4).move_to(center)
        arm_right = Line(center, center + RIGHT * L)
        arm_up = Line(center, center + UP * L)

        mirror_right = Square(0.3).move_to(arm_right.get_end())
        mirror_up = Square(0.3).move_to(arm_up.get_end())

        source = Dot(center + LEFT * 2)

        apparatus = VGroup(
            splitter, arm_right, arm_up,
            mirror_right, mirror_up,
            source
        )

        self.play(Create(apparatus))
        self.wait(1)

        # ----------------------------
        # FIX 2: Light Source label — placed BELOW the source dot with
        # a fixed perpendicular offset so it never overlaps the incoming
        # wave (which travels horizontally RIGHT toward the splitter).
        # We offset in the direction perpendicular-and-downward from the
        # wave travel direction, scaled enough to clear the wave amplitude.
        # The label rebuilds every frame so it follows apparatus rotation.
        # ----------------------------

        def make_label():
            travel_dir = normalize(splitter.get_center() - source.get_center())
            # Clockwise-perpendicular (initially "down" from wave path)
            perp = np.array([travel_dir[1], -travel_dir[0], 0])
            # Also push away from splitter along the travel direction's opposite
            away = -travel_dir
            pos = source.get_center() + perp * 0.45 + away * 0.55
            return Text("Light Source", font_size=16).move_to(pos)

        source_label = always_redraw(make_label)
        self.add(source_label)

        # ----------------------------
        # Scene 4 — Wave propagation
        # FIX 3: Incoming wave is CLAMPED to stop exactly at the splitter
        # (progress capped at distance source→splitter so it never crosses
        # the beam-splitter boundary). Split waves only start after the
        # incoming wave has fully reached the splitter.
        # ----------------------------

        t = ValueTracker(0)

        # Distance from source to splitter (≈ 2 units)
        src_to_split = np.linalg.norm(splitter.get_center() - source.get_center())

        def wave_func(dist, t_val):
            """Transverse displacement — perpendicular sine wave."""
            return 0.15 * np.sin(8 * (dist - t_val))

        def make_wave(get_start, get_dir, color, delay, max_len=None):
            """
            Builds a direction-vector-based transverse wave.
            - get_start / get_dir are callables → live geometry, so waves
              automatically follow apparatus rotation.
            - delay: t-value at which wave begins propagating.
            - max_len: hard cap on wave length (used to stop incoming wave
              at the splitter).
            """
            def draw():
                start = get_start()
                raw_dir = get_dir()
                raw_len = np.linalg.norm(raw_dir)
                if raw_len < 1e-6:
                    return VMobject()
                d = raw_dir / raw_len                       # unit propagation dir
                perp = np.array([-d[1], d[0], 0])          # CCW perpendicular

                progress = max(0.0, t.get_value() - delay)
                if max_len is not None:
                    progress = min(progress, max_len)       # clamp to max_len
                else:
                    progress = min(progress, L)

                if progress < 1e-4:
                    return VMobject()

                return ParametricFunction(
                    lambda s: start + d * s + perp * wave_func(s, t.get_value()),
                    t_range=[0, progress],
                    color=color,
                )
            return always_redraw(draw)

        # Incoming wave: source → splitter, clamped at src_to_split
        incoming_wave = make_wave(
            get_start=lambda: source.get_center(),
            get_dir=lambda: splitter.get_center() - source.get_center(),
            color=YELLOW,
            delay=0,
            max_len=src_to_split,   # STOPS at the beam-splitter, never crosses
        )

        self.add(incoming_wave)
        # t goes to src_to_split so incoming wave just reaches splitter
        self.play(t.animate.set_value(src_to_split), run_time=3, rate_func=linear)

        # Split waves start RIGHT when incoming wave reaches splitter (delay=src_to_split)
        wave_right = make_wave(
            get_start=lambda: splitter.get_center(),
            get_dir=lambda: arm_right.get_end() - splitter.get_center(),
            color=BLUE,
            delay=src_to_split,
        )

        wave_up = make_wave(
            get_start=lambda: splitter.get_center(),
            get_dir=lambda: arm_up.get_end() - splitter.get_center(),
            color=GREEN,
            delay=src_to_split,
        )

        self.add(wave_right, wave_up)
        self.play(t.animate.set_value(src_to_split + L + 1), run_time=4, rate_func=linear)

        self.wait(2)

        # ----------------------------
        # Prediction
        # ----------------------------

        prediction = Text("If ether exists → Fringe shift expected").scale(0.6)
        prediction.to_edge(DOWN)

        self.play(Write(prediction))
        self.wait(2)
        self.play(FadeOut(prediction))

        # ----------------------------
        # Rotation
        # ----------------------------

        rotate_text = Text("Rotate the apparatus").scale(0.6).to_edge(UP)
        self.play(Write(rotate_text))

        self.play(
            Rotate(apparatus, angle=PI / 2, about_point=splitter.get_center()),
            run_time=4,
        )

        self.wait(2)
        self.play(FadeOut(rotate_text))

        # ----------------------------
        # FIX 4: Clean background before result text.
        # Clear all updaters first, then fade out EVERYTHING (apparatus,
        # waves, label) before writing "No fringe shift detected".
        # ----------------------------

        incoming_wave.clear_updaters()
        wave_right.clear_updaters()
        wave_up.clear_updaters()
        source_label.clear_updaters()

        self.play(FadeOut(*self.mobjects))
        self.wait(0.3)

        # Now result appears on a completely clean black background
        result = Text("No fringe shift detected").scale(0.8)
        conclusion = Text("No ether detected").scale(0.8)

        self.play(Write(result))
        self.wait(2)
        self.play(Transform(result, conclusion))
        self.wait(2)

        # ----------------------------
        # Final screen — already clean
        # ----------------------------

        self.play(FadeOut(*self.mobjects))

        final = Text("Speed of light is the same in all directions.").scale(0.7)
        self.play(Write(final))
        self.wait(3)