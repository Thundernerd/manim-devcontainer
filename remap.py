from manim import *

class Remap(Scene):
    def construct(self):
        t = 0.0
        var = Variable(t, Text("t"), num_decimal_places=2)
        var.move_to(UP*2)
        var_tracker = var.tracker

        method = Text("math.remap(0, 1, 5, 15, t);")
        method.scale(0.75)
        method.move_to(UP*1)

        l0 = NumberLine(
            x_range=[0,1, 0.2],
            length=5,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        l0.move_to(DOWN*0.5)

        l1 = NumberLine(
            x_range=[5,15],
            length=10,
            color=GREEN,
            include_numbers=True,
            label_direction=UP,
        )

        l1.move_to(DOWN*1.5)

        self.play(Create(l0), Create(l1), Create(var), Create(method))

        d0 = Dot(color=RED)
        d0.move_to(l0.n2p(0))

        d1 = Dot(color=RED)
        d1.move_to(l1.n2p(5))

        self.play(FadeIn(d0, scale=0.5), FadeIn(d1,scale=0.5))

        t = 1.0
        self.play(d0.animate.move_to(l0.n2p(1)), d1.animate.move_to(l1.n2p(15)), var_tracker.animate.set_value(t))
        self.wait()

        t = 0.2
        self.play(d0.animate.move_to(l0.n2p(0.2)), d1.animate.move_to(l1.n2p(7)), var_tracker.animate.set_value(t))
        self.wait()

        t = 0.5
        self.play(d0.animate.move_to(l0.n2p(0.5)), d1.animate.move_to(l1.n2p(10)), var_tracker.animate.set_value(t))
        self.wait(5)
