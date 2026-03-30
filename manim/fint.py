from manim import *

class EqualFall(Scene):
    def construct(self):

        #scene1 title

        title = Text("Heavier objects fall faster... right?")
        title.to_edge(UP)

        feather = Circle(radius=0.2, color=WHITE).shift(LEFT * 3)
        feather_label = Text("Light").scale(0.5).next_to(feather, DOWN)

        ball = Circle(radius=0.6, color=BLUE).shift(RIGHT * 3)
        ball_label = Text("Heavy").scale(0.5).next_to(ball, DOWN)

        self.play(Write(title))
        self.play(FadeIn(feather), FadeIn(ball))
        self.play(FadeIn(feather_label), FadeIn(ball_label))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(feather_label), FadeOut(ball_label))


        #Scene 2 — Vacuum Drop
        
        vacuum_text = Text("Vacuum (No Air)").to_edge(UP)
        ground = Line(LEFT*6, RIGHT*6).to_edge(DOWN)

        self.play(Write(vacuum_text), Create(ground))

        #reset positions
        feather.move_to(LEFT*3 + UP*2)
        ball.move_to(RIGHT*3 + UP*2)

        self.play(
            feather.animate.shift(DOWN*4),
            ball.animate.shift(DOWN*4),
            run_time=2,
            rate_func=linear
        )

        self.wait(1)

        self.play(FadeOut(vacuum_text))



        # Scene 3 — The Math

        eq1 = MathTex("F = m g")
        eq2 = MathTex("F = m a")
        eq_group = VGroup(eq1, eq2).arrange(DOWN, buff=1)

        self.play(FadeOut(feather), FadeOut(ball))
        self.play(Write(eq_group))
        self.wait(1)

        combined = MathTex("m g = m a")
        self.play(TransformMatchingTex(eq_group, combined))
        self.wait(1)

        result = MathTex("a = g")
        self.play(TransformMatchingTex(combined, result))
        self.wait(2)


        
        #scene 4 — explanation of f

        heavy_obj = Circle(radius=0.6, color=BLUE).shift(LEFT*3)
        light_obj = Circle(radius=0.2, color=WHITE).shift(RIGHT*3)

        gravity_heavy = Arrow(heavy_obj.get_top(), heavy_obj.get_bottom()+DOWN*1.5, color=RED)
        gravity_light = Arrow(light_obj.get_top(), light_obj.get_bottom()+DOWN*0.7, color=RED)

        label = Text("Heavier object → more gravity\nbut more resistance").scale(0.6)
        label.to_edge(UP)

        self.play(FadeOut(result))
        self.play(FadeIn(heavy_obj), FadeIn(light_obj))
        self.play(GrowArrow(gravity_heavy), GrowArrow(gravity_light))
        self.play(Write(label))
        self.wait(3)

        self.play(FadeOut(label), FadeOut(gravity_heavy), FadeOut(gravity_light))
        self.play(FadeOut(light_obj), FadeOut(heavy_obj))



        # Scene 5 — Air Drag

        air_text = Text("In Air: Drag Slows Light Objects").to_edge(UP)

        feather.move_to(LEFT*3 + UP*2)
        ball.move_to(RIGHT*3 + UP*2)

        drag_arrow =always_redraw(lambda: Arrow(feather.get_bottom(), feather.get_bottom()+UP*1.5, color=YELLOW))
        drag_arrow2 =always_redraw(lambda: Arrow(ball.get_center(), ball.get_top()+UP*.6, color=RED))

        self.play(FadeIn(air_text))
        self.play(FadeIn(feather), FadeIn(ball))
        self.play(GrowArrow(drag_arrow), GrowArrow(drag_arrow2))

        self.play(
            feather.animate.shift(DOWN*2),
            ball.animate.shift(DOWN*4),
            run_time=2,
            rate_func=linear
        )

        self.wait(2)

        self.play(FadeOut(air_text), FadeOut(drag_arrow), FadeOut(drag_arrow2))


        
        # Scene 6 — Final Statement

        final_text = Text("Gravity accelerates everything equally.")
        final_text.scale(0.8)

        self.play(FadeOut(feather), FadeOut(ball))
        self.wait()
        self.play(Write(final_text), run_time=2)
        self.wait(2)