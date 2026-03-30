from manim import *
import numpy as np

class ComptonEffect(Scene):
    def construct(self):

        # ----------------------------
        # SCENE 1 — SETUP
        # ----------------------------
        title = Text("Compton Effect").to_edge(UP)
        self.play(Write(title))

        photon = Arrow(LEFT*5, LEFT*1, color=YELLOW, buff=0)
        photon.set_stroke(width=6)
        photon.set_color(YELLOW)
        photon.set_opacity(0.8)

        photon_label = Text("Photon", font_size=24).next_to(photon, UP)

        electron = Dot(RIGHT*1, color=BLUE)
        electron_label = Text("Electron", font_size=24).next_to(electron, DOWN)

        self.play(Create(photon), Write(photon_label))
        self.play(FadeIn(electron), Write(electron_label))

        self.wait()

        # ----------------------------
        # SCENE 2 — COLLISION
        # ----------------------------
        collision_point = electron.get_center()

        self.play(photon.animate.shift(RIGHT*4), run_time=2)
        
        #photon = Arrow(collision_point + LEFT*0.5, collision_point, color=YELLOW, buff=0)

        # Scattered photon
        scattered_photon = Arrow(
            collision_point,
            collision_point + UP*2 + RIGHT*2,
            color=YELLOW,
            buff=0
        )
        
        #scattering angle
        # Angle arc (theta)
        angle = Angle(
            Line(collision_point, collision_point + RIGHT*2),
            Line(collision_point, collision_point + UP*2 + RIGHT*2),
            radius=0.5,
            color=WHITE
        )

        theta_label = MathTex("\\theta").next_to(angle, RIGHT)


        # Recoiled electron
        recoiled_electron = Dot(color=BLUE).move_to(collision_point)

        self.play(Create(angle), Write(theta_label))
        self.play(
            FadeOut(photon),
            FadeOut(electron_label),
            FadeOut(photon),
            electron.animate.scale(1.2),
        )

        self.play(
            Create(scattered_photon),
            recoiled_electron.animate.shift(RIGHT*2 + DOWN*1),
            run_time=2
        )

        # Labels
        sp_label = Text("Photon (λ ↑, E ↓)", font_size=24).next_to(scattered_photon, UP)
        re_label = Text("Electron (E ↑)", font_size=24).next_to(recoiled_electron, DOWN)

        self.play(Write(sp_label), Write(re_label))
        self.wait()

        # ----------------------------
        # SCENE 3 — ENERGY TEXT
        # ----------------------------
        energy_text = VGroup(
            MathTex("E = h\\nu"),
            MathTex("E = \\frac{hc}{\\lambda}")
        ).arrange(DOWN).to_edge(LEFT)

        self.play(Write(energy_text))
        self.wait()
        self.clear()
        # ----------------------------
        # SCENE 4 — GRAPH
        # ----------------------------
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        labels = axes.get_axis_labels(
            Text("Time"), Text("Energy")
        )

        # Photon energy decreases
        photon_energy_graph = axes.plot(
            lambda x: 4 if x < 2 else 4 - 1.2*(x-2),
            x_range=[0, 5],
        )

        # Electron energy increases
        electron_energy_graph = axes.plot(
            lambda x: 0 if x < 2 else 1.2*(x-2),
            x_range=[0, 5],
        )

        photon_graph_label = Text("Photon Energy", font_size=24).next_to(photon_energy_graph, UP)
        electron_graph_label = Text("Electron Energy", font_size=24).next_to(electron_energy_graph, DOWN)
        photon_graph_label.scale(0.8)
        electron_graph_label.scale(0.8)
         
        self.play(Create(axes), Write(labels))
        self.play(Create(photon_energy_graph), Write(photon_graph_label))
        self.play(Create(electron_energy_graph), Write(electron_graph_label))
        tracker = ValueTracker(0)

        dot_photon = always_redraw(lambda: 
            Dot(axes.c2p(tracker.get_value(), 
                        4 if tracker.get_value() < 2 else 4 - 1.2*(tracker.get_value()-2)))
        )

        dot_electron = always_redraw(lambda: 
            Dot(axes.c2p(tracker.get_value(), 
                        0 if tracker.get_value() < 2 else 1.2*(tracker.get_value()-2)))
        )

        self.add(dot_photon, dot_electron)
        self.play(tracker.animate.set_value(5), run_time=4, rate_func=linear)


        self.wait()
        graph_group = VGroup(
            axes,
            labels,
            photon_energy_graph,
            electron_energy_graph,
            photon_graph_label,
            electron_graph_label,
            dot_photon,
            dot_electron
        )
        self.play(
            graph_group.animate.scale(0.6).to_corner(DL),
            run_time=1.5,
            rate_functions=smooth
        )

        # ----------------------------
        # SCENE 5 — FORMULA
        # ----------------------------
        formula = MathTex(
            "\\Delta \\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta)"
        ).to_edge(UR,buff=1)

        box = SurroundingRectangle(formula, color=WHITE)


        note = Text("Wavelength increases after scattering", font_size=24).next_to(formula, DOWN)
        self.play(Write(note))


        self.play(Write(formula), Create(box))
        self.wait(2)

        # Fade out nicely
        self.play(
            FadeOut(*self.mobjects)
        )
        self.wait(2)