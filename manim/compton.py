
from manim import *
import numpy as np

class ComptonEffect(Scene):

    # ----------------------------
    # PHOTON WAVE (CLEARLY VISIBLE)
    # ----------------------------
    def photon_wave(self, start, end, color=YELLOW):
        direction = end - start
        length = np.linalg.norm(direction)
        unit_dir = direction / length

        amplitude = 0.2
        wavelength = 0.6

        perp = np.array([-unit_dir[1], unit_dir[0], 0])

        def wave_func(t):
            return start + unit_dir*t + amplitude*np.sin(2*np.pi*t/wavelength)*perp

        wave = ParametricFunction(
            wave_func,
            t_range=[0, length],
            stroke_width=3,
            color=color,
            stroke_opacity=0.9
        )

        angle = np.arctan2(unit_dir[1], unit_dir[0])

        arrow = Triangle(fill_opacity=1, color=color).scale(0.15)
        arrow.rotate(angle - PI/2)
        arrow.move_to(end + unit_dir * 0.15)

        wave.set_z_index(1)
        arrow.set_z_index(2)

        return VGroup(wave, arrow)

    def construct(self):

        title = Text("Compton Scattering").to_edge(UP)
        self.play(Write(title))

        # ----------------------------
        # INITIAL OBJECTS
        # ----------------------------
        photon = self.photon_wave(LEFT*6, LEFT*2)
        photon_label = Text("Photon", font_size=24).next_to(photon, UP)

        electron = Dot(RIGHT*1, color=BLUE).scale(1.2)
        electron_label = Text("Electron", font_size=24).next_to(electron, DOWN)

        self.play(Create(photon), Write(photon_label))
        self.play(FadeIn(electron), Write(electron_label))
        self.wait()

        collision_point = electron.get_center()

        self.play(
            photon.animate.shift(RIGHT*4),
            run_time=2
        )
        self.remove(photon)
        # Fade photon at collision point
        self.play(FadeOut(photon), run_time=0.5)

        # ----------------------------
        # SCATTERED PHOTON (θ)
        # ----------------------------
        theta = PI/3
        photon_dir = np.array([np.cos(theta), np.sin(theta), 0])

        scattered_photon = self.photon_wave(
            collision_point,
            collision_point + 4 * photon_dir
        )
        scattered_photon.set_opacity(0.8)
        theta_arc = Angle(
            Line(collision_point, collision_point + RIGHT*3),
            Line(collision_point, collision_point + photon_dir*3),
            radius=0.7,
            color=WHITE
        )

        theta_label = MathTex("\\theta").next_to(theta_arc, RIGHT)

        # ----------------------------
        # ELECTRON DEFLECTION (γ)
        # ----------------------------
        gamma = PI/4

        electron_dir = np.array([
            np.cos(gamma),
            -np.sin(gamma),
            0
        ])

        recoiled_electron = Dot(color=BLUE).scale(1.2).move_to(collision_point)

        incident_line = Line(collision_point, collision_point + RIGHT*3)
        electron_line = Line(collision_point, collision_point + electron_dir*3)

        gamma_arc = Angle(
            incident_line,
            electron_line,
            radius=1,
            color=BLUE,
            other_angle=True   
        )

        gamma_label = MathTex("\\gamma").next_to(gamma_arc, DOWN)

        # show angles clearly
        self.play(Create(theta_arc), Write(theta_label))
        self.play(Create(gamma_arc), Write(gamma_label))

        self.play(
            FadeOut(photon),
            FadeOut(electron_label),
            electron.animate.scale(1.3),
        )

        self.play(
            Create(scattered_photon),
            recoiled_electron.animate.shift(4 * electron_dir),
            run_time=2
        )

        self.wait()

        self.clear()

        # ----------------------------
        # ENERGY vs ANGLE GRAPH (BATTLE STYLE)
        # ----------------------------
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=4,
        )

        labels = axes.get_axis_labels(
            MathTex("\\theta"),
            Text("Energy")
        )

        # exaggerated for visibility (battle crossing)
        photon_energy = axes.plot(
            lambda x: 4 - 2*(1 - np.cos(x)),
            x_range=[0, 2*PI],
            color=RED
        )

        electron_energy = axes.plot(
            lambda x: 2*(1 - np.cos(x)),
            x_range=[0, 2*PI],
            color=BLUE
        )

        photon_text = Text("Photon", color=RED).scale(0.7).next_to(photon_energy, DOWN)
        electron_text = Text("Electron", color=BLUE).scale(0.7).next_to(electron_energy, UP)

        self.play(Create(axes), Write(labels))
        self.play(Create(photon_energy), Write(photon_text))
        self.play(Create(electron_energy), Write(electron_text))

        # moving dots (battle interaction)
        tracker = ValueTracker(0)

        dot_photon = always_redraw(lambda:
            Dot(color=RED).move_to(
                axes.c2p(
                    tracker.get_value(),
                    4 - 2*(1 - np.cos(tracker.get_value()))
                )
            )
        )

        dot_electron = always_redraw(lambda:
            Dot(color=BLUE).move_to(
                axes.c2p(
                    tracker.get_value(),
                    2*(1 - np.cos(tracker.get_value()))
                )
            )
        )

        self.add(dot_photon, dot_electron)

        self.play(tracker.animate.set_value(2*PI), run_time=5, rate_func=linear)

        self.wait()

        # ----------------------------
        # FINAL FORMULA
        # ----------------------------
        formula = MathTex(
            "\\Delta \\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta)"
        ).to_edge(UR)

        box = SurroundingRectangle(formula)

        self.play(Write(formula), Create(box))
        self.wait(2)

        self.play(FadeOut(*self.mobjects))
        self.wait()
