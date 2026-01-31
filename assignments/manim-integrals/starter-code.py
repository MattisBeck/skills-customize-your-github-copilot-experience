from manim import *

class AreaUnderCurve(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 5, 1],
            axis_config={"color": GREY}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Plot y = x^2
        curve = axes.plot(lambda x: x**2, x_range=[0, 2], color=BLUE)
        curve_label = axes.get_graph_label(curve, label=MathTex("y = x^2"), x_val=2, direction=UR)

        # Area under curve from x=0 to x=2
        area = axes.get_area(curve, x_range=[0, 2], color=[GREEN, YELLOW])

        # Integral value
        integral_value = MathTex(r"\int_0^2 x^2 dx = \frac{8}{3}").to_corner(UR)

        self.play(Create(axes), Write(labels))
        self.play(Create(curve), Write(curve_label))
        self.wait(0.5)
        self.play(FadeIn(area))
        self.wait(0.5)
        self.play(Write(integral_value))
        self.wait(2)
