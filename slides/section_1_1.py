"""Section 1.1 -- Functions and Their Graphs.

Render:   manim-slides render section_1_1.py Section1_1
Present:  manim-slides present Section1_1
"""

from common import *


class Section1_1(Lesson):
    def construct(self):
        self.title_card(
            "1.1", "Functions and Their Graphs",
            "Domain and range, graphs, symmetry, and the common functions of calculus",
        )
        self.function_machine()
        self.notation_and_mappings()
        self.domain_range_concept()
        self.domain_example_root()
        self.domain_example_reciprocal()
        self.domain_example_semicircle()
        self.graphing()
        self.numerical()
        self.vertical_line_test()
        self.vertical_line_example()
        self.piecewise_intro()
        self.piecewise_example()
        self.floor_function()
        self.increasing_decreasing()
        self.increasing_example()
        self.even_odd()
        self.even_odd_examples()
        self.linear()
        self.linear_example()
        self.power_positive()
        self.power_negative_fractional()
        self.power_example()
        self.polynomials()
        self.rational_example()
        self.other_families()
        self.classify_example()
        self.recap()

    # ---------------------------------------------------------- functions --
    def function_machine(self):
        h = self.heading("What is a function?")
        intro = para(
            r"A function is a rule: put in an input, get out \emph{exactly one} output.",
        ).next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(intro))

        box = RoundedRectangle(width=3, height=1.6, corner_radius=0.2, color=FUNC)
        box.set_fill(FUNC, 0.15).shift(UP * 0.2)
        rule = MathTex("f(x) = x^2", font_size=44).move_to(box)
        a_in = Arrow(box.get_left() + LEFT * 2.6, box.get_left(), buff=0.05, color=MUTED)
        a_out = Arrow(box.get_right(), box.get_right() + RIGHT * 2.6, buff=0.05, color=MUTED)
        lab_in = Tex("input $x$", font_size=30, color=INPUT).next_to(a_in, UP, buff=0.12)
        lab_out = Tex("output $f(x)$", font_size=30, color=OUTPUT).next_to(a_out, UP, buff=0.12)
        self.play(Create(box), Write(rule), GrowArrow(a_in), GrowArrow(a_out),
                  FadeIn(lab_in), FadeIn(lab_out))
        self.pause()

        log = VGroup()
        for xin, yout in [("3", "9"), ("-3", "9"), (r"\tfrac12", r"\tfrac14")]:
            x = MathTex(xin, color=INPUT, font_size=48).next_to(a_in, LEFT, buff=0.25)
            self.play(FadeIn(x, shift=RIGHT * 0.3), run_time=0.5)
            self.play(FadeOut(x, target_position=box.get_center(), scale=0.3),
                      Indicate(box, color=FUNC, scale_factor=1.05), run_time=0.8)
            y = MathTex(yout, color=OUTPUT, font_size=48).next_to(a_out, RIGHT, buff=0.25)
            self.play(FadeIn(y, target_position=box.get_center(), scale=0.3), run_time=0.7)
            entry = MathTex("f(", xin, ") = ", yout, font_size=36)
            entry[1].set_color(INPUT)
            entry[3].set_color(OUTPUT)
            log.add(entry)
            log.arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=1.4)
            self.play(ReplacementTransform(y, entry), run_time=0.7)
            self.pause()

        same = note(r"$3$ and $-3$ share the output $9$ --- that is allowed.").next_to(log, DOWN, buff=0.35)
        self.play(FadeIn(same))
        self.pause()
        never = Tex(r"But one input may \emph{never} produce two different outputs.",
                    font_size=34, color=WARN).next_to(log, DOWN, buff=0.35)
        self.play(ReplacementTransform(same, never))
        self.pause()

    def notation_and_mappings(self):
        h = self.topic("Definition and notation")
        body = para(
            r"A \textbf{function} $f$ from a set $D$ to a set $Y$ is a rule that\\"
            r"assigns a \emph{single} value $f(x)$ in $Y$ to each $x$ in $D$.",
            fs=34,
        )
        card = framed(body, "Definition").next_to(h, DOWN, buff=0.7).set_x(0)
        self.play(FadeIn(card[0]), Write(card[1]), Write(body))
        self.pause()

        eq = MathTex("y", "=", "f", "(", "x", ")", font_size=80).shift(DOWN * 1.2)
        eq[0].set_color(OUTPUT)
        eq[2].set_color(FUNC)
        eq[4].set_color(INPUT)
        self.play(Write(eq))
        b_y = Brace(eq[0], DOWN, color=OUTPUT)
        t_y = Tex("dependent variable\\\\(output)", font_size=28, color=OUTPUT).next_to(b_y, DOWN).align_to(b_y, RIGHT)
        b_x = Brace(eq[4], DOWN, color=INPUT)
        t_x = Tex("independent variable\\\\(input)", font_size=28, color=INPUT).next_to(b_x, DOWN).align_to(b_x, LEFT)
        b_f = Brace(eq[2], UP, color=FUNC)
        t_f = Tex("the rule", font_size=28, color=FUNC).next_to(b_f, UP, buff=0.1)
        self.play(GrowFromCenter(b_x), FadeIn(t_x))
        self.pause()
        self.play(GrowFromCenter(b_y), FadeIn(t_y))
        self.pause()
        self.play(GrowFromCenter(b_f), FadeIn(t_f))
        self.pause()

        # Arrow diagrams: a function vs. not a function.
        self.topic("Arrow diagrams")

        def diagram(pairs, bad=False):
            D = Ellipse(width=2.0, height=3.4, color=INPUT).set_fill(INPUT, 0.08)
            Y = Ellipse(width=2.0, height=3.4, color=OUTPUT).set_fill(OUTPUT, 0.08)
            Y.shift(RIGHT * 3.2)
            dl = MathTex("D", color=INPUT, font_size=36).next_to(D, UP)
            yl = MathTex("Y", color=OUTPUT, font_size=36).next_to(Y, UP)
            ds = VGroup(*[Dot(D.get_center() + UP * (1 - i), color=INPUT) for i in range(3)])
            ys = VGroup(*[Dot(Y.get_center() + UP * (1 - i), color=OUTPUT) for i in range(3)])
            arrows = VGroup(*[
                Arrow(ds[i].get_center(), ys[j].get_center(), buff=0.12,
                      color=WARN if bad and i == 0 else WHITE, stroke_width=3)
                for i, j in pairs
            ])
            return VGroup(D, Y, dl, yl, ds, ys, arrows)

        good = diagram([(0, 0), (1, 0), (2, 2)]).shift(LEFT * 5.2 + DOWN * 0.3)
        bad = diagram([(0, 0), (0, 1), (1, 1), (2, 2)], bad=True).shift(RIGHT * 1.6 + DOWN * 0.3)
        good_t = Tex(r"Function \checkmark", font_size=36, color=OUTPUT).next_to(good, DOWN)
        bad_t = Tex(r"Not a function $\times$", font_size=36, color=WARN).next_to(bad, DOWN)
        self.play(FadeIn(good[:6]))
        self.play(LaggedStart(*[GrowArrow(a) for a in good[6]], lag_ratio=0.4))
        self.play(Write(good_t))
        g_note = note(r"Two inputs may point to\\the same output.", fs=26).next_to(good_t, DOWN)
        self.play(FadeIn(g_note))
        self.pause()
        self.play(FadeIn(bad[:6]))
        self.play(LaggedStart(*[GrowArrow(a) for a in bad[6]], lag_ratio=0.4))
        self.play(Write(bad_t), Indicate(bad[4][0], color=WARN, scale_factor=1.8))
        b_note = note(r"One input points to two outputs.", fs=26).next_to(bad_t, DOWN)
        self.play(FadeIn(b_note))
        self.pause()

    # ----------------------------------------------------- domain / range --
    def domain_range_concept(self):
        h = self.topic("Domain and Range")
        defs = stack(
            para(r"\textbf{Domain} $D(f)$: every allowed input $x$.", fs=30, color=INPUT),
            para(r"\textbf{Range}: every output $f(x)$ the function actually produces.", fs=30, color=OUTPUT),
            para(r"\textbf{Natural domain}: the largest set of real $x$ that give real $y$.", fs=30),
            buff=0.25,
        ).next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        for d in defs:
            self.play(Write(d), run_time=1)
        self.pause()

        ax = make_axes([-1, 7, 1], [-1, 4, 1], 6.2, 3.6).to_corner(DR, buff=0.4)
        f = lambda x: np.sqrt(x) + 1
        g = plot_clip(ax, f, 0, 6.6)
        lab = MathTex(r"y = \sqrt{x} + 1", font_size=34, color=FUNC).next_to(ax.c2p(5, 3.4), UP, buff=0.1)
        self.play(Create(ax), run_time=1)
        self.play(Create(g), Write(lab))
        self.pause()

        x0, y0 = ax.c2p(0, 0)[1], ax.c2p(0, 0)[0]
        shadow_x = g.copy().set_color(INPUT)
        self.play(shadow_x.animate.apply_function(lambda p: np.array([p[0], x0, 0])), run_time=1.5)
        dom = axis_interval(ax, 0, None, "x", INPUT)
        self.play(FadeIn(dom))
        dom_t = MathTex(r"D = [0, \infty)", color=INPUT, font_size=36)
        dom_t.next_to(defs, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(dom_t))
        self.pause()

        shadow_y = g.copy().set_color(OUTPUT)
        self.play(shadow_y.animate.apply_function(lambda p: np.array([y0, p[1], 0])), run_time=1.5)
        rng = axis_interval(ax, 1, None, "y", OUTPUT)
        self.play(FadeIn(rng))
        rng_t = MathTex(r"R = [1, \infty)", color=OUTPUT, font_size=36).next_to(dom_t, DOWN, aligned_edge=LEFT)
        self.play(Write(rng_t))
        self.pause()

        rules = stack(
            Tex(r"Natural-domain red flags:", font_size=30, color=YELLOW),
            Tex(r"$\bullet$ no dividing by $0$", font_size=30),
            Tex(r"$\bullet$ no even roots of negatives", font_size=30),
            buff=0.15,
        ).next_to(rng_t, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(rules, shift=UP * 0.2))
        self.pause()

    def _domain_layout(self, tag, fn_tex, axes_args, axes_shift=RIGHT * 3.5 + DOWN * 0.5):
        h = self.topic("Finding Domain and Range")
        self.example_tag(tag)
        prob = MathTex(r"\text{Find the domain and range of } " + fn_tex, font_size=38)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes(*axes_args).move_to(axes_shift)
        self.pause()
        return prob, ax

    def domain_example_root(self):
        prob, ax = self._domain_layout("Example 1", r"y = \sqrt{x - 3}",
                                       ([-1, 10, 1], [-1, 4, 1], 6.2, 3.8))
        steps = stack(
            row(r"x - 3 \ge 0", r"inside a $\sqrt{\phantom{x}}$ must be $\ge 0$"),
            row(r"x \ge 3"),
            row(r"D = [3, \infty)", color=INPUT),
            row(r"\sqrt{x-3} \ge 0", r"a square root is never negative"),
            row(r"R = [0, \infty)", color=OUTPUT),
            max_width=6.2,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        self.step(steps[0])
        self.step(steps[1])
        self.play(Create(ax))
        g = plot_clip(ax, lambda x: np.sqrt(x - 3), 3, 10)
        self.step(steps[2], FadeIn(axis_interval(ax, 3, None, "x", INPUT)), Create(g))
        self.step(steps[3])
        self.step(steps[4], FadeIn(axis_interval(ax, 0, None, "y", OUTPUT)))
        self.box(steps[2], steps[4])

    def domain_example_reciprocal(self):
        prob, ax = self._domain_layout("Example 2", r"y = \dfrac{1}{x + 2}",
                                       ([-6, 3, 1], [-4, 4, 1], 6.2, 4.6))
        steps = stack(
            row(r"x + 2 \ne 0", r"the denominator can't be $0$"),
            row(r"x \ne -2"),
            row(r"D = (-\infty, -2) \cup (-2, \infty)", color=INPUT),
            row(r"\dfrac{1}{x+2} = 0 \text{ has no solution}"),
            note(r"A fraction is $0$ only when its numerator is $0$,\\and the numerator here is always $1$."),
            row(r"R = (-\infty, 0) \cup (0, \infty)", color=OUTPUT),
            max_width=6.4,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.45)
        self.step(steps[0])
        self.play(Create(ax))
        asym = DashedLine(ax.c2p(-2, -4), ax.c2p(-2, 4), color=MUTED)
        self.step(steps[1], Create(asym))
        g = plot_clip(ax, lambda x: 1 / (x + 2), -6, 3)
        dom = VGroup(axis_interval(ax, None, -2, "x", INPUT, (True, False)),
                     axis_interval(ax, -2, None, "x", INPUT, (False, True)))
        self.step(steps[2], Create(g), FadeIn(dom))
        self.step(VGroup(steps[3], steps[4]))
        h_asym = DashedLine(ax.c2p(-6, 0), ax.c2p(3, 0), color=OUTPUT, stroke_opacity=0.6)
        rng = VGroup(axis_interval(ax, None, 0, "y", OUTPUT, (True, False)),
                     axis_interval(ax, 0, None, "y", OUTPUT, (False, True)))
        self.step(steps[5], FadeIn(rng), Create(h_asym))
        self.box(steps[2], steps[5])

    def domain_example_semicircle(self):
        prob, ax = self._domain_layout("Example 3", r"y = \sqrt{9 - x^2}",
                                       ([-4, 4, 1], [-1, 4, 1], 6.4, 4.0))
        steps = stack(
            row(r"9 - x^2 \ge 0", r"inside must be $\ge 0$"),
            row(r"x^2 \le 9"),
            row(r"-3 \le x \le 3", r"$|x| \le 3$"),
            row(r"D = [-3, 3]", color=INPUT),
            row(r"0 \le 9 - x^2 \le 9", r"biggest at $x=0$, smallest at $x=\pm 3$"),
            row(r"0 \le \sqrt{9 - x^2} \le 3", r"take $\sqrt{\phantom{x}}$ of every part"),
            row(r"R = [0, 3]", color=OUTPUT),
            buff=0.26, max_width=6.3,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.4)
        self.step(steps[0])
        self.step(steps[1])
        self.play(Create(ax))
        self.step(steps[2])
        g = plot_clip(ax, lambda x: np.sqrt(9 - x * x), -3, 3)
        self.step(steps[3], FadeIn(axis_interval(ax, -3, 3, "x", INPUT)), Create(g))
        self.step(steps[4])
        self.step(steps[5])
        self.step(steps[6], FadeIn(axis_interval(ax, 0, 3, "y", OUTPUT)))
        self.box(steps[3], steps[6])

    # ------------------------------------------------------------ graphs --
    def graphing(self):
        h = self.topic("Graphs of Functions")
        defn = MathTex(r"\text{graph of } f = \{\, (x, f(x)) \mid x \in D \,\}", font_size=40)
        defn.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        how = note(r"Plot input--output pairs, then connect them with a smooth curve.")
        how.next_to(defn, DOWN, aligned_edge=LEFT)
        self.play(Write(defn))
        self.play(FadeIn(how))
        self.pause()
        self.example_tag("Example 4")
        prob = Tex(r"Graph $y = 4 - x^2$ on $[-2, 2]$.", font_size=36).next_to(how, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))

        xs = [-2, -1, 0, 1, 2]
        ys = [0, 3, 4, 3, 0]
        table, xc, yc = value_table(xs, ys, cell_w=0.8)
        table.next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        for c in yc:
            c[1].set_opacity(0)
        self.play(FadeIn(table))
        self.pause()

        calc = MathTex(r"y = 4 - (-2)^2 = 4 - 4 = 0", font_size=34).next_to(table, DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(Write(calc), Indicate(xc[0]))
        self.play(yc[0][1].animate.set_opacity(1))
        self.pause()
        calc2 = MathTex(r"y = 4 - (-1)^2 = 4 - 1 = 3", font_size=34).move_to(calc, aligned_edge=LEFT)
        self.play(ReplacementTransform(calc, calc2), Indicate(xc[1]))
        self.play(yc[1][1].animate.set_opacity(1))
        self.pause()
        self.play(*[c[1].animate.set_opacity(1) for c in yc[2:]], FadeOut(calc2))
        self.pause()

        ax = make_axes([-3, 3, 1], [-1, 5, 1], 5.2, 5.0).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        self.play(Create(ax))
        dots = VGroup()
        for i, (x, y) in enumerate(zip(xs, ys)):
            d = Dot(ax.c2p(x, y), color=YELLOW, radius=0.08)
            pair = VGroup(xc[i][1].copy(), yc[i][1].copy())
            self.play(ReplacementTransform(pair, d), run_time=0.6)
            dots.add(d)
        self.pause()
        g = plot_clip(ax, lambda x: 4 - x * x, -2, 2)
        lab = MathTex(r"y = 4 - x^2", font_size=34, color=FUNC).next_to(ax.c2p(1.3, 3.6), RIGHT)
        self.play(Create(g), Write(lab), run_time=1.5)
        self.pause()

    def numerical(self):
        h = self.topic("Representing a Function Numerically")
        txt = para(r"A function can also be given by a \textbf{table of values}.\\"
                   r"Plotting only those points gives a \textbf{scatterplot}.", fs=30)
        txt.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(txt))
        weeks = [0, 1, 2, 3, 4, 5, 6]
        hts = [2, 3.5, 5.5, 8, 10, 13, 15]
        table, xc, yc = value_table(weeks, hts, x_label="t", y_label="h", cell_w=0.72, fs=28)
        table.next_to(txt, DOWN, aligned_edge=LEFT, buff=0.4)
        cap = note(r"Height $h$ (cm) of a plant $t$ weeks after planting", fs=26).next_to(table, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(table), FadeIn(cap))
        self.pause()

        ax = make_axes([0, 7, 1], [0, 16, 2], 5.6, 3.8, x_label="t", y_label="h", fs=20)
        ax.to_corner(DR, buff=0.4)
        self.play(Create(ax))
        dots = VGroup(*[Dot(ax.c2p(t, v), color=YELLOW) for t, v in zip(weeks, hts)])
        self.play(LaggedStart(*[
            ReplacementTransform(VGroup(xc[i][1].copy(), yc[i][1].copy()), dots[i])
            for i in range(len(weeks))
        ], lag_ratio=0.25), run_time=3)
        self.pause()
        model = plot_clip(ax, lambda t: 2 + 1.55 * t + 0.105 * t * t, 0, 6.6, color=FUNC, stroke_width=3)
        model = DashedVMobject(model[0], num_dashes=40)
        m_note = note(r"A smooth curve through the data\\estimates values between weeks.", fs=26)
        m_note.next_to(cap, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Create(model), FadeIn(m_note))
        self.pause()

    # -------------------------------------------------- vertical line test --
    def vertical_line_test(self):
        h = self.topic("The Vertical Line Test")
        rule = para(r"A curve is the graph of a function $\iff$ every vertical line\\"
                    r"crosses it \emph{at most once}.", fs=32)
        rule.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(rule))
        self.pause()

        left = make_axes([-3, 3, 1], [-3, 3, 1], 4.8, 4.2, fs=18).move_to(LEFT * 3.4 + DOWN * 1.1)
        right = make_axes([-3, 3, 1], [-3, 3, 1], 4.8, 4.2, fs=18).move_to(RIGHT * 3.4 + DOWN * 1.1)
        par = plot_clip(left, lambda x: 0.5 * x * x - 2, -3, 3)
        circ = right.plot_parametric_curve(lambda t: (2 * np.cos(t), 2 * np.sin(t)),
                                           t_range=[0, TAU], color=ALT, stroke_width=4)
        pl = MathTex(r"y = \tfrac12 x^2 - 2", font_size=30, color=FUNC).next_to(left, UP, buff=0.05)
        cl = MathTex(r"x^2 + y^2 = 4", font_size=30, color=ALT).next_to(right, UP, buff=0.05)
        self.play(Create(left), Create(right))
        self.play(Create(par), Create(circ), Write(pl), Write(cl))
        self.pause()

        t = ValueTracker(-2.8)
        vl = always_redraw(lambda: DashedLine(left.c2p(t.get_value(), -3), left.c2p(t.get_value(), 3), color=YELLOW))
        vr = always_redraw(lambda: DashedLine(right.c2p(t.get_value(), -3), right.c2p(t.get_value(), 3), color=YELLOW))
        dl = always_redraw(lambda: Dot(left.c2p(t.get_value(), 0.5 * t.get_value() ** 2 - 2), color=YELLOW))

        def circle_dots():
            x = t.get_value()
            if abs(x) >= 2:
                return VGroup()
            y = np.sqrt(4 - x * x)
            return VGroup(Dot(right.c2p(x, y), color=WARN), Dot(right.c2p(x, -y), color=WARN))

        dr = always_redraw(circle_dots)
        cnt_l = always_redraw(lambda: Tex("1 crossing", font_size=30, color=OUTPUT).next_to(left, DOWN, buff=0.15))

        def cnt_r_text():
            n = 2 if abs(t.get_value()) < 2 else 0
            return Tex(f"{n} crossings", font_size=30, color=WARN if n == 2 else MUTED).next_to(right, DOWN, buff=0.15)

        cnt_r = always_redraw(cnt_r_text)
        self.add(vl, vr, dl, dr, cnt_l, cnt_r)
        self.play(t.animate.set_value(2.8), run_time=5, rate_func=linear)
        self.play(t.animate.set_value(0.6), run_time=1.5)
        self.pause()
        verdict_l = Tex(r"Function \checkmark", font_size=34, color=OUTPUT).move_to(pl)
        verdict_r = Tex(r"Not a function $\times$", font_size=34, color=WARN).move_to(cl)
        self.play(ReplacementTransform(pl, verdict_l), ReplacementTransform(cl, verdict_r))
        self.pause()

    def vertical_line_example(self):
        h = self.topic("Vertical Line Test: Algebraically")
        self.example_tag("Example 5")
        prob = Tex(r"Does $x^2 + y^2 = 4$ define $y$ as a function of $x$?", font_size=36)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        self.pause()
        steps = stack(
            row(r"y^2 = 4 - x^2", r"solve for $y$"),
            row(r"y = \pm\sqrt{4 - x^2}", r"$\pm$ means two choices"),
            row(r"x = 0:\quad y = \pm\sqrt{4} = \pm 2", r"test one input"),
            Tex(r"The input $x=0$ gives two outputs, $2$ and $-2$.", font_size=34),
            Tex(r"Not a function of $x$.", font_size=38, color=WARN),
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        for s in steps[:-1]:
            self.step(s)
        self.step(steps[-1], pause=False)
        self.box(steps[-1], color=WARN)
        tip = note(r"Each half, $y = \sqrt{4-x^2}$ or $y = -\sqrt{4-x^2}$, \emph{is} a function on its own.")
        tip.next_to(steps, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(tip))
        self.pause()

    # --------------------------------------------------------- piecewise --
    def piecewise_intro(self):
        h = self.topic("Piecewise-Defined Functions")
        txt = para(r"Different formulas on different parts of the domain --- still \emph{one} function.", fs=30)
        txt.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(txt))
        absdef = MathTex(r"|x| = \begin{cases} -x, & x < 0 \\ \phantom{-}x, & x \ge 0 \end{cases}", font_size=44)
        absdef.next_to(txt, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(absdef))
        ax = make_axes([-3, 3, 1], [-1, 3, 1], 5.6, 3.8).to_corner(DR, buff=0.5)
        self.play(Create(ax))
        left = plot_clip(ax, lambda x: -x, -3, 0, color=ALT)
        right = plot_clip(ax, lambda x: x, 0, 3, color=FUNC)
        self.play(Indicate(absdef[0][5:10], color=ALT), Create(left))
        self.play(Indicate(absdef[0][11:], color=FUNC), Create(right))
        self.pause()

    def piecewise_example(self):
        h = self.topic("Graphing and Evaluating a Piecewise Function")
        self.example_tag("Example 6")
        f = MathTex(r"f(x) = \begin{cases} x + 3, & x < -1 \\ x^2, & -1 \le x < 2 \\ 1, & x \ge 2 \end{cases}",
                    font_size=40).next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(f))
        ax = make_axes([-5, 5, 1], [-2, 5, 1], 6.4, 4.6).to_corner(DR, buff=0.35)
        self.play(Create(ax))
        self.pause()

        pieces = [
            (lambda x: x + 3, -5, -1, FUNC, [(-1, 2, False)], f[0][9:13]),
            (lambda x: x * x, -1, 2, ALT, [(-1, 1, True), (2, 4, False)], f[0][19:22]),
            (lambda x: 1 + 0 * x, 2, 5, TEAL, [(2, 1, True)], f[0][31:32]),
        ]
        full = [(lambda x: x + 3, -5, 2), (lambda x: x * x, -2.2, 2.2), (lambda x: 1 + 0 * x, -5, 5)]
        self.graph_parts = VGroup()
        for (fn, a, b, col, ends, part), (gfn, ga, gb) in zip(pieces, full):
            ghost = DashedVMobject(plot_clip(ax, gfn, ga, gb, color=col, stroke_width=2)[0], num_dashes=40)
            self.play(Indicate(part, color=col), Create(ghost), run_time=1)
            real = plot_clip(ax, fn, a, b, color=col)
            marks = VGroup(*[endpoint(ax.c2p(x, y), c, col) for x, y, c in ends])
            self.play(Create(real), FadeOut(ghost))
            self.play(FadeIn(marks))
            self.graph_parts.add(VGroup(real, marks))
            self.pause()

        rows = stack(
            row(r"f(-3) = -3 + 3 = 0", r"$-3 < -1$: first piece"),
            row(r"f(-1) = (-1)^2 = 1", r"$-1 \le -1 < 2$: second piece"),
            row(r"f(1) = 1^2 = 1", r"second piece"),
            row(r"f(4) = 1", r"$4 \ge 2$: third piece"),
            buff=0.28, max_width=6.2,
        ).next_to(f, DOWN, aligned_edge=LEFT, buff=0.5)
        for r, (x, y) in zip(rows, [(-3, 0), (-1, 1), (1, 1), (4, 1)]):
            d = Dot(ax.c2p(x, y), color=YELLOW, radius=0.1)
            self.step(r, Flash(d, color=YELLOW), FadeIn(d))
        caution = note(r"At $x=-1$ use the piece whose condition contains $-1$:\\the \emph{filled} dot, not the open one.", fs=26)
        caution.next_to(rows, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(caution))
        self.pause()

    def floor_function(self):
        h = self.topic("The Greatest Integer (Floor) Function")
        d = para(r"$\lfloor x \rfloor$ = the greatest integer \emph{less than or equal to} $x$.", fs=32)
        d.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(d))
        ax = make_axes([-3, 4, 1], [-3, 4, 1], 5.4, 5.0).to_corner(DR, buff=0.35)
        self.play(Create(ax))
        steps = VGroup()
        for n in range(-3, 4):
            seg = Line(ax.c2p(n, n), ax.c2p(n + 1, n), color=FUNC, stroke_width=4)
            steps.add(VGroup(seg, endpoint(ax.c2p(n, n), True, FUNC), endpoint(ax.c2p(n + 1, n), False, FUNC)))
        ref = DashedLine(ax.c2p(-3, -3), ax.c2p(4, 4), color=MUTED)
        self.play(LaggedStart(*[FadeIn(s) for s in steps], lag_ratio=0.15), Create(ref))
        self.pause()
        self.example_tag("Example 7")
        rows = stack(
            row(r"\lfloor 2.4 \rfloor = 2"),
            row(r"\lfloor 2 \rfloor = 2", r"already an integer"),
            row(r"\lfloor -0.3 \rfloor = -1", r"$0$ is \emph{above} $-0.3$"),
            row(r"\lfloor -1.2 \rfloor = -2", r"go \emph{down} to the next integer"),
            buff=0.3,
        ).next_to(d, DOWN, aligned_edge=LEFT, buff=0.6)
        for r in rows:
            self.step(r)
        tip = note(r"Think: on a number line, step \emph{left}\\to the nearest integer (or stay put).")
        tip.next_to(rows, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(tip))
        self.pause()

    # ----------------------------------------------- increasing/decreasing --
    def increasing_decreasing(self):
        h = self.topic("Increasing and Decreasing Functions")
        body = para(
            r"Let $x_1 < x_2$ be any two points in an interval $I$.\\"
            r"$\bullet$ \textbf{increasing} on $I$ if $f(x_2) > f(x_1)$ \\"
            r"$\bullet$ \textbf{decreasing} on $I$ if $f(x_2) < f(x_1)$",
            fs=30,
        )
        card = framed(body).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(card[0]), Write(card[1]), Write(body))
        self.pause()

        ax = make_axes([-3, 3, 1], [-4, 4, 2], 5.6, 5.0, fs=18).to_corner(DR, buff=0.35)
        f = lambda x: x ** 3 - 3 * x
        g = plot_clip(ax, f, -2.3, 2.3)
        lab = MathTex(r"y = x^3 - 3x", font_size=30, color=FUNC).next_to(ax.c2p(1.1, -3), RIGHT)
        self.play(Create(ax), Create(g), Write(lab))
        t = ValueTracker(-2.1)
        gap = 0.45

        def pair():
            a, b = t.get_value(), t.get_value() + gap
            pa, pb = ax.c2p(a, f(a)), ax.c2p(b, f(b))
            return VGroup(
                Dot(pa, color=YELLOW), Dot(pb, color=ORANGE),
                DashedLine(pa, ax.c2p(0, f(a)), color=YELLOW, stroke_width=2),
                DashedLine(pb, ax.c2p(0, f(b)), color=ORANGE, stroke_width=2),
            )

        def verdict():
            a = t.get_value()
            up = f(a + gap) > f(a)
            s = r"$f(x_2) > f(x_1)$: increasing" if up else r"$f(x_2) < f(x_1)$: decreasing"
            return Tex(s, font_size=32, color=OUTPUT if up else WARN).next_to(card, DOWN, aligned_edge=LEFT, buff=0.5)

        p = always_redraw(pair)
        v = always_redraw(verdict)
        self.add(p, v)
        self.play(t.animate.set_value(1.6), run_time=7, rate_func=linear)
        self.pause()
        p.clear_updaters()
        v.clear_updaters()
        self.play(FadeOut(p), FadeOut(v))
        inc1 = plot_clip(ax, f, -2.3, -1, color=OUTPUT, stroke_width=7)
        dec = plot_clip(ax, f, -1, 1, color=WARN, stroke_width=7)
        inc2 = plot_clip(ax, f, 1, 2.3, color=OUTPUT, stroke_width=7)
        summary = stack(
            Tex(r"increasing on $(-\infty, -1)$ and $(1, \infty)$", font_size=32, color=OUTPUT),
            Tex(r"decreasing on $(-1, 1)$", font_size=32, color=WARN),
        ).next_to(card, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Create(inc1), Create(inc2), Write(summary[0]))
        self.play(Create(dec), Write(summary[1]))
        self.pause()

    def increasing_example(self):
        h = self.topic("Increasing and Decreasing: Example")
        self.example_tag("Example 8")
        prob = Tex(r"Where is the function from Example 6 increasing or decreasing?", font_size=34)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes([-5, 5, 1], [-2, 5, 1], 6.4, 4.6).to_corner(DR, buff=0.35)
        parts = VGroup(
            plot_clip(ax, lambda x: x + 3, -5, -1, color=MUTED),
            plot_clip(ax, lambda x: x * x, -1, 2, color=MUTED),
            plot_clip(ax, lambda x: 1 + 0 * x, 2, 5, color=MUTED),
        )
        self.play(Create(ax), Create(parts))
        self.pause()
        segs = [
            (plot_clip(ax, lambda x: x + 3, -5, -1, color=OUTPUT, stroke_width=7),
             row(r"(-\infty, -1):\ \text{increasing}", r"line with slope $1$", color=OUTPUT)),
            (plot_clip(ax, lambda x: x * x, -1, 0, color=WARN, stroke_width=7),
             row(r"(-1, 0):\ \text{decreasing}", r"$x^2$ falls to $0$", color=WARN)),
            (plot_clip(ax, lambda x: x * x, 0, 2, color=OUTPUT, stroke_width=7),
             row(r"(0, 2):\ \text{increasing}", r"$x^2$ rises", color=OUTPUT)),
            (plot_clip(ax, lambda x: 1 + 0 * x, 2, 5, color=TEAL, stroke_width=7),
             row(r"(2, \infty):\ \text{neither}", r"constant", color=TEAL)),
        ]
        rows = stack(*[r for _, r in segs], buff=0.35, max_width=6.3).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.6)
        for (curve, _), r in zip(segs, rows):
            self.step(r, Create(curve))
        why = note(r"Constant is neither: the definition needs a \emph{strict} $>$ or $<$.")
        why.next_to(rows, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(why))
        self.pause()

    # ---------------------------------------------------------- even/odd --
    def even_odd(self):
        h = self.topic("Even and Odd Functions: Symmetry")
        body = para(
            r"$\bullet$ \textbf{even} if $f(-x) = f(x)$ \quad (symmetric about the $y$-axis)\\"
            r"$\bullet$ \textbf{odd} if $f(-x) = -f(x)$ \quad (symmetric about the origin)",
            fs=30,
        )
        card = framed(body).next_to(h, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(FadeIn(card[0]), Write(card[1]), Write(body))
        self.pause()

        L = make_axes([-3, 3, 1], [-1, 4, 1], 5.0, 3.4, fs=18).move_to(LEFT * 3.4 + DOWN * 1.9)
        R = make_axes([-3, 3, 1], [-4, 4, 2], 5.0, 3.4, fs=18).move_to(RIGHT * 3.4 + DOWN * 1.9)
        ev = plot_clip(L, lambda x: x * x, -2, 2)
        od = plot_clip(R, lambda x: x ** 3 / 2, -2, 2, color=ALT)
        self.play(Create(L), Create(ev))
        ev_lab = MathTex(r"y = x^2", font_size=30, color=FUNC).next_to(L.c2p(2, 4), RIGHT, buff=0.05)
        self.play(Write(ev_lab))

        t = ValueTracker(1.5)
        pts = always_redraw(lambda: VGroup(
            Dot(L.c2p(t.get_value(), t.get_value() ** 2), color=YELLOW),
            Dot(L.c2p(-t.get_value(), t.get_value() ** 2), color=YELLOW),
            DashedLine(L.c2p(-t.get_value(), t.get_value() ** 2), L.c2p(t.get_value(), t.get_value() ** 2), color=YELLOW, stroke_width=2),
            MathTex("(x, y)", font_size=24).next_to(L.c2p(t.get_value(), t.get_value() ** 2), RIGHT, buff=0.1),
            MathTex("(-x, y)", font_size=24).next_to(L.c2p(-t.get_value(), t.get_value() ** 2), LEFT, buff=0.1),
        ))
        self.add(pts)
        self.play(t.animate.set_value(0.6), run_time=2)
        self.play(t.animate.set_value(1.3), run_time=1.5)
        self.pause()
        mirror = ev.copy().set_color(YELLOW)
        self.play(Rotate(mirror, PI, axis=UP, about_point=L.c2p(0, 0)), run_time=2)
        same = note(r"Flip across the $y$-axis: lands on itself.", fs=26).next_to(L, UP, buff=0.15)
        self.play(FadeIn(same), FadeOut(mirror))
        self.pause()

        self.play(Create(R), Create(od))
        od_lab = MathTex(r"y = \tfrac12 x^3", font_size=30, color=ALT).next_to(R.c2p(2, 4), RIGHT, buff=0.05)
        self.play(Write(od_lab))
        s = ValueTracker(1.6)
        opts = always_redraw(lambda: VGroup(
            Dot(R.c2p(s.get_value(), s.get_value() ** 3 / 2), color=YELLOW),
            Dot(R.c2p(-s.get_value(), -s.get_value() ** 3 / 2), color=YELLOW),
            DashedLine(R.c2p(-s.get_value(), -s.get_value() ** 3 / 2), R.c2p(s.get_value(), s.get_value() ** 3 / 2), color=YELLOW, stroke_width=2),
            MathTex("(x, y)", font_size=24).next_to(R.c2p(s.get_value(), s.get_value() ** 3 / 2), RIGHT, buff=0.1),
            MathTex("(-x, -y)", font_size=24).next_to(R.c2p(-s.get_value(), -s.get_value() ** 3 / 2), LEFT, buff=0.1),
        ))
        self.add(opts)
        self.play(s.animate.set_value(0.8), run_time=2)
        self.play(s.animate.set_value(1.5), run_time=1.5)
        self.pause()
        spin = od.copy().set_color(YELLOW)
        self.play(Rotate(spin, PI, about_point=R.c2p(0, 0)), run_time=2)
        same2 = note(r"Rotate $180^\circ$ about the origin: lands on itself.", fs=26).next_to(R, UP, buff=0.15)
        self.play(FadeIn(same2), FadeOut(spin))
        self.pause()

    def even_odd_examples(self):
        cases = [
            ("Example 9", r"f(x) = x^4 - 3x^2 + 1",
             [row(r"f(-x) = (-x)^4 - 3(-x)^2 + 1", r"replace every $x$ with $-x$"),
              row(r"= x^4 - 3x^2 + 1", r"even powers erase the sign"),
              row(r"= f(x)")],
             Tex(r"Even: symmetric about the $y$-axis", font_size=36, color=OUTPUT),
             lambda x: x ** 4 - 3 * x ** 2 + 1, (-2.2, 2.2), ([-3, 3, 1], [-2, 4, 1])),
            ("Example 10", r"g(x) = x^3 - 5x",
             [row(r"g(-x) = (-x)^3 - 5(-x)", r"replace every $x$ with $-x$"),
              row(r"= -x^3 + 5x", r"odd powers keep the sign"),
              row(r"= -(x^3 - 5x)", r"factor out $-1$"),
              row(r"= -g(x)")],
             Tex(r"Odd: symmetric about the origin", font_size=36, color=OUTPUT),
             lambda x: (x ** 3 - 5 * x) / 2, (-3, 3), ([-3, 3, 1], [-4, 4, 2])),
            ("Example 11", r"h(x) = x^2 + x",
             [row(r"h(-x) = (-x)^2 + (-x)", r"replace every $x$ with $-x$"),
              row(r"= x^2 - x"),
              row(r"x^2 - x \ne x^2 + x = h(x)", r"so not even"),
              row(r"x^2 - x \ne -x^2 - x = -h(x)", r"so not odd")],
             Tex(r"Neither even nor odd", font_size=36, color=WARN),
             lambda x: x * x + x, (-2.3, 1.6), ([-3, 3, 1], [-1, 4, 1])),
        ]
        for tag, fn, rows, verdict, f, (a, b), (xr, yr) in cases:
            h = self.topic("Even, Odd, or Neither?")
            self.example_tag(tag)
            prob = MathTex(r"\text{Is } " + fn + r" \text{ even, odd, or neither?}", font_size=38)
            prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
            self.play(Write(prob))
            self.pause()
            body = stack(*rows, verdict, buff=0.3, max_width=7.6).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
            for r in rows:
                self.step(r)
            ax = make_axes(xr, yr, 4.6, 4.0, fs=18).to_corner(DR, buff=0.4)
            g = plot_clip(ax, f, a, b)
            self.step(verdict, Create(ax), Create(g), pause=False)
            self.box(verdict, color=verdict.get_color())
        tip = note(r"Shortcut for polynomials: only even powers $\Rightarrow$ even;\\"
                   r"only odd powers $\Rightarrow$ odd. (A constant counts as\\"
                   r"an even power: $1 = x^0$.)")
        tip.next_to(body, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(tip))
        self.pause()

    # ---------------------------------------------------------- linear ----
    def linear(self):
        h = self.topic("Linear Functions")
        f = MathTex(r"f(x) = m x + b", font_size=48).next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        f[0][5].set_color(YELLOW)
        f[0][8].set_color(OUTPUT)
        lab = note(r"$m$ = slope, \quad $b$ = $y$-intercept").next_to(f, DOWN, aligned_edge=LEFT)
        self.play(Write(f), FadeIn(lab))

        ax = make_axes([-1, 6, 1], [-1, 6, 1], 5.4, 5.0).to_corner(DR, buff=0.35)
        line = lambda x: 0.5 * x + 1.5
        g = plot_clip(ax, line, -1, 6)
        self.play(Create(ax), Create(g))
        a = ValueTracker(0.5)
        w = ValueTracker(2)

        def tri():
            x1, x2 = a.get_value(), a.get_value() + w.get_value()
            p1, p2, c = ax.c2p(x1, line(x1)), ax.c2p(x2, line(x2)), ax.c2p(x2, line(x1))
            run = Line(p1, c, color=YELLOW)
            rise = Line(c, p2, color=OUTPUT)
            return VGroup(run, rise, Dot(p1), Dot(p2),
                          MathTex(r"\Delta x", font_size=26, color=YELLOW).next_to(run, DOWN, buff=0.08),
                          MathTex(r"\Delta y", font_size=26, color=OUTPUT).next_to(rise, RIGHT, buff=0.08))

        T = always_redraw(tri)
        ratio = MathTex(r"\frac{\Delta y}{\Delta x} = \frac12", font_size=40).next_to(lab, DOWN, aligned_edge=LEFT, buff=0.5)
        self.add(T)
        self.play(Write(ratio))
        self.play(w.animate.set_value(4), run_time=1.5)
        self.play(a.animate.set_value(-0.5), w.animate.set_value(1), run_time=1.5)
        self.play(a.animate.set_value(1.5), w.animate.set_value(3), run_time=1.5)
        same = note(r"Any two points give the same ratio:\\the rate of change is \emph{constant}.").next_to(ratio, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(same))
        self.pause()

        why = stack(
            row(r"\frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{(m x_2 + b) - (m x_1 + b)}{x_2 - x_1}", fs=34),
            row(r"= \frac{m x_2 - m x_1}{x_2 - x_1}", r"the $b$'s cancel", fs=34),
            row(r"= \frac{m (x_2 - x_1)}{x_2 - x_1} = m", r"so does $x_2 - x_1$", fs=34),
            buff=0.25, max_width=7.4,
        ).next_to(same, DOWN, aligned_edge=LEFT, buff=0.35)
        for r in why:
            self.step(r)
        T.clear_updaters()

        self.topic("Two forms of a line")
        si = framed(MathTex(r"y = m x + b", font_size=48), "Slope-intercept form", color=PURPLE_B)
        ps = framed(MathTex(r"y - y_1 = m(x - x_1)", font_size=48), "Point-slope form", color=PURPLE_B)
        VGroup(si, ps).arrange(RIGHT, buff=1.2).shift(UP * 0.6)
        si_n = note(r"use when you know\\the slope and $y$-intercept").next_to(si, DOWN)
        ps_n = note(r"use when you know the slope\\and \emph{any} point $(x_1, y_1)$").next_to(ps, DOWN)
        self.play(FadeIn(si), FadeIn(si_n))
        self.pause()
        self.play(FadeIn(ps), FadeIn(ps_n))
        self.pause()

    def linear_example(self):
        h = self.topic("Writing the Equation of a Line")
        self.example_tag("Example 12")
        prob = Tex(r"Find the line through $(-1, 2)$ and $(3, 10)$.", font_size=36)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        ax = make_axes([-3, 4, 1], [-2, 12, 2], 5.0, 5.4, fs=18).to_corner(DR, buff=0.35)
        P, Q = ax.c2p(-1, 2), ax.c2p(3, 10)
        self.play(Create(ax))
        self.play(FadeIn(Dot(P, color=YELLOW)), FadeIn(Dot(Q, color=YELLOW)),
                  Write(MathTex("(-1, 2)", font_size=26).next_to(P, LEFT)),
                  Write(MathTex("(3, 10)", font_size=26).next_to(Q, LEFT)))
        self.pause()
        steps = stack(
            row(r"m = \frac{10 - 2}{3 - (-1)}", r"rise over run"),
            row(r"m = \frac{8}{4} = 2"),
            row(r"y - 2 = 2\big(x - (-1)\big)", r"point-slope with $(-1, 2)$"),
            row(r"y - 2 = 2x + 2", r"distribute"),
            row(r"y = 2x + 4", r"add $2$", color=ANSWER),
            row(r"\text{Check: } 2(3) + 4 = 10 \ \checkmark", fs=34),
            buff=0.28, max_width=7.0,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.4)
        corner = ax.c2p(3, 2)
        run = Line(P, corner, color=YELLOW)
        rise = Line(corner, Q, color=OUTPUT)
        self.step(steps[0], Create(run), Create(rise),
                  FadeIn(MathTex("4", color=YELLOW, font_size=28).next_to(run, DOWN, buff=0.08)),
                  FadeIn(MathTex("8", color=OUTPUT, font_size=28).next_to(rise, RIGHT, buff=0.08)))
        self.step(steps[1])
        self.step(steps[2])
        self.step(steps[3])
        g = plot_clip(ax, lambda x: 2 * x + 4, -3, 4)
        self.step(steps[4], Create(g))
        self.step(steps[5])
        self.box(steps[4])

    # ----------------------------------------------------------- powers ---
    def power_positive(self):
        h = self.topic(r"Power Functions $f(x) = x^a$")
        sub = note(r"Case 1: $a$ is a positive integer.").next_to(h, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(sub))
        L = make_axes([-2, 2, 1], [-2, 2, 1], 3.8, 3.8, fs=18).move_to(LEFT * 3.3 + DOWN * 0.5)
        R = make_axes([-2, 2, 1], [-2, 2, 1], 3.8, 3.8, fs=18).move_to(RIGHT * 3.3 + DOWN * 0.5)
        lt = Tex(r"odd $a$: $x,\ x^3,\ x^5$", font_size=30).next_to(L, UP, buff=0.1)
        rt = Tex(r"even $a$: $x^2,\ x^4,\ x^6$", font_size=30).next_to(R, UP, buff=0.1)
        self.play(Create(L), Create(R), Write(lt), Write(rt))
        cols = [BLUE, TEAL, GREEN]
        for i, n in enumerate([1, 3, 5]):
            self.play(Create(plot_clip(L, lambda x, n=n: x ** n, -2, 2, color=cols[i])), run_time=0.8)
        for i, n in enumerate([2, 4, 6]):
            self.play(Create(plot_clip(R, lambda x, n=n: x ** n, -2, 2, color=[PINK, RED, ORANGE][i])), run_time=0.8)
        self.pause()
        marks = VGroup(*[Dot(A.c2p(*p), color=YELLOW) for A in (L, R) for p in [(0, 0), (1, 1)]],
                       Dot(L.c2p(-1, -1), color=YELLOW), Dot(R.c2p(-1, 1), color=YELLOW))
        self.play(LaggedStart(*[Flash(m, color=YELLOW) for m in marks], lag_ratio=0.1), FadeIn(marks))
        facts = stack(
            Tex(r"All pass through $(0,0)$ and $(1,1)$. Domain: $(-\infty, \infty)$.", font_size=28),
            Tex(r"Odd $a$: odd function, range $(-\infty, \infty)$. \quad Even $a$: even function, range $[0, \infty)$.", font_size=28),
            Tex(r"Bigger $a$: flatter on $(-1, 1)$, steeper for $|x| > 1$.", font_size=28),
            buff=0.12,
        ).to_edge(DOWN, buff=0.15)
        for fct in facts:
            self.play(FadeIn(fct, shift=UP * 0.2))
            self.pause()

    def power_negative_fractional(self):
        h = self.topic(r"Power Functions $f(x) = x^a$")
        sub = note(r"Case 2: $a$ is a negative integer, so $x^a = 1/x^{-a}$ and $x \ne 0$.").next_to(h, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(sub))
        L = make_axes([-3, 3, 1], [-3, 3, 1], 4.6, 4.4, fs=18).move_to(LEFT * 3.3 + DOWN * 1.0)
        R = make_axes([-3, 3, 1], [-3, 3, 1], 4.6, 4.4, fs=18).move_to(RIGHT * 3.3 + DOWN * 1.0)
        lt = MathTex(r"y = x^{-1} = \tfrac{1}{x}", font_size=30, color=FUNC).next_to(L, UP, buff=0.1)
        rt = MathTex(r"y = x^{-2} = \tfrac{1}{x^2}", font_size=30, color=ALT).next_to(R, UP, buff=0.1)
        self.play(Create(L), Create(R))
        self.play(Write(lt), Create(plot_clip(L, lambda x: 1 / x, -3, 3)))
        ln = note(r"odd; decreasing on each side of $0$", fs=24).next_to(L, DOWN, buff=0.1)
        self.play(FadeIn(ln))
        self.pause()
        self.play(Write(rt), Create(plot_clip(R, lambda x: 1 / x ** 2, -3, 3, color=ALT)))
        rn = note(r"even; range $(0, \infty)$", fs=24).next_to(R, DOWN, buff=0.1)
        self.play(FadeIn(rn))
        self.pause()

        h = self.topic(r"Power Functions $f(x) = x^a$")
        sub = note(r"Case 3: $a = p/q$ in lowest terms, so $x^{p/q} = \left(\sqrt[q]{x}\right)^p$.").next_to(h, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(sub))
        specs = [
            (r"x^{1/2} = \sqrt{x}", lambda x: np.sqrt(x), BLUE, r"$q$ even: $x \ge 0$ only"),
            (r"x^{1/3} = \sqrt[3]{x}", np.cbrt, TEAL, r"$q$ odd: all real $x$"),
            (r"x^{2/3} = (\sqrt[3]{x})^2", lambda x: np.cbrt(x) ** 2, PINK, r"$p$ even: outputs $\ge 0$"),
            (r"x^{3/2} = (\sqrt{x})^3", lambda x: np.sqrt(x) ** 3, ORANGE, r"$q$ even: $x \ge 0$ only"),
        ]
        panels = VGroup()
        for tex_s, fn, col, n in specs:
            A = make_axes([-3, 3, 1], [-2, 3, 1], 3.0, 2.6, numbers=False)
            curve = plot_clip(A, fn, -3, 3, color=col)
            t = MathTex(tex_s, font_size=28, color=col).next_to(A, UP, buff=0.1)
            nn = note(n, fs=22).next_to(A, DOWN, buff=0.1)
            panels.add(VGroup(A, curve, t, nn))
        panels.arrange(RIGHT, buff=0.3).next_to(sub, DOWN, buff=0.5).set_x(0)
        for p in panels:
            self.play(Create(p[0]), Write(p[2]), run_time=0.7)
            self.play(Create(p[1]), FadeIn(p[3]))
            self.pause()

    def power_example(self):
        h = self.topic("Domain and Range of a Power Function")
        self.example_tag("Example 13")
        prob = MathTex(r"\text{Find the domain and range of } f(x) = x^{2/3} \text{ and } g(x) = x^{-1/2}.", font_size=36)
        prob.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        self.pause()
        left = stack(
            row(r"x^{2/3} = \left(\sqrt[3]{x}\right)^2"),
            row(r"\sqrt[3]{x} \text{ works for all } x", fs=34),
            row(r"D = (-\infty, \infty)", color=INPUT),
            row(r"(\cdots)^2 \ge 0", fs=34),
            row(r"R = [0, \infty)", color=OUTPUT),
            buff=0.3,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.5)
        right = stack(
            row(r"x^{-1/2} = \dfrac{1}{\sqrt{x}}"),
            row(r"\sqrt{x} \text{ needs } x \ge 0;\ \text{denominator needs } x \ne 0", fs=30),
            row(r"D = (0, \infty)", color=INPUT),
            row(r"\sqrt{x} > 0 \Rightarrow \tfrac{1}{\sqrt{x}} > 0", fs=34),
            row(r"R = (0, \infty)", color=OUTPUT),
            buff=0.3,
        ).next_to(prob, DOWN, buff=0.5).to_edge(RIGHT, buff=0.5)
        for r in left:
            self.step(r)
        self.box(left[2], left[4])
        for r in right:
            self.step(r)
        self.box(right[2], right[4])

    # ------------------------------------------------- other families -----
    def polynomials(self):
        h = self.topic("Polynomials")
        d = MathTex(r"p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0", font_size=42)
        d.next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        n = note(r"$n$ = \textbf{degree} (a whole number), \quad $a_0, \dots, a_n$ = \textbf{coefficients}.\\Domain: $(-\infty, \infty)$.")
        n.next_to(d, DOWN, aligned_edge=LEFT)
        self.play(Write(d), FadeIn(n))
        self.pause()
        self.example_tag("Example 14")
        poly = MathTex("p(x) = ", "3x^4", "- 2x^2", "+ x", "- 7", font_size=46).next_to(n, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(poly))
        self.pause()
        q = stack(
            row(r"\text{degree} = 4", r"highest power of $x$"),
            row(r"\text{leading coefficient} = 3", r"coefficient on that highest power"),
            row(r"\text{constant term} = -7", r"$a_0$"),
            row(r"a_3 = 0", r"there is no $x^3$ term"),
            buff=0.3,
        ).next_to(poly, DOWN, aligned_edge=LEFT, buff=0.5)
        self.step(q[0], Indicate(poly[1]))
        self.step(q[1], Indicate(poly[1]))
        self.step(q[2], Indicate(poly[4]))
        self.step(q[3])

    def rational_example(self):
        h = self.topic("Rational Functions")
        d = MathTex(r"f(x) = \frac{p(x)}{q(x)}", font_size=46).next_to(h, DOWN, aligned_edge=LEFT, buff=0.4)
        n = note(r"$p, q$ polynomials. Domain: every $x$ with $q(x) \ne 0$.").next_to(d, RIGHT, buff=0.6)
        self.play(Write(d), FadeIn(n))
        self.pause()
        self.example_tag("Example 15")
        prob = MathTex(r"\text{Find the domain of } f(x) = \frac{x + 1}{x^2 - 4}.", font_size=38)
        prob.next_to(d, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(prob))
        steps = stack(
            row(r"x^2 - 4 = 0", r"find where the denominator is $0$"),
            row(r"(x - 2)(x + 2) = 0", r"difference of squares"),
            row(r"x = 2 \ \text{or}\ x = -2"),
            row(r"D = (-\infty, -2) \cup (-2, 2) \cup (2, \infty)", color=INPUT, fs=36),
            buff=0.3, max_width=6.4,
        ).next_to(prob, DOWN, aligned_edge=LEFT, buff=0.4)
        ax = make_axes([-5, 5, 1], [-5, 5, 1], 5.6, 4.6, fs=18).to_corner(DR, buff=0.35)
        self.step(steps[0])
        self.step(steps[1])
        asy = VGroup(DashedLine(ax.c2p(-2, -5), ax.c2p(-2, 5), color=MUTED),
                     DashedLine(ax.c2p(2, -5), ax.c2p(2, 5), color=MUTED))
        self.step(steps[2], Create(ax), Create(asy))
        g = plot_clip(ax, lambda x: (x + 1) / (x * x - 4), -5, 5)
        self.step(steps[3], Create(g), run_time=2)
        self.box(steps[3])

    def other_families(self):
        h = self.topic("More Families of Functions")
        specs = [
            ("Algebraic", r"y = \sqrt[3]{x}\,(x - 2)", lambda x: np.cbrt(x) * (x - 2), [-2, 4], BLUE,
             r"polynomials combined with roots"),
            ("Trigonometric", r"y = \sin x", np.sin, [-3, 3], PINK, r"Section 1.3"),
            ("Exponential", r"y = 2^x", lambda x: 2.0 ** x, [-3, 3], GREEN, r"$a^x$, $a > 0$, $a \ne 1$ (Section 1.4)"),
            ("Logarithmic", r"y = \log_2 x", np.log2, [0.01, 3], ORANGE, r"inverse of $a^x$ (Section 1.5)"),
        ]
        panels = VGroup()
        for name, f_tex, fn, (a, b), col, sub in specs:
            A = make_axes([-3, 4, 1], [-2, 3, 1], 3.0, 2.4, numbers=False)
            c = plot_clip(A, fn, a, b, color=col)
            title = Tex(name, font_size=30, color=col)
            ft = MathTex(f_tex, font_size=28)
            s = note(sub, fs=20)
            VGroup(title, ft).arrange(DOWN, buff=0.1).next_to(A, UP, buff=0.1)
            s.next_to(A, DOWN, buff=0.1)
            panels.add(VGroup(A, c, title, ft, s))
        panels.arrange_in_grid(rows=1, buff=0.3).scale_to_fit_width(13).next_to(h, DOWN, buff=0.6).set_x(0)
        for p in panels:
            self.play(Create(p[0]), Write(p[2]), Write(p[3]), run_time=0.7)
            self.play(Create(p[1]), FadeIn(p[4]))
            self.pause()
        trans = framed(para(
            r"\textbf{Transcendental} = not algebraic: trigonometric, inverse trigonometric,\\"
            r"exponential, and logarithmic functions. Every rational function is algebraic,\\"
            r"but not every algebraic function is rational (e.g.\ $\sqrt{x}$).", fs=28),
            "Big picture", color=PURPLE_B)
        trans.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(trans))
        self.pause()

    def classify_example(self):
        h = self.topic("Identify the Type of Function")
        self.example_tag("Example 16")
        items = [
            (r"y = 2x^3 - x + 5", r"\text{polynomial (degree 3)}", BLUE),
            (r"y = \dfrac{x^2 + 1}{x - 3}", r"\text{rational}", TEAL),
            (r"y = x^{2/3}", r"\text{power (algebraic)}", GREEN),
            (r"y = \sqrt{x^2 + 1}", r"\text{algebraic, not rational}", GREEN_B),
            (r"y = 5^x", r"\text{exponential (transcendental)}", ORANGE),
            (r"y = \log_3 x", r"\text{logarithmic (transcendental)}", ORANGE),
            (r"y = \cos x", r"\text{trigonometric (transcendental)}", PINK),
        ]
        lefts = VGroup(*[MathTex(f, font_size=36) for f, _, _ in items])
        rights = VGroup(*[MathTex(t, font_size=34, color=c) for _, t, c in items])
        grid = VGroup(*[VGroup(l, r) for l, r in zip(lefts, rights)])
        for gl in grid:
            gl[1].next_to(gl[0], RIGHT, buff=0.6)
        lefts.arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(h, DOWN, aligned_edge=LEFT, buff=0.4).shift(RIGHT * 0.5)
        for l, r in zip(lefts, rights):
            r.move_to(l, coor_mask=UP).set_x(1.0, direction=LEFT)
        self.play(LaggedStart(*[Write(l) for l in lefts], lag_ratio=0.15))
        self.pause()
        for r in rights:
            self.play(Write(r))
            self.pause()

    def recap(self):
        h = self.topic("Section 1.1 Recap")
        items = BulletedList(
            r"A function gives \emph{exactly one} output for each input (vertical line test).",
            r"Domain: allowed inputs (watch $\div 0$ and even roots). Range: outputs produced.",
            r"Piecewise functions use the formula whose condition fits $x$.",
            r"Increasing: $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$; decreasing: the reverse.",
            r"Even: $f(-x) = f(x)$, $y$-axis symmetry. Odd: $f(-x) = -f(x)$, origin symmetry.",
            r"Families: linear, power, polynomial, rational, algebraic, transcendental.",
            font_size=32, buff=0.3,
        ).next_to(h, DOWN, aligned_edge=LEFT, buff=0.5)
        for it in items:
            self.play(FadeIn(it, shift=RIGHT * 0.2))
        self.pause()
