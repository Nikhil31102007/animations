from manim import *

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

        # Ether wind arrows
        ether_label = Text("Ether Wind").to_edge(UP)

        arrows = VGroup()
        for y in range(-3, 3):
            arrow = Arrow(LEFT*6 + UP*y, RIGHT*6 + UP*y, buff=0)
            arrows.add(arrow)

        self.play(Write(ether_label))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1))
        self.wait(2)
        self.play(FadeOut(arrows), FadeOut(ether_label))


        # ------------------------------------------------
        # Scene 2 — Apparatus Setup
        # ------------------------------------------------

        # Beam splitter
        splitter = Square(0.3).rotate(PI/4).move_to([0,-2,0])
        
        # Arms
        arm_right = Line(splitter.get_center(), splitter.get_center() + RIGHT*3)
        arm_up = Line(splitter.get_center(), splitter.get_center() + UP*3)

        # Mirrors
        mirror_right = Square(0.3).move_to(arm_right.get_end())
        mirror_up = Square(0.3).move_to(arm_up.get_end())

        # Light source
        source = Dot(splitter.get_center() + LEFT*2)
        source_label = Text("Light Source").scale(0.45).next_to(source, DOWN)

        apparatus = VGroup(
            splitter, arm_right, arm_up,
            mirror_right, mirror_up,
            source, source_label
        )

        self.play(Create(apparatus))
        self.wait(2)


        # ------------------------------------------------
        # Scene 3 — Beam Splitting
        # ------------------------------------------------

        beam_in = Line(source.get_center(), splitter.get_center(), color=YELLOW)
        beam_right = Line(splitter.get_center(), mirror_right.get_center(), color=YELLOW)
        beam_up = Line(splitter.get_center(), mirror_up.get_center(), color=YELLOW)

        self.play(Create(beam_in))
        self.play(Create(beam_right), Create(beam_up))
        self.wait(1)

        # Returning beams
        beam_right_back = Line(mirror_right.get_center(), splitter.get_center(), color=YELLOW)
        beam_up_back = Line(mirror_up.get_center(), splitter.get_center(), color=YELLOW)

        self.play(Create(beam_right_back), Create(beam_up_back))
        self.wait(2)


        # ------------------------------------------------
        # Scene 4 — Expected Fringe Shift
        # ------------------------------------------------

        prediction = Text("If ether exists → Fringe shift expected").scale(0.6)
        prediction.to_edge(DOWN)

        self.play(Write(prediction))
        self.wait(2)
        self.play(FadeOut(prediction))
        self.play(FadeOut(beam_in), FadeOut(beam_up), FadeOut(beam_right), FadeOut(beam_right_back), FadeOut(beam_up_back))
        self.play(FadeOut(apparatus))


        # ------------------------------------------------
        # Scene 5 — Rotate Apparatus
        # ------------------------------------------------

        rotate_text = Text("Rotate the apparatus").scale(0.6)
        rotate_text.to_edge(UP)

        self.play(Write(rotate_text))
        self.play(Rotate(apparatus, angle=PI/2))
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

        self.play(FadeOut(result), FadeOut(apparatus))


        # ------------------------------------------------
        # Scene 7 — Impact
        # ------------------------------------------------

        final = Text("Speed of light is the same in all directions.")
        final.scale(0.7)

        self.play(Write(final))
        self.wait(3)

    