from manim import *


# ─────────────────────────────────────────────────────────────────────────────
#  LAYOUT CONSTANTS
#  Left zone  (graph only):  x ∈ [-7.1, -1.2]
#  Right zone (math only):   x ∈ [-0.8,  6.5]   → anchor MATH_X = RIGHT * 2.8
#  All MathTex scaled to MSCALE = 0.72 for visual consistency
#  VGroups arranged with VBUFF = 0.32 vertical gap
# ─────────────────────────────────────────────────────────────────────────────
MATH_X  = RIGHT * 2.8          # horizontal anchor for every math block
MSCALE  = 0.72                 # uniform MathTex scale
VBUFF   = 0.32                 # vertical spacing inside VGroups


def mmath(*args):
    """Return a scaled MathTex (or list of them) at MSCALE."""
    objs = [MathTex(a).scale(MSCALE) for a in args]
    return objs[0] if len(objs) == 1 else objs


def math_vgroup(*latex_strings, scale=MSCALE, buff=VBUFF):
    """Build a vertically arranged VGroup of MathTex, centred on MATH_X."""
    items = [MathTex(s).scale(scale) for s in latex_strings]
    return VGroup(*items).arrange(DOWN, buff=buff).move_to(MATH_X)


def right_title(text, scale=0.65):
    """A section title that lives in the right zone, top area."""
    return (
        Text(text).scale(scale)
        .move_to(MATH_X + UP * 3.1)
    )


class FullLorentzDerivation(Scene):
    def construct(self):

        # ─────────────────────────────────────────────────────────────────────
        # FRAME SETUP
        # Axes shrunk to x_length=5, y_length=3.5 and pinned to DL corner
        # so they occupy x ∈ [-6.6, -1.6], leaving the right half for math.
        # ─────────────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 6],
            y_range=[0, 4],
            x_length=5,
            y_length=3.2,
            axis_config={"include_tip": True},
        ).to_corner(DL, buff=0.6)   # larger buff → axes sit higher, labels clear top

        labels = axes.get_axis_labels("x", "t")

        # frameS: centred horizontally over axes, elevated above t-axis tip
        frameS = (
            Text("Frame S").scale(0.55)
            .next_to(axes, UP, buff=0.55)     # buff=0.55 clears the t-axis arrow tip
        )

        self.play(Create(axes), Write(labels))
        self.play(Write(frameS))
        self.wait(2)

        # axes_p: copy of axes pre-shifted RIGHT so Frame S' label never touches
        # Frame S label or the t' axis-tip from the start.
        axes_p = axes.copy().set_color(BLUE).shift(RIGHT * 1.8)
        labels_p = axes_p.get_axis_labels("x'", "t'").set_color(BLUE)

        # frameSp: same large buff as frameS so it clears the t'-axis arrow tip.
        # Horizontally it is auto-centred over axes_p via next_to.
        frameSp = (
            Text("Frame S'").scale(0.55).set_color(BLUE)
            .next_to(axes_p, UP, buff=0.55)   # matches frameS buff → same height
        )

        self.play(Create(axes_p), Write(labels_p), Write(frameSp))
        self.wait(2)

        velocity = MathTex("v").scale(0.6).next_to(frameSp, RIGHT, buff=0.2)
        self.play(Write(velocity))

        # Shift axes_p group right to show relative motion.
        # frameSp and velocity shift with it — next_to relationship keeps them
        # horizontally centred above axes_p after the shift as well.
        self.play(
            axes_p.animate.shift(RIGHT * 1.2),
            labels_p.animate.shift(RIGHT * 1.2),
            frameSp.animate.shift(RIGHT * 1.2),
            velocity.animate.shift(RIGHT * 1.2),
            run_time=4,
        )
        self.wait(2)

        # ─────────────────────────────────────────────────────────────────────
        # EVENT WITH COORDINATES
        # Event dot placed on axes (left zone).  Coordinate labels go into
        # the right zone so they never overlap the dot or axes.
        # ─────────────────────────────────────────────────────────────────────
        # Event dot lives in Frame S' (the blue axes) as requested
        event = Dot(color=RED).move_to(axes_p.c2p(3, 2))

        # Coordinate labels in the right zone (clear of both axes)
        coordS  = MathTex("(x,t)").scale(MSCALE).move_to(MATH_X + UP * 1.0)
        coordSp = (
            MathTex("(x',t')").scale(MSCALE).set_color(BLUE)
            .move_to(MATH_X + UP * 0.3)
        )

        self.play(FadeIn(event))
        self.play(Write(coordS))
        self.play(Write(coordSp))
        self.wait(4)

        self.play(FadeOut(coordS), FadeOut(coordSp), FadeOut(event))

        # ─────────────────────────────────────────────────────────────────────
        # GENERAL LINEAR TRANSFORMATION
        # All math in the right zone; title in upper-right area.
        # ─────────────────────────────────────────────────────────────────────
        title = right_title("General Linear Transformation")

        general = math_vgroup(
            "x' = Ax + Bt",
            "t' = Dx + Et",
        )

        self.play(Write(title))
        self.play(Write(general))
        self.wait(4)

        # ─────────────────────────────────────────────────────────────────────
        # RELATIVE MOTION CONDITION
        # Stacked below 'general' in the right zone.
        # ─────────────────────────────────────────────────────────────────────
        cond = math_vgroup("x = vt", "x' = 0").move_to(MATH_X + DOWN * 1.2)

        self.play(Write(cond))
        self.wait(3)

        # Step-by-step derivation: each step replaces the previous in-place
        derive1 = MathTex("0 = A(vt) + Bt").scale(MSCALE).move_to(MATH_X + DOWN * 2.3)
        derive2 = MathTex("0 = t(Av + B)").scale(MSCALE).move_to(MATH_X + DOWN * 2.3)
        derive3 = MathTex("B = -Av").scale(MSCALE).move_to(MATH_X + DOWN * 2.3)
        finalx  = MathTex("x' = A(x - vt)").scale(MSCALE).move_to(MATH_X + DOWN * 2.3)

        self.play(Write(derive1))
        self.wait(2)
        self.play(Transform(derive1, derive2))
        self.wait(2)
        self.play(Transform(derive1, derive3))
        self.wait(3)
        self.play(Transform(derive1, finalx))
        self.wait(4)

        self.play(FadeOut(cond), FadeOut(general), FadeOut(derive1), FadeOut(title))

        # ─────────────────────────────────────────────────────────────────────
        # LIGHT POSTULATE
        # ─────────────────────────────────────────────────────────────────────
        light_title = right_title("Light moves with speed c in all frames", scale=0.6)

        light = math_vgroup("x = ct", "x' = ct'").move_to(MATH_X + UP * 1.5)

        self.play(Write(light_title))
        self.play(Write(light))
        self.wait(3)

        # ─────────────────────────────────────────────────────────────────────
        # SUBSTITUTE INTO TRANSFORM
        # step1 and step3 sit below 'light'; condlight at the very bottom.
        # ─────────────────────────────────────────────────────────────────────
        step1 = MathTex("x' = A(ct - vt)").scale(MSCALE).move_to(MATH_X + UP * 0.4)
        step2 = MathTex("x' = At(c - v)").scale(MSCALE).move_to(MATH_X + UP * 0.4)
        step3 = MathTex("t' = t(Dc + E)").scale(MSCALE).move_to(MATH_X - UP * 0.4)

        self.play(Write(step1))
        self.wait(2)
        self.play(Transform(step1, step2))
        self.wait(2)
        self.play(Write(step3))
        self.wait(3)

        condlight = MathTex("x' = ct'").scale(MSCALE).move_to(MATH_X + DOWN * 1.3)
        self.play(Write(condlight))
        self.wait(3)

        # FIX: fade step1, step3 AND condlight together before eq1/eq2 appear
        # (condlight at y=-1.3 collides with eq2 at y=-1.1 if left alive)
        self.play(FadeOut(step1), FadeOut(step3), FadeOut(condlight))

        eq1 = MathTex("A(c-v) = c(Dc + E)").scale(MSCALE).move_to(MATH_X + DOWN * 0.3)
        eq2 = MathTex("-A(c+v) = c(-Dc + E)").scale(MSCALE).move_to(MATH_X + DOWN * 1.1)

        self.play(Write(eq1), Write(eq2))
        self.wait(4)

        # ─────────────────────────────────────────────────────────────────────
        # SOLVE EQUATIONS
        # FIX: fade light + light_title BEFORE showing solving block.
        # light sits at y=+1.5 and solving top reaches y≈+1.3 — too close.
        # Clearing light first gives the solving block a completely clean field.
        # ─────────────────────────────────────────────────────────────────────
        self.play(FadeOut(light), FadeOut(light_title))

        solving = math_vgroup(
            "-2Av = 2cE",
            "E = -\\frac{Av}{c}",
            "2Ac = 2cDc",
            "D = \\frac{A}{c}",
        ).move_to(MATH_X + DOWN * 0.55)   # shifted lower → well clear of top

        eqs = VGroup(eq1, eq2)
        self.play(Transform(eqs, solving))
        self.wait(5)

        self.play(FadeOut(eqs))

        # ─────────────────────────────────────────────────────────────────────
        # SYMMETRY STEP
        # ─────────────────────────────────────────────────────────────────────
        sym    = right_title("Symmetry between frames")
        gamma1 = MathTex(
            "A = \\frac{1}{\\sqrt{1 - v^2/c^2}}"
        ).scale(MSCALE).move_to(MATH_X)

        self.play(Write(sym))
        self.play(Write(gamma1))
        self.wait(5)

        # ─────────────────────────────────────────────────────────────────────
        # DEFINE GAMMA
        # ─────────────────────────────────────────────────────────────────────
        gamma_title = right_title("Lorentz Factor")
        gamma = MathTex(
            "\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}"
        ).scale(MSCALE).move_to(MATH_X)

        self.play(FadeOut(sym), FadeOut(gamma1))
        self.play(Write(gamma_title))
        self.play(Write(gamma))
        self.wait(4)

        # ─────────────────────────────────────────────────────────────────────
        # FINAL TRANSFORMATIONS
        # ─────────────────────────────────────────────────────────────────────
        final = math_vgroup(
            "x' = \\gamma(x - vt)",
            "t' = \\gamma\\left(t - \\frac{vx}{c^2}\\right)",
        ).move_to(MATH_X)

        self.play(FadeOut(gamma), FadeOut(gamma_title))
        self.play(Write(final))
        self.wait(4)

        # ─────────────────────────────────────────────────────────────────────
        # SIGNIFICANCE OF GAMMA
        # ─────────────────────────────────────────────────────────────────────
        significance_title = right_title("Where γ appears in Relativity")

        formulas = math_vgroup(
            "t' = \\gamma t",
            "L = \\frac{L_0}{\\gamma}",
            "E = \\gamma mc^2",
            "p = \\gamma mv",
        ).move_to(MATH_X)

        self.play(FadeOut(final))
        self.play(Write(significance_title))
        self.play(Write(formulas))
        self.wait(6)

        # ─────────────────────────────────────────────────────────────────────
        # CONCLUSION — fully clean background
        # Fade every object (including the persistent axes/labels) before
        # showing the final text centred on screen.
        # ─────────────────────────────────────────────────────────────────────
        self.play(FadeOut(*self.mobjects))
        self.wait(0.3)

        conclusion = Text("This was the Lorentz Transformation").scale(0.8)
        self.play(Write(conclusion))
        self.wait(4)