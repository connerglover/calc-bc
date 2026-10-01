"""Shared look and helpers for the AP Calculus BC manim-slides lessons.

Style: dark chalkboard, colour-coded math, one idea per slide, and worked
examples revealed one step at a time (each step is its own slide, so the
presenter advances through a solution with the arrow keys).
"""

import numpy as np
from manim import *
from manim_slides import Slide

BG = "#0f1115"
config.background_color = BG

MUTED = GREY_B
INPUT = YELLOW  # x / inputs / domain
OUTPUT = GREEN  # y / outputs / range
FUNC = BLUE  # the function itself
ALT = PINK  # a second function
WARN = RED
ANSWER = GOLD


# --------------------------------------------------------------- text ------
def para(s, fs=32, color=WHITE):
    """Left-aligned prose. Break lines by hand with \\\\."""
    return Tex(s, font_size=fs, color=color, tex_environment="flushleft")


def note(s, fs=28):
    return Tex(s, font_size=fs, color=MUTED)


def row(math, comment=None, fs=40, color=WHITE):
    """One line of a worked solution: math, with an optional grey side note."""
    m = MathTex(math, font_size=fs, color=color) if isinstance(math, str) else math
    if comment is None:
        return m
    c = note(comment)
    c.next_to(m, RIGHT, buff=0.45)
    return VGroup(m, c)


def stack(*rows, buff=0.32, max_width=None):
    g = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=buff)
    if max_width is not None and g.width > max_width:
        g.scale_to_fit_width(max_width)
    return g


def framed(body, title="Definition", color=GREEN, buff=0.3):
    """A KA-style definition / formula card."""
    frame = SurroundingRectangle(body, color=color, buff=buff, corner_radius=0.12)
    frame.set_fill(color, opacity=0.08)
    label = Tex(title, font_size=28, color=color)
    label.next_to(frame, UP, aligned_edge=LEFT, buff=0.1)
    return VGroup(frame, label, body)


# --------------------------------------------------------------- graphs ----
def make_axes(x_range, y_range, x_length, y_length, numbers=True, fs=22,
              x_label="x", y_label="y"):
    ax = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=True,
        axis_config={
            "color": MUTED,
            "stroke_width": 2,
            "include_numbers": numbers,
            "font_size": fs,
            "numbers_to_exclude": [0],
            "tip_width": 0.18,
            "tip_height": 0.18,
        },
    )
    labels = ax.get_axis_labels(
        MathTex(x_label, font_size=30, color=MUTED),
        MathTex(y_label, font_size=30, color=MUTED),
    )
    ax.add(labels)
    return ax


def plot_clip(ax, f, x_min, x_max, color=FUNC, n=900, stroke_width=4,
              y_min=None, y_max=None):
    """Plot f on [x_min, x_max], dropping any part outside the visible y-range.

    Handles asymptotes and undefined points (NaN / division by zero) by
    splitting the curve into separate pieces.
    """
    lo = ax.y_range[0] if y_min is None else y_min
    hi = ax.y_range[1] if y_max is None else y_max
    pieces, cur = [], []
    with np.errstate(all="ignore"):
        for x in np.linspace(x_min, x_max, n):
            try:
                y = float(f(x))
            except (ZeroDivisionError, ValueError, OverflowError):
                y = np.nan
            if np.isfinite(y) and lo <= y <= hi:
                cur.append(ax.c2p(x, y))
            else:
                if len(cur) > 1:
                    pieces.append(cur)
                cur = []
    if len(cur) > 1:
        pieces.append(cur)
    g = VGroup()
    for p in pieces:
        m = VMobject(color=color, stroke_width=stroke_width)
        m.set_points_as_corners(p)
        g.add(m)
    return g


def endpoint(point, closed, color):
    if closed:
        return Dot(point, radius=0.09, color=color)
    c = Circle(radius=0.09, color=color, stroke_width=3)
    c.set_fill(BG, opacity=1).move_to(point)
    return c


