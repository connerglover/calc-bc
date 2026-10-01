# Lesson slides (manim + manim-slides)

Animated, step-by-step lessons for each section of the notes.

| File | Scene | Section |
| --- | --- | --- |
| `section_1_1.py` | `Section1_1` | 1.1 Functions and Their Graphs |
| `section_1_2.py` | `Section1_2` | 1.2 Combining Functions; Shifting and Scaling Graphs |

`common.py` holds the shared style (colors, axes, step-by-step helpers).

## Requirements

- `manim` and `manim-slides` (installed globally with `uv tool install`, Python 3.13)
- MiKTeX (LaTeX for the math), set to auto-install missing packages
- FFmpeg

## Render

Run from this folder:

```sh
manim-slides render --quality h section_1_1.py Section1_1   # 1080p
manim-slides render --quality h section_1_2.py Section1_2
```

Use `--quality l` for a quick 480p draft. Don't write `-qh`: manim-slides
reads the `h` as its own help flag and renders nothing.

## Present

```sh
manim-slides present Section1_1
```

Right arrow / space goes to the next step, left arrow goes back, `F` toggles fullscreen.

## Export

```sh
manim-slides convert Section1_1 section_1_1.html                 # self-contained web page
manim-slides convert --to pptx Section1_1 section_1_1.pptx       # PowerPoint
```
