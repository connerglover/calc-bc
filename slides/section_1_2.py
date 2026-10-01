"""Section 1.2 -- Combining Functions; Shifting and Scaling Graphs.

Render:   manim-slides render section_1_2.py Section1_2
Present:  manim-slides present Section1_2
"""

from common import *


class Section1_2(Lesson):
    def construct(self):
        self.title_card(
            "1.2", "Combining Functions; Shifting and Scaling Graphs",
            "Arithmetic of functions, composition, and transformations",
        )
        self.arithmetic_rules()
        self.graphical_addition()
        self.combine_example()
        self.composition_machine()
        self.composition_example()
        self.composition_table_example()
        self.vertical_shift()
        self.horizontal_shift()
        self.shift_example()
        self.vertical_scaling()
        self.horizontal_scaling()
        self.reflections()
        self.scaling_example()
        self.combined_transform_example()
        self.recap()

    # -------------------------------------------------- combining -----------
    def arithmetic_rules(self):
        h = self.heading("Sums, Differences, Products, and Quotients")
        sub = note(r"Combine two functions by combining their outputs at each $x$.")
        sub.next_to(h, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(sub))
        data = [
            (r"(f + g)(x) = f(x) + g(x)", r"D(f) \cap D(g)"),
            (r"(f - g)(x) = f(x) - g(x)", r"D(f) \cap D(g)"),
            (r"(f g)(x) = f(x)\, g(x)", r"D(f) \cap D(g)"),
            (r"\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}", r"D(f) \cap D(g),\ g(x) \ne 0"),
            (r"(c f)(x) = c\, f(x)", r"D(f)"),
        ]
        tbl = MathTable(
            [[a, b] for a, b in data],
            col_labels=[Tex("Formula", color=YELLOW), Tex("Domain", color=YELLOW)],
            include_outer_lines=True,
            line_config={"stroke_width": 1.5, "color": MUTED},
            element_to_mobject_config={"font_size": 36},
            v_buff=0.3, h_buff=0.8,
        ).scale(0.85).next_to(sub, DOWN, buff=0.4).set_x(0)
        self.play(Create(tbl.get_horizontal_lines()), Create(tbl.get_vertical_lines()),
                  Write(tbl.get_col_labels()))
        rows = tbl.get_rows()
        for r in rows[1:]:
            self.play(Write(r), run_time=0.9)
            self.pause()
        cap = note(r"Left side: an operation on \emph{functions}. Right side: ordinary arithmetic on the \emph{numbers} $f(x)$ and $g(x)$.", fs=26)
        cap.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(cap))
        self.pause()

    def graphical_addition(self):
        h = self.topic("Adding Functions Graphically")
        sub = note(r"At each $x$, stack the height $g(x)$ on top of $f(x)$.")
        sub.next_to(h, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(sub))
        ax = make_axes([-2, 4, 1], [0, 4, 1], 9.0, 4.8).next_to(sub, DOWN, buff=0.3).set_x(0)
        f = lambda x: np.sqrt(x + 1)
        g = lambda x: np.sqrt(3 - x)
        F = plot_clip(ax, f, -1, 3.8, color=FUNC)
        G = plot_clip(ax, g, -1.8, 3, color=ALT)
        fl = MathTex(r"f(x) = \sqrt{x + 1}", color=FUNC, font_size=32).next_to(ax.c2p(3.8, 2.2), UP)
        gl = MathTex(r"g(x) = \sqrt{3 - x}", color=ALT, font_size=32).next_to(ax.c2p(-1.8, 2.2), UP)
        self.play(Create(ax))
        self.play(Create(F), Write(fl))
        self.play(Create(G), Write(gl))
        self.pause()

        t = ValueTracker(-1)

        def bars():
            x = t.get_value()
            base, a, b = ax.c2p(x, 0), ax.c2p(x, f(x)), ax.c2p(x, f(x) + g(x))
            return VGroup(Line(base, a, color=FUNC, stroke_width=6),
                          Line(a, b, color=ALT, stroke_width=6),
                          Dot(b, color=YELLOW))

        B = always_redraw(bars)
        dot = always_redraw(lambda: Dot(ax.c2p(t.get_value(), f(t.get_value()) + g(t.get_value())), color=YELLOW))
        trace = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=4)
        self.add(B, dot, trace)
        self.play(t.animate.set_value(1), run_time=2, rate_func=linear)
        self.pause()
        self.play(t.animate.set_value(3), run_time=2.5, rate_func=linear)
        sl = MathTex(r"(f + g)(x)", color=YELLOW, font_size=32).next_to(ax.c2p(1, 2.83), UP)
        self.play(Write(sl))
        self.pause()
        B.clear_updaters()
        self.play(FadeOut(B))
        dom = axis_interval(ax, -1, 3, "x", INPUT)
        why = note(r"$f + g$ only exists where \emph{both} are defined: $[-1, 3]$.", fs=28).next_to(ax, DOWN, buff=0.15)
        self.play(FadeIn(dom), FadeIn(why))
        self.pause()

    def combine_example(self):
        h = self.topic("Combining Functions: Domains")
        self.example_tag("Example 1")
        prob = MathTex(r"f(x) = \sqrt{x + 1},\quad g(x) = \sqrt{3 - x}", font_size=40)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        self.pause()

        nl = NumberLine(x_range=[-3, 5, 1], length=6.5, include_numbers=True, font_size=24, color=MUTED)
        nl.to_corner(UR, buff=0.4).shift(DOWN * 1.6)

        def ray(a, b, col, closed, dy):
            lo = nl.n2p(-3 if a is None else a) + UP * dy
            hi = nl.n2p(5 if b is None else b) + UP * dy
            g = VGroup(Line(lo, hi, color=col, stroke_width=7))
            if a is not None:
                g.add(endpoint(lo, closed[0], col))
            if b is not None:
                g.add(endpoint(hi, closed[1], col))
            return g

        steps = stack(
            row(r"x + 1 \ge 0 \Rightarrow D(f) = [-1, \infty)", color=FUNC, fs=36),
            row(r"3 - x \ge 0 \Rightarrow D(g) = (-\infty, 3]", color=ALT, fs=36),
            row(r"D(f) \cap D(g) = [-1, 3]", r"where both are defined", fs=36),
            buff=0.3,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Create(nl))
        self.step(steps[0], FadeIn(ray(-1, None, FUNC, (True, True), 0.45)))
        self.step(steps[1], FadeIn(ray(None, 3, ALT, (True, True), 0.75)))
        self.step(steps[2], FadeIn(ray(-1, 3, YELLOW, (True, True), 0)))
        self.pause()

        tbl = stack(
            row(r"(f + g)(x) = \sqrt{x+1} + \sqrt{3-x}", r"$[-1, 3]$", fs=34),
            row(r"(f g)(x) = \sqrt{(x+1)(3-x)}", r"$[-1, 3]$", fs=34),
            row(r"\left(\tfrac{f}{g}\right)(x) = \dfrac{\sqrt{x+1}}{\sqrt{3-x}}", r"$[-1, 3)$ \ since $g(3) = 0$", fs=34),
            row(r"\left(\tfrac{g}{f}\right)(x) = \dfrac{\sqrt{3-x}}{\sqrt{x+1}}", r"$(-1, 3]$ \ since $f(-1) = 0$", fs=34),
            buff=0.28, max_width=12.5,
        ).next_to(steps, DOWN, aligned_edge=LEFT, buff=0.45)
        for r in tbl:
            self.step(r)
        self.box(tbl[2][1], tbl[3][1])

        h = self.topic("Combining Functions: Evaluating")
        self.example_tag("Example 1 (cont.)")
        prob = MathTex(r"f(x) = \sqrt{x + 1},\quad g(x) = \sqrt{3 - x}", font_size=40)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(prob))
        ev = stack(
            row(r"(f + g)(0) = \sqrt{0 + 1} + \sqrt{3 - 0}"),
            row(r"= 1 + \sqrt{3} \approx 2.73", color=ANSWER),
            row(r"(f g)(1) = \sqrt{1 + 1}\cdot\sqrt{3 - 1}"),
            row(r"= \sqrt{2}\cdot\sqrt{2} = 2", color=ANSWER),
            row(r"\left(\tfrac{f}{g}\right)(3) = \dfrac{\sqrt{4}}{\sqrt{0}}", r"undefined: $3$ is not in $D(f/g)$"),
            buff=0.32,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        for r in ev:
            self.step(r)
        ax = make_axes([-2, 4, 1], [0, 3, 1], 4.8, 3.0, fs=18).to_corner(DR, buff=0.4)
        prod = plot_clip(ax, lambda x: np.sqrt((x + 1) * (3 - x)), -1, 3, color=YELLOW)
        pl = note(r"Bonus: $y = (fg)(x)$ is a semicircle,\\since $(x+1)(3-x) = 4 - (x-1)^2$.", fs=24).next_to(ax, UP, buff=0.1)
        self.play(Create(ax), Create(prod), FadeIn(pl))
        self.pause()

    # -------------------------------------------------- composition ---------
    def composition_machine(self):
        h = self.topic("Composing Functions")
        body = MathTex(r"(f \circ g)(x) = f\big(g(x)\big)", font_size=48)
        card = framed(body, "Definition").next_to(h, DOWN, buff=0.6).set_x(0)
        self.play(FadeIn(card[0]), Write(card[1]), Write(body))
        nt = note(r"Read ``$f$ of $g$ of $x$'': do $g$ \emph{first}, then feed its output into $f$.").next_to(card, DOWN)
        self.play(FadeIn(nt))
        self.pause()

        def machine(label, col):
            b = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.2, color=col).set_fill(col, 0.15)
            return VGroup(b, MathTex(label, font_size=34).move_to(b))

        G = machine(r"g(x) = x - 3", ALT)
        F = machine(r"f(x) = \sqrt{x}", FUNC)
        VGroup(G, F).arrange(RIGHT, buff=2.4).shift(DOWN * 1.6)
        a0 = Arrow(G.get_left() + LEFT * 1.6, G.get_left(), buff=0.05, color=MUTED)
        a1 = Arrow(G.get_right(), F.get_left(), buff=0.05, color=MUTED)
        a2 = Arrow(F.get_right(), F.get_right() + RIGHT * 1.6, buff=0.05, color=MUTED)
        self.play(FadeIn(G), FadeIn(F), GrowArrow(a0), GrowArrow(a1), GrowArrow(a2))
        lbls = VGroup(
            MathTex("x", color=INPUT, font_size=32).next_to(a0, UP, buff=0.1),
            MathTex("g(x)", color=ALT, font_size=32).next_to(a1, UP, buff=0.1),
            MathTex("f(g(x))", color=OUTPUT, font_size=32).next_to(a2, UP, buff=0.1),
        )
        self.play(FadeIn(lbls))
        self.pause()
        x = MathTex("7", color=INPUT, font_size=44).next_to(a0, LEFT)
        self.play(FadeIn(x))
        self.play(FadeOut(x, target_position=G.get_center(), scale=0.3), Indicate(G, color=ALT, scale_factor=1.05))
        mid = MathTex("4", color=ALT, font_size=44).next_to(a1, DOWN, buff=0.15)
        self.play(FadeIn(mid, target_position=G.get_center(), scale=0.3))
        self.pause()
        self.play(FadeOut(mid.copy(), target_position=F.get_center(), scale=0.3), Indicate(F, color=FUNC, scale_factor=1.05))
        out = MathTex("2", color=OUTPUT, font_size=44).next_to(a2, RIGHT)
        self.play(FadeIn(out, target_position=F.get_center(), scale=0.3))
        res = MathTex(r"(f \circ g)(7) = f(g(7)) = f(4) = \sqrt{4} = 2", font_size=38).to_edge(DOWN, buff=0.4)
        self.play(Write(res))
        self.pause()
        dom = note(r"Domain of $f \circ g$: the $x$ in $D(g)$ whose output $g(x)$ lands in $D(f)$.", fs=28)
        dom.next_to(res, UP, buff=0.25)
        self.play(FadeIn(dom))
        self.pause()

    def composition_example(self):
        h = self.topic("Finding Compositions")
        self.example_tag("Example 2")
        prob = MathTex(r"f(x) = \sqrt{x},\quad g(x) = x - 3.\quad \text{Find each composition and its domain.}", font_size=36)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        self.pause()
        parts = [
            [row(r"(a)\ (f \circ g)(x) = f(x - 3) = \sqrt{x - 3}", fs=36),
             row(r"x - 3 \ge 0 \Rightarrow [3, \infty)", r"$g(x)$ must be $\ge 0$ for $\sqrt{\ }$", fs=34, color=INPUT)],
            [row(r"(b)\ (g \circ f)(x) = g(\sqrt{x}) = \sqrt{x} - 3", fs=36),
             row(r"x \ge 0 \Rightarrow [0, \infty)", r"$x$ must be in $D(f)$ first", fs=34, color=INPUT)],
            [row(r"(c)\ (f \circ f)(x) = \sqrt{\sqrt{x}} = x^{1/4}", fs=36),
             row(r"[0, \infty)", fs=34, color=INPUT)],
            [row(r"(d)\ (g \circ g)(x) = (x - 3) - 3 = x - 6", fs=36),
             row(r"(-\infty, \infty)", fs=34, color=INPUT)],
        ]
        body = stack(*[stack(*p, buff=0.12) for p in parts], buff=0.35, max_width=12.6)
        body.next_to(prob, DOWN, aligned_edge=LEFT, buff=0.45)
        for p in body:
            for r in p:
                self.step(r)
        warn = Tex(r"$f \circ g \ne g \circ f$ \ in general!", font_size=36, color=WARN).to_corner(DR, buff=0.5)
        self.play(Write(warn), Indicate(body[0][0]), Indicate(body[1][0]))
        self.pause()

        h = self.topic("A Domain Trap")
        self.example_tag("Example 3")
        prob = MathTex(r"f(x) = x^2,\quad g(x) = \sqrt{x}.\quad \text{Find } (f \circ g)(x) \text{ and its domain.}", font_size=36)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        steps = stack(
            row(r"(f \circ g)(x) = f(\sqrt{x}) = (\sqrt{x})^2 = x"),
            row(r"\text{but } g(x) = \sqrt{x} \text{ needs } x \ge 0", r"the inside function is evaluated first"),
            row(r"D(f \circ g) = [0, \infty), \text{ not } (-\infty, \infty)", color=ANSWER),
            buff=0.35,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        for s in steps:
            self.step(s)
        ax = make_axes([-3, 3, 1], [-1, 3, 1], 5.0, 3.0, fs=18).to_corner(DR, buff=0.4)
        g = plot_clip(ax, lambda x: x, 0, 2.9, color=ANSWER)
        ghost = DashedVMobject(plot_clip(ax, lambda x: x, -1, 0, color=MUTED, stroke_width=2)[0], num_dashes=10)
        self.play(Create(ax), Create(g), Create(ghost), FadeIn(endpoint(ax.c2p(0, 0), True, ANSWER)))
        self.pause()

    def composition_table_example(self):
        h = self.topic("Compositions from a Table")
        self.example_tag("Example 4")
        xs = [0, 1, 2, 3, 4]
        fv = [2, 4, 1, 3, 0]
        gv = [3, 0, 4, 1, 2]
        top, xc, fc = value_table(xs, fv, y_label="f(x)", cell_w=1.0)
        gt, _, gc = value_table(xs, gv, y_label="g(x)", cell_w=1.0)
        g_row = gt[1]
        g_row[0][0].set_fill(ALT, 0.15)
        g_row[0][1].set_color(ALT)
        tbl = VGroup(top, g_row).arrange(DOWN, buff=0).next_to(h, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(tbl))
        self.pause()
        qs = stack(
            row(r"f(g(2))", fs=40),
            row(r"g(f(2))", fs=40),
            row(r"f(f(1))", fs=40),
            buff=0.5,
        ).next_to(tbl, DOWN, aligned_edge=LEFT, buff=0.6)

        def hl(cell, col):
            return SurroundingRectangle(cell, color=col, buff=0.0, stroke_width=5)

        work = [
            [(gc[2], ALT, r"= f(4)"), (fc[4], FUNC, r"= 0")],
            [(fc[2], FUNC, r"= g(1)"), (gc[1], ALT, r"= 0")],
            [(fc[1], FUNC, r"= f(4)"), (fc[4], FUNC, r"= 0")],
        ]
        for q, steps in zip(qs, work):
            self.play(Write(q))
            self.pause()
            prev = q
            for cell, col, s in steps:
                r = hl(cell, col)
                m = MathTex(s, font_size=40).next_to(prev, RIGHT, buff=0.2)
                self.play(Create(r))
                self.play(Write(m))
                self.play(FadeOut(r))
                prev = m
                self.pause()
            self.play(Create(SurroundingRectangle(prev, color=ANSWER, buff=0.08)))
        tip = note(r"Always work from the inside out.").to_edge(DOWN, buff=0.4)
        self.play(FadeIn(tip))
        self.pause()

    # -------------------------------------------------- shifts ---------------
    def _parabola_board(self, title):
        h = self.topic(title)
        ax = make_axes([-5, 5, 1], [-4, 6, 1], 6.2, 5.6, fs=18).to_corner(DR, buff=0.35)
        base = plot_clip(ax, lambda x: x * x, -2, 2, color=MUTED, stroke_width=3)
        bl = MathTex("y = x^2", font_size=30, color=MUTED).next_to(ax.c2p(2, 4), RIGHT, buff=0.1)
        self.play(Create(ax), Create(base), FadeIn(bl))
        return h, ax, base

    def vertical_shift(self):
        h, ax, base = self._parabola_board("Vertical Shifts")
        rule = framed(stack(
            MathTex(r"y = f(x) + k", font_size=44),
            Tex(r"$k > 0$: shift \textbf{up} $k$ units", font_size=30),
            Tex(r"$k < 0$: shift \textbf{down} $|k|$ units", font_size=30),
            buff=0.2), "Vertical shift", color=PURPLE_B).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(rule))
        self.pause()
        up = base.copy().set_color(FUNC).set_stroke(width=4)
        unit = ax.c2p(0, 1) - ax.c2p(0, 0)
        self.play(up.animate.shift(2 * unit), run_time=1.5)
        ul = MathTex("y = x^2 + 2", font_size=30, color=FUNC).next_to(ax.c2p(-2, 6), LEFT, buff=0.1)
        self.play(Write(ul))
        self.pause()
        down = base.copy().set_color(ALT).set_stroke(width=4)
        self.play(down.animate.shift(-3 * unit), run_time=1.5)
        dl = MathTex("y = x^2 - 3", font_size=30, color=ALT).next_to(ax.c2p(0, -3), DOWN, buff=0.15).shift(RIGHT * 1.3)
        self.play(Write(dl))
        why = note(r"Adding $k$ changes every \emph{output}, so\\every point moves straight up or down.").next_to(rule, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(why))
        self.pause()

    def horizontal_shift(self):
        h, ax, base = self._parabola_board("Horizontal Shifts")
        rule = framed(stack(
            MathTex(r"y = f(x + h)", font_size=44),
            Tex(r"$h > 0$: shift \textbf{left} $h$ units", font_size=30),
            Tex(r"$h < 0$: shift \textbf{right} $|h|$ units", font_size=30),
            buff=0.2), "Horizontal shift", color=PURPLE_B).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(rule))
        self.pause()
        unit = ax.c2p(1, 0) - ax.c2p(0, 0)
        left = base.copy().set_color(FUNC).set_stroke(width=4)
        self.play(left.animate.shift(-3 * unit), run_time=1.5)
        ll = MathTex("y = (x + 3)^2", font_size=30, color=FUNC).move_to(ax.c2p(-3, -1.4))
        self.play(Write(ll))
        self.pause()
        right = base.copy().set_color(ALT).set_stroke(width=4)
        self.play(right.animate.shift(2 * unit), run_time=1.5)
        rl = MathTex("y = (x - 2)^2", font_size=30, color=ALT).move_to(ax.c2p(2.6, -1.4))
        self.play(Write(rl))
        self.pause()
        why = stack(
            Tex(r"Why ``$+$'' moves \emph{left}:", font_size=30, color=YELLOW),
            note(r"the vertex of $(x+3)^2$ is where the inside is $0$:"),
            MathTex(r"x + 3 = 0 \Rightarrow x = -3", font_size=34),
            buff=0.15,
        ).next_to(rule, DOWN, aligned_edge=LEFT, buff=0.45)
        self.play(FadeIn(why))
        self.play(Flash(ax.c2p(-3, 0), color=YELLOW))
        self.pause()

    def shift_example(self):
        h = self.topic("Shifting: Example")
        self.example_tag("Example 5")
        prob = Tex(r"Describe and graph $y = \sqrt{x + 3} - 2$ starting from $y = \sqrt{x}$.", font_size=34)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes([-4, 6, 1], [-3, 3, 1], 6.2, 4.6, fs=18).to_corner(DR, buff=0.35)
        base = plot_clip(ax, lambda x: np.sqrt(x), 0, 6, color=MUTED, stroke_width=3)
        bl = MathTex(r"y = \sqrt{x}", font_size=28, color=MUTED).next_to(ax.c2p(6, np.sqrt(6)), UP, buff=0.1)
        self.play(Create(ax), Create(base), FadeIn(bl))
        p = Dot(ax.c2p(0, 0), color=YELLOW, radius=0.1)
        pl = MathTex("(0, 0)", font_size=26, color=YELLOW).next_to(p, UR, buff=0.05)
        self.play(FadeIn(p), FadeIn(pl))
        self.pause()
        ux = ax.c2p(1, 0) - ax.c2p(0, 0)
        uy = ax.c2p(0, 1) - ax.c2p(0, 0)
        steps = stack(
            row(r"x + 3 \text{ inside}", r"$h = 3 > 0$: \textbf{left} 3"),
            row(r"-2 \text{ outside}", r"$k = -2 < 0$: \textbf{down} 2"),
            row(r"(0, 0) \to (-3, 0) \to (-3, -2)", r"track the starting point"),
            buff=0.35, max_width=6.2,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        g = base.copy().set_color(FUNC).set_stroke(width=4)
        self.add(g)
        self.step(steps[0], g.animate.shift(-3 * ux), p.animate.shift(-3 * ux), FadeOut(pl))
        self.step(steps[1], g.animate.shift(-2 * uy), p.animate.shift(-2 * uy))
        self.step(steps[2], FadeIn(MathTex("(-3, -2)", font_size=26, color=YELLOW).next_to(p, DL, buff=0.05)))
        fl = MathTex(r"y = \sqrt{x + 3} - 2", font_size=30, color=FUNC).move_to(ax.c2p(3.6, -1.4))
        self.play(Write(fl))
        dr = stack(
            row(r"D = [-3, \infty)", color=INPUT, fs=36),
            row(r"R = [-2, \infty)", color=OUTPUT, fs=36),
            buff=0.2,
        ).next_to(steps, DOWN, aligned_edge=LEFT, buff=0.45)
        self.step(dr, FadeIn(axis_interval(ax, -3, None, "x", INPUT)), FadeIn(axis_interval(ax, -2, None, "y", OUTPUT)))
        self.pause()

        h = self.topic("Shifting: Writing the Equation")
        self.example_tag("Example 6")
        prob = Tex(r"Shift $y = x^2$ right 4 units and up 1 unit. Write the new equation.", font_size=34)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        steps = stack(
            row(r"y = (x - 4)^2", r"right 4: replace $x$ with $x - 4$"),
            row(r"y = (x - 4)^2 + 1", r"up 1: add $1$ to the output", color=ANSWER),
            row(r"\text{vertex: } (0, 0) \to (4, 1)", fs=34),
            buff=0.35,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        ax = make_axes([-2, 7, 1], [-1, 6, 1], 5.4, 4.2, fs=18).to_corner(DR, buff=0.35)
        b = plot_clip(ax, lambda x: x * x, -2, 2.2, color=MUTED, stroke_width=3)
        self.play(Create(ax), Create(b))
        g = b.copy().set_color(FUNC).set_stroke(width=4)
        self.add(g)
        ux = ax.c2p(1, 0) - ax.c2p(0, 0)
        uy = ax.c2p(0, 1) - ax.c2p(0, 0)
        self.step(steps[0], g.animate.shift(4 * ux))
        self.step(steps[1], g.animate.shift(uy))
        self.step(steps[2], FadeIn(Dot(ax.c2p(4, 1), color=YELLOW)))
        self.box(steps[1])

    # -------------------------------------------------- scaling --------------
    def _root_board(self, title, y_range=(-1, 5, 1)):
        h = self.topic(title)
        ax = make_axes([-1, 9, 1], list(y_range), 6.4, 4.8, fs=18).to_corner(DR, buff=0.35)
        base = plot_clip(ax, lambda x: np.sqrt(x), 0, 9, color=MUTED, stroke_width=3)
        bl = MathTex(r"y = \sqrt{x}", font_size=28, color=MUTED).next_to(ax.c2p(9, 3), DOWN, buff=0.1)
        self.play(Create(ax), Create(base), FadeIn(bl))
        return h, ax, base

    def vertical_scaling(self):
        h, ax, base = self._root_board("Vertical Stretch and Compression", (-1, 7, 1))
        rule = framed(stack(
            Tex(r"For $c > 1$:", font_size=30),
            MathTex(r"y = c\,f(x)", font_size=40), note(r"stretch vertically by $c$"),
            MathTex(r"y = \tfrac{1}{c}\,f(x)", font_size=40), note(r"compress vertically by $c$"),
            buff=0.15), "Vertical scaling", color=PURPLE_B).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(rule))
        self.pause()
        origin = ax.c2p(0, 0)
        p = Dot(ax.c2p(4, 2), color=YELLOW)
        self.play(FadeIn(p), FadeIn(MathTex("(4, 2)", font_size=24).next_to(p, UP, buff=0.1)))
        s = base.copy().set_color(FUNC).set_stroke(width=4)
        q = p.copy()
        self.play(s.animate.stretch(2, 1, about_point=origin), q.animate.move_to(ax.c2p(4, 4)), run_time=1.5)
        self.play(FadeIn(MathTex(r"y = 2\sqrt{x}", font_size=28, color=FUNC).next_to(ax.c2p(6.2, 2 * np.sqrt(6.2)), LEFT, buff=0.15)),
                  FadeIn(MathTex("(4, 4)", font_size=24, color=FUNC).next_to(q, LEFT, buff=0.1)))
        self.pause()
        c = base.copy().set_color(ALT).set_stroke(width=4)
        r = p.copy()
        self.play(c.animate.stretch(0.5, 1, about_point=origin), r.animate.move_to(ax.c2p(4, 1)), run_time=1.5)
        self.play(FadeIn(MathTex(r"y = \tfrac12\sqrt{x}", font_size=28, color=ALT).next_to(ax.c2p(8, 0.5 * np.sqrt(8)), DOWN, buff=0.15)),
                  FadeIn(MathTex("(4, 1)", font_size=24, color=ALT).next_to(r, DOWN, buff=0.1)))
        rulept = MathTex(r"(x, y) \to (x,\ c\,y)", font_size=34, color=YELLOW).next_to(rule, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(rulept))
        self.pause()

    def horizontal_scaling(self):
        h, ax, base = self._root_board("Horizontal Stretch and Compression")
        rule = framed(stack(
            Tex(r"For $c > 1$:", font_size=30),
            MathTex(r"y = f(c\,x)", font_size=40), note(r"\textbf{compress} horizontally by $c$"),
            MathTex(r"y = f(x / c)", font_size=40), note(r"\textbf{stretch} horizontally by $c$"),
            buff=0.15), "Horizontal scaling", color=PURPLE_B).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(rule))
        self.pause()
        origin = ax.c2p(0, 0)
        p = Dot(ax.c2p(4, 2), color=YELLOW)
        self.play(FadeIn(p), FadeIn(MathTex("(4, 2)", font_size=24).next_to(p, DR, buff=0.05)))
        s = base.copy().set_color(FUNC).set_stroke(width=4)
        q = p.copy()
        self.play(s.animate.stretch(0.5, 0, about_point=origin), q.animate.move_to(ax.c2p(2, 2)), run_time=1.5)
        self.play(FadeIn(MathTex(r"y = \sqrt{2x}", font_size=28, color=FUNC).next_to(ax.c2p(4.5, 3), UP, buff=0.1)),
                  FadeIn(MathTex("(2, 2)", font_size=24, color=FUNC).next_to(q, UL, buff=0.05)))
        self.pause()
        c = base.copy().set_color(ALT).set_stroke(width=4)
        r = p.copy()
        self.play(c.animate.stretch(2, 0, about_point=origin), r.animate.move_to(ax.c2p(8, 2)), run_time=1.5)
        self.play(FadeIn(MathTex(r"y = \sqrt{x/2}", font_size=28, color=ALT).next_to(ax.c2p(8, 2), DOWN, buff=0.2)),
                  FadeIn(MathTex("(8, 2)", font_size=24, color=ALT).next_to(r, UP, buff=0.1)))
        rulept = MathTex(r"y = f(cx):\ (x, y) \to \left(\tfrac{x}{c},\ y\right)", font_size=34, color=YELLOW)
        rulept.next_to(rule, DOWN, aligned_edge=LEFT, buff=0.4)
        why = note(r"Inside changes act ``backwards'':\\$\sqrt{2x}$ reaches $2$ already at $x = 2$.").next_to(rulept, DOWN, aligned_edge=LEFT)
        self.play(Write(rulept), FadeIn(why))
        self.pause()

    def reflections(self):
        h = self.topic("Reflections")
        ax = make_axes([-5, 5, 1], [-3, 3, 1], 6.4, 4.8, fs=18).to_corner(DR, buff=0.35)
        f = lambda x: np.sqrt(x + 1)
        base = plot_clip(ax, f, -1, 5, color=FUNC)
        bl = MathTex(r"y = \sqrt{x + 1}", font_size=28, color=FUNC).next_to(ax.c2p(4, f(4)), UP, buff=0.1)
        self.play(Create(ax), Create(base), Write(bl))
        rule = framed(stack(
            MathTex(r"y = -f(x)", font_size=40), note(r"reflect across the $x$-axis: $(x, y) \to (x, -y)$"),
            MathTex(r"y = f(-x)", font_size=40), note(r"reflect across the $y$-axis: $(x, y) \to (-x, y)$"),
            buff=0.15), "Reflections ($c = -1$)", color=PURPLE_B).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(rule))
        self.pause()
        o = ax.c2p(0, 0)
        rx = base.copy().set_color(ALT)
        self.play(Rotate(rx, PI, axis=RIGHT, about_point=o), run_time=1.8)
        self.play(Write(MathTex(r"y = -\sqrt{x + 1}", font_size=28, color=ALT).next_to(ax.c2p(4, -f(4)), DOWN, buff=0.1)))
        self.pause()
        ry = base.copy().set_color(TEAL)
        self.play(Rotate(ry, PI, axis=UP, about_point=o), run_time=1.8)
        self.play(Write(MathTex(r"y = \sqrt{-x + 1}", font_size=28, color=TEAL).next_to(ax.c2p(-4, f(4)), UP, buff=0.1)))
        self.pause()

    def scaling_example(self):
        f = lambda x: x ** 3 - 3 * x ** 2 + 2
        h = self.topic("Scaling and Reflecting: Example")
        self.example_tag("Example 7")
        prob = para(r"Let $f(x) = x^3 - 3x^2 + 2$. Find a formula for the graph after\\"
                    r"(a) a horizontal compression by a factor of $2$, then a reflection across the $y$-axis.", fs=30)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes([-3, 4, 1], [-6, 6, 2], 5.4, 4.8, fs=18).to_corner(DR, buff=0.3)
        base = plot_clip(ax, f, -1.4, 3.3, color=MUTED, stroke_width=3)
        bl = MathTex(r"y = f(x)", font_size=28, color=MUTED).next_to(ax.c2p(3.3, f(3.3)), LEFT, buff=0.15)
        self.play(Create(ax), Create(base), FadeIn(bl))
        self.pause()
        o = ax.c2p(0, 0)
        steps = stack(
            row(r"y = f(2x)", r"compress: replace $x$ with $2x$"),
            row(r"y = f(-2x)", r"reflect: replace $x$ with $-x$"),
            row(r"= (-2x)^3 - 3(-2x)^2 + 2", r"substitute into $f$"),
            row(r"= -8x^3 - 3(4x^2) + 2"),
            row(r"y = -8x^3 - 12x^2 + 2", color=ANSWER),
            buff=0.28, max_width=6.6,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.4)
        g = base.copy().set_color(FUNC).set_stroke(width=4)
        self.add(g)
        self.step(steps[0], g.animate.stretch(0.5, 0, about_point=o))
        self.step(steps[1], Rotate(g, PI, axis=UP, about_point=o))
        self.step(steps[2])
        self.step(steps[3])
        check = DashedVMobject(plot_clip(ax, lambda x: -8 * x ** 3 - 12 * x ** 2 + 2, -1.7, 0.75, color=YELLOW, stroke_width=3)[0], num_dashes=30)
        self.step(steps[4], Create(check))
        self.box(steps[4])

        h = self.topic("Scaling and Reflecting: Example")
        self.example_tag("Example 7 (cont.)")
        prob = para(r"Let $f(x) = x^3 - 3x^2 + 2$. Find a formula for the graph after\\"
                    r"(b) a vertical compression by a factor of $2$, then a reflection across the $x$-axis.", fs=30)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes([-3, 4, 1], [-6, 6, 2], 5.4, 4.8, fs=18).to_corner(DR, buff=0.3)
        base = plot_clip(ax, f, -1.4, 3.3, color=MUTED, stroke_width=3)
        self.play(Create(ax), Create(base))
        o = ax.c2p(0, 0)
        steps = stack(
            row(r"y = \tfrac12 f(x)", r"compress: multiply the output by $\tfrac12$"),
            row(r"y = -\tfrac12 f(x)", r"reflect: multiply the output by $-1$"),
            row(r"= -\tfrac12\left(x^3 - 3x^2 + 2\right)"),
            row(r"y = -\tfrac12 x^3 + \tfrac32 x^2 - 1", color=ANSWER),
            buff=0.3, max_width=6.6,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.4)
        g = base.copy().set_color(ALT).set_stroke(width=4)
        self.add(g)
        self.step(steps[0], g.animate.stretch(0.5, 1, about_point=o))
        self.step(steps[1], Rotate(g, PI, axis=RIGHT, about_point=o))
        self.step(steps[2])
        check = DashedVMobject(plot_clip(ax, lambda x: -0.5 * f(x), -1.4, 3.3, color=YELLOW, stroke_width=3)[0], num_dashes=30)
        self.step(steps[3], Create(check))
        self.box(steps[3])

    def combined_transform_example(self):
        h = self.topic("Putting It All Together")
        self.example_tag("Example 8")
        prob = Tex(r"Graph $y = -2(x - 1)^2 + 3$ by transforming $y = x^2$.", font_size=34)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes([-3, 5, 1], [-5, 5, 1], 5.6, 5.4, fs=18).to_corner(DR, buff=0.3)
        base = plot_clip(ax, lambda x: x * x, -1.5, 1.5, color=MUTED, stroke_width=3)
        self.play(Create(ax), Create(base))
        o = ax.c2p(0, 0)
        ux = ax.c2p(1, 0) - o
        uy = ax.c2p(0, 1) - o
        g = base.copy().set_color(FUNC).set_stroke(width=4)
        v = Dot(o, color=YELLOW, radius=0.1)
        self.add(g, v)
        self.pause()
        steps = stack(
            row(r"y = (x - 1)^2", r"1. right $1$"),
            row(r"y = 2(x - 1)^2", r"2. stretch vertically by $2$"),
            row(r"y = -2(x - 1)^2", r"3. reflect across the $x$-axis"),
            row(r"y = -2(x - 1)^2 + 3", r"4. up $3$", color=ANSWER),
            buff=0.35, max_width=6.4,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        self.step(steps[0], g.animate.shift(ux), v.animate.shift(ux))
        piv = ax.c2p(1, 0)
        self.step(steps[1], g.animate.stretch(2, 1, about_point=piv))
        self.step(steps[2], Rotate(g, PI, axis=RIGHT, about_point=piv))
        self.step(steps[3], g.animate.shift(3 * uy), v.animate.shift(3 * uy))
        vt = MathTex(r"\text{vertex } (1, 3)", font_size=28, color=YELLOW).next_to(v, UR, buff=0.1)
        self.play(Write(vt))
        order = note(r"Order tip: do the inside (horizontal) changes,\\then stretch/reflect, then shift up/down last.")
        order.next_to(steps, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(order))
        self.pause()

    def recap(self):
        h = self.topic("Section 1.2 Recap")
        items = BulletedList(
            r"$f \pm g$, $fg$, $f/g$ live on $D(f) \cap D(g)$; for $f/g$ also drop $g(x) = 0$.",
            r"$(f \circ g)(x) = f(g(x))$: inside first. Usually $f \circ g \ne g \circ f$.",
            r"Outside changes ($+k$, $\times c$, $-$) act on $y$ the way you expect.",
            r"Inside changes ($x + h$, $cx$, $-x$) act on $x$ \emph{backwards}.",
            r"Track a key point (vertex, endpoint) through each step.",
            font_size=32, buff=0.3,
        ).next_to(h, DOWN, aligned_edge=LEFT, buff=0.5)
        for it in items:
            self.play(FadeIn(it, shift=RIGHT * 0.2))
        self.pause()