def axis_interval(ax, a, b, axis="x", color=INPUT, closed=(True, True), width=9):
    """Highlight an interval on an axis. a/b = None means 'to the end of the axis'."""
    rng = ax.x_range if axis == "x" else ax.y_range
    lo = rng[0] if a is None else a
    hi = rng[1] if b is None else b

    def p(v):
        return ax.c2p(v, 0) if axis == "x" else ax.c2p(0, v)

    g = VGroup(Line(p(lo), p(hi), color=color, stroke_width=width))
    if a is not None:
        g.add(endpoint(p(a), closed[0], color))
    if b is not None:
        g.add(endpoint(p(b), closed[1], color))
    return g


def value_table(xs, ys, x_label="x", y_label="y", cell_w=0.95, cell_h=0.6, fs=32):
    """Two-row table. Returns (table, x_cells, y_cells); each cell is VGroup(box, tex)."""
    def cell(s, color=WHITE, fill=None):
        box = Rectangle(width=cell_w, height=cell_h, color=MUTED, stroke_width=2)
        if fill:
            box.set_fill(fill, opacity=0.15)
        t = MathTex(s, font_size=fs, color=color).move_to(box)
        return VGroup(box, t)

    top = VGroup(cell(x_label, INPUT, INPUT), *[cell(str(x)) for x in xs]).arrange(RIGHT, buff=0)
    bot = VGroup(cell(y_label, OUTPUT, OUTPUT), *[cell(str(y)) for y in ys]).arrange(RIGHT, buff=0)
    table = VGroup(top, bot).arrange(DOWN, buff=0)
    return table, top[1:], bot[1:]


# --------------------------------------------------------------- scene -----
class Lesson(Slide):
    """Base slide deck with presenter-friendly helpers."""

    def pause(self):
        self.next_slide()

    def clear(self):
        mobs = [m for m in self.mobjects]
        for m in mobs:
            m.clear_updaters()
        if mobs:
            self.play(FadeOut(Group(*mobs)), run_time=0.6)

    def title_card(self, number, title, blurb):
        num = Tex(f"Section {number}", font_size=40, color=YELLOW)
        t = Tex(title, font_size=64)
        if t.width > 12.5:
            t.scale_to_fit_width(12.5)
        rule = Line(LEFT * 4, RIGHT * 4, color=YELLOW, stroke_width=3)
        b = Tex(blurb, font_size=32, color=MUTED)
        g = VGroup(num, t, rule, b).arrange(DOWN, buff=0.4)
        self.play(FadeIn(num, shift=DOWN * 0.3))
        self.play(Write(t), GrowFromCenter(rule))
        self.play(FadeIn(b))
        self.pause()
        self.clear()

    def heading(self, text):
        h = Tex(text, font_size=44, color=YELLOW).to_corner(UL, buff=0.4)
        ul = Underline(h, color=YELLOW, buff=0.08, stroke_width=3)
        self.play(Write(h), Create(ul), run_time=0.9)
        return VGroup(h, ul)

    def topic(self, text):
        """Clear the board and start a new topic."""
        self.clear()
        return self.heading(text)

    def example_tag(self, label):
        t = Tex(label, font_size=30, color=BLACK)
        bg = RoundedRectangle(
            corner_radius=0.15, width=t.width + 0.45, height=t.height + 0.3,
            fill_color=ORANGE, fill_opacity=1, stroke_width=0,
        )
        t.move_to(bg)
        g = VGroup(bg, t).to_corner(UR, buff=0.4)
        self.play(FadeIn(g, shift=LEFT * 0.3))
        return g

    def step(self, mob, *extra, pause=True, run_time=None):
        kw = {} if run_time is None else {"run_time": run_time}
        self.play(Write(mob), *extra, **kw)
        if pause:
            self.pause()

    def box(self, *mobs, color=ANSWER, pause=True):
        """Box each final answer (separately when there are several)."""
        rs = VGroup(*[SurroundingRectangle(m, color=color, buff=0.12, corner_radius=0.08) for m in mobs])
        self.play(Create(rs))
        if pause:
            self.pause()
        return rs
