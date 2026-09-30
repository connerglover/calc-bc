// ===========================================================================
//  template.typ -- shared textbook styles for the BC Calculus notes.
//
//  Usage (top of notes.typ):
//    #import "template.typ": *
//    #show: notes.with(title: "AP Calculus BC", source: [...])
//
//  The headings drive everything else:
//    = Chapter 3 -- Derivatives            chapter opener with its own contents
//    == Section 3.2 -- The Derivative ...  numbered section
//    === Increments                        subsection
//  The cover, table of contents, running heads, PDF bookmarks and box numbers
//  (Theorem 3.2.1, ...) are generated from those headings, and every entry in
//  the contents, the chapter openers and the running heads is a link.
//
//  Numbered boxes, which can be labelled and referenced:
//    #theorem(title: "Mean Value Theorem")[...] <mvt>     ... by @mvt, ...
//    #definition[...]  #example[...]  #formula[...]
//  Unnumbered: #note[...]  #warning[...]  #proof[...]  #solution[...]
//  Chapter furniture: #objectives[...]  #epigraph[quote][author]
//  Student work room: #workspace(3cm)  #lines(4)  #plane(xmin: -5, xmax: 5)
//
//  Export:
//    typst compile notes.typ                                  (PDF)
//    typst compile --features html --format html notes.typ    (HTML)
//  `notes.with(print: true)` switches everything to grayscale for printing.
//  Carmel Catholic version: brown and gold, with the school on the cover.
//    #show: notes.with(theme: themes.carmel,
//      school: "Carmel Catholic High School",
//      course: "Carmel Catholic · AP Calculus BC", ...)
// ===========================================================================

// ----------------------------------------------------------------- themes --
// accent:    cover, chapter bands, section badges, links
// highlight: the second school color -- band stripes, cover curve, eyebrows
// badge-ink: text on the section-number badges
#let themes = (
  classic: (
    accent: rgb("#17406d"),
    highlight: rgb("#a9c7ea"),
    badge-ink: white,
    ink: rgb("#1b1b1b"),
    muted: rgb("#6b7079"),
    hair: rgb("#c9cdd3"),
    theorem: rgb("#1f5fa8"),
    definition: rgb("#2e7d32"),
    example: rgb("#b26a00"),
    formula: rgb("#6a1b9a"),
    note: rgb("#5f6368"),
    warning: rgb("#c62828"),
  ),
  // Carmel Catholic brown and gold.
  carmel: (
    accent: rgb("#4a2c1d"),
    highlight: rgb("#d4a82a"),
    badge-ink: rgb("#f3d27a"),
    ink: rgb("#221a15"),
    muted: rgb("#7a6f66"),
    hair: rgb("#d9cfc4"),
    theorem: rgb("#5a3620"),
    definition: rgb("#9a7612"),
    example: rgb("#b5651d"),
    formula: rgb("#7b2d26"),
    note: rgb("#6e645c"),
    warning: rgb("#b3261e"),
  ),
)
// Everything collapses to black and gray so a laser printer loses nothing.
#let _grays = (
  accent: luma(15),
  highlight: luma(70),
  badge-ink: white,
  ink: luma(0),
  muted: luma(85),
  hair: luma(175),
  theorem: luma(15),
  definition: luma(15),
  example: luma(60),
  formula: luma(15),
  note: luma(85),
  warning: luma(15),
)
#let _print = state("bc-print", false)
#let _theme = state("bc-theme", themes.classic)
// Both need context.
#let _pal() = if _print.get() { _grays } else { _theme.get() }
#let _html() = target() == "html"

// Page geometry, shared by the cover and chapter bands that bleed to the edge.
#let _paper = (width: 8.5in, height: 11in)
#let _margin = (x: 1in, top: 1.1in, bottom: 1in)

// -------------------------------------------------------- heading parsing --
// Headings are written "Chapter 3 -- Derivatives" / "Section 3.2 -- ...".
// The textbook skips sections, so numbers are read from the heading rather
// than counted.
#let _plain(it) = {
  if it == none { "" }
  else if type(it) == str { it }
  else if it.func() == smartquote { if it.double { "\"" } else { "’" } }
  else if it.has("text") { _plain(it.text) }
  else if it.has("children") { it.children.map(_plain).sum(default: "") }
  else if it.has("body") { _plain(it.body) }
  else { " " }
}

#let _split(body) = {
  let s = _plain(body).trim()
  let m = s.match(regex("^(?:Chapter|Section|Unit)\s+([0-9]+(?:\.[0-9]+)?)\s*(?:[-–—:]+\s*(.*))?$"))
  if m == none { (num: none, title: s) }
  else { (num: m.captures.at(0), title: m.captures.at(1, default: none)) }
}

// ------------------------------------------------------- numbering state --
#let _chapter = state("bc-chapter", none)
#let _section = state("bc-section", none)

#let _kinds = (
  theorem: [Theorem],
  definition: [Definition],
  example: [Example],
  formula: [Formula],
)
#let _reset-boxes() = for k in _kinds.keys() {
  counter(figure.where(kind: "bc-" + k)).update(0)
}

// "3.2.1": section, then the box's position within the section.
#let _number-at(loc, kind) = {
  let n = counter(figure.where(kind: kind)).at(loc).first()
  let prefix = _section.at(loc)
  if prefix == none { prefix = _chapter.at(loc) }
  if prefix == none { str(n) } else { prefix + "." + str(n) }
}

// ============================================================== BOXES ======
// Numbered boxes are figures so `<label>` / `@label` work. The figure's
// caption carries the optional title.
#let _box(kind) = (title: none, body) => figure(
  kind: "bc-" + kind,
  supplement: _kinds.at(kind),
  numbering: "1",
  outlined: false,
  caption: title,
  body,
)

#let theorem = _box("theorem")
#let definition = _box("definition")
#let example = _box("example")
#let formula = _box("formula")

// Label shared by every box: "Theorem 3.2.1 (Mean Value Theorem)".
#let _box-label(name, num, title, color) = {
  text(weight: "bold", fill: color)[#name#if num != none [ #num]]
  if title != none [ #text(style: "italic")[(#title)]]
}

#let _html-box(kind, name, num, title, body) = html.elem(
  "div",
  attrs: (class: "box " + kind),
  {
    html.elem("div", attrs: (class: "box-head"), {
      html.elem("span", attrs: (class: "box-name"))[#name#if num != none [ #num]]
      if title != none { html.elem("span", attrs: (class: "box-title"), title) }
    })
    html.elem("div", attrs: (class: "box-body"), body)
  },
)

#let _render-box(it) = context {
  let kind = it.kind.slice(3)
  let p = _pal()
  let col = p.at(kind)
  let num = _number-at(it.location(), it.kind)
  let title = if it.caption != none { it.caption.body } else { none }
  let space = (above: 1.35em, below: 1.35em)
  // Figures center their contents by default; boxes read left to right.
  set align(start)

  if _html() {
    _html-box(kind, it.supplement, num, title, it.body)
  } else if kind == "theorem" {
    // Solid title band over a tinted panel.
    let band = if _print.get() { luma(228) } else { col }
    let band-ink = if _print.get() { black } else { white }
    block(width: 100%, breakable: true, stroke: 0.9pt + col, radius: 4pt, clip: true, ..space, {
      block(width: 100%, fill: band, inset: (x: 12pt, y: 6pt), above: 0pt, below: 0pt, sticky: true,
        text(fill: band-ink, _box-label(smallcaps(it.supplement), num, title, band-ink)))
      block(width: 100%, fill: col.lighten(95%), inset: (x: 12pt, top: 9pt, bottom: 11pt),
        above: 0pt, below: 0pt, it.body)
    })
  } else if kind == "definition" {
    // Tinted panel with a heavy left rule; the label runs into the text.
    block(width: 100%, breakable: true, fill: col.lighten(93%), stroke: (left: 3.5pt + col),
      radius: (right: 4pt), inset: (x: 13pt, y: 10pt), ..space,
      [#_box-label(it.supplement, num, title, col.darken(15%))#h(0.6em)#it.body])
  } else if kind == "formula" {
    // Double rule: the frame worth memorizing.
    block(width: 100%, breakable: false, stroke: 0.7pt + col, radius: 4pt, inset: 2.5pt, ..space,
      block(width: 100%, stroke: 0.7pt + col, radius: 2.5pt, fill: col.lighten(96%),
        inset: (x: 13pt, y: 10pt), {
          _box-label(smallcaps(it.supplement), num, title, col.darken(10%))
          block(above: 0.7em, below: 0pt, width: 100%, it.body)
        }))
  } else {
    // Example: open, with a colored rule down the left.
    block(width: 100%, breakable: true, stroke: (left: 2pt + col), inset: (left: 13pt, y: 5pt), ..space,
      [#_box-label(smallcaps(it.supplement), num, title, col.darken(10%))#h(0.6em)#it.body])
  }
}

// Unnumbered asides.
#let note(title: none, body) = context {
  let col = _pal().note
  if _html() { return _html-box("note", [Note], none, title, body) }
  block(width: 100%, breakable: true, fill: col.lighten(92%), stroke: (left: 1.5pt + col),
    radius: (right: 3pt), inset: (x: 12pt, y: 8pt), above: 1.1em, below: 1.1em,
    text(size: 0.93em)[#_box-label(smallcaps[Note], none, title, col)#h(0.5em)#body])
}

#let warning(title: none, body) = context {
  let col = _pal().warning
  if _html() { return _html-box("warning", [Watch Out], none, title, body) }
  let mark = box(baseline: 0.18em, circle(radius: 0.6em, fill: col,
    align(center + horizon, text(fill: white, weight: "bold", size: 0.85em)[!])))
  block(width: 100%, breakable: true, stroke: (paint: col, thickness: 0.9pt, dash: "dashed"),
    radius: 4pt, inset: (x: 12pt, y: 9pt), above: 1.1em, below: 1.1em,
    [#mark#h(0.45em)#_box-label(smallcaps[Watch Out], none, title, col)#h(0.5em)#body])
}

// Proof / solution: unboxed. Proof ends with a square.
#let proof(body) = context {
  if _html() {
    return html.elem("div", attrs: (class: "proof"))[_Proof._ #body #html.elem("span", attrs: (class: "qed"))[□]]
  }
  block(inset: (left: 12pt), above: 0.9em, below: 1.1em)[
    #text(style: "italic", weight: "bold")[Proof.] #body #h(1fr) $square$
  ]
}

#let solution(body) = context {
  let col = _pal().example
  if _html() {
    return html.elem("div", attrs: (class: "solution"))[#strong[Solution.] #body]
  }
  block(inset: (left: 13pt), above: 0.8em, below: 1.1em)[
    #text(weight: "bold", fill: col.darken(10%))[Solution.] #body
  ]
}

// ===================================================== CHAPTER FURNITURE ===
// Learning objectives, usually right under a chapter heading.
#let objectives(title: [By the end of this chapter you should be able to:], body) = context {
  let p = _pal()
  if _html() {
    return html.elem("div", attrs: (class: "objectives"), {
      html.elem("div", attrs: (class: "objectives-head"), title)
      body
    })
  }
  block(width: 100%, breakable: true, stroke: 0.9pt + p.accent, radius: 4pt, clip: true,
    above: 1.2em, below: 1.4em, {
      block(width: 100%, fill: p.accent.lighten(90%), inset: (x: 12pt, y: 7pt), above: 0pt,
        below: 0pt, sticky: true, text(weight: "bold", fill: p.accent, smallcaps(title)))
      block(width: 100%, inset: (x: 12pt, top: 8pt, bottom: 10pt), above: 0pt, below: 0pt, {
        set enum(numbering: n => text(weight: "bold", fill: p.accent)[#n.])
        body
      })
    })
}

// Quotation under a chapter heading.
#let epigraph(quote, author) = context {
  if _html() {
    return html.elem("blockquote", attrs: (class: "epigraph"))[#quote #html.elem("footer")[— #author]]
  }
  align(right, block(width: 62%, above: 1em, below: 1.6em, {
    set par(justify: false)
    align(left, text(style: "italic", size: 10.5pt, quote))
    v(0.3em)
    align(right, text(size: 9.5pt, fill: _pal().muted)[— #author])
  }))
}

// ====================================================== STUDENT WORK ROOM ==
// Blank room that survives a page break.
#let workspace(height) = context {
  if _html() { return html.elem("div", attrs: (class: "workspace", style: "height:" + repr(height))) }
  block(width: 100%, height: height, breakable: false, above: 0.4em, below: 0.6em)
}

// n faint writing rules, like notebook paper.
#let lines(n, gap: 0.8cm) = context {
  let col = _pal().hair
  if _html() {
    return html.elem("div", attrs: (class: "lines", style: "--n:" + str(n)))
  }
  block(width: 100%, breakable: false, above: 0.6em, below: 0.8em,
    for _ in range(n) { block(width: 100%, height: gap, above: 0pt, below: 0pt,
      align(bottom, line(length: 100%, stroke: 0.5pt + col))) })
}

// Blank coordinate plane for students to graph on.
//   #plane(xmin: -4, xmax: 6, ymin: -2, ymax: 8, unit: 0.55cm)
#let plane(xmin: -5, xmax: 5, ymin: -5, ymax: 5, step: 1, unit: 0.5cm,
  labels: true, xlabel: $x$, ylabel: $y$) = context {
  let p = _pal()
  let w = (xmax - xmin) * unit
  let h = (ymax - ymin) * unit
  let X(x) = (x - xmin) * unit
  let Y(y) = (ymax - y) * unit
  let nx = int(calc.round((xmax - xmin) / step))
  let ny = int(calc.round((ymax - ymin) / step))
  let label(body) = text(size: 6.5pt, fill: p.ink, body)
  let drawing = box(width: w, height: h, {
    for i in range(nx + 1) {
      let x = X(xmin + i * step)
      place(line(start: (x, 0pt), end: (x, h), stroke: 0.35pt + p.hair))
    }
    for j in range(ny + 1) {
      let y = Y(ymin + j * step)
      place(line(start: (0pt, y), end: (w, y), stroke: 0.35pt + p.hair))
    }
    let has-y = xmin <= 0 and 0 <= xmax
    let has-x = ymin <= 0 and 0 <= ymax
    if has-y {
      place(line(start: (X(0), 0pt), end: (X(0), h), stroke: 0.9pt + p.ink))
      place(dx: X(0) + 3pt, dy: -9pt, label(ylabel))
    }
    if has-x {
      place(line(start: (0pt, Y(0)), end: (w, Y(0)), stroke: 0.9pt + p.ink))
      place(dx: w + 3pt, dy: Y(0) - 4pt, label(xlabel))
    }
    if labels {
      let ax = if has-x { Y(0) } else { h }
      let ay = if has-y { X(0) } else { 0pt }
      for i in range(nx + 1) {
        let v = xmin + i * step
        if v != 0 {
          place(dx: X(v) - 1em, dy: ax + 2pt, box(width: 2em, align(center, label(str(v)))))
        }
      }
      for j in range(ny + 1) {
        let v = ymin + j * step
        if v != 0 {
          place(dx: ay - 2em - 2pt, dy: Y(v) - 3.5pt, box(width: 2em, align(right, label(str(v)))))
        }
      }
    }
  })
  if _html() { return html.elem("div", attrs: (class: "plane"), html.frame(drawing)) }
  block(width: 100%, breakable: false, above: 1.2em, below: 1.4em, align(center, drawing))
}

// ================================================================ HEADINGS =
#let _chapter-heading(it) = {
  let parts = _split(it.body)
  _chapter.update(parts.num)
  _section.update(none)
  _reset-boxes()
  context {
    let p = _pal()
    // This chapter's sections, for the "In this chapter" list.
    let all = query(heading.where(level: 1).or(heading.where(level: 2)))
    let i = all.position(h => h.location() == it.location())
    let sections = ()
    for h in all.slice(i + 1) {
      if h.level == 1 { break }
      sections.push(h)
    }

    if _html() {
      html.elem("header", attrs: (class: "chapter"), {
        if parts.num != none { html.elem("div", attrs: (class: "chapter-num"))[Chapter #parts.num] }
        html.elem("h2", if parts.title != none { parts.title } else { it.body })
        if sections.len() > 0 {
          html.elem("ul", attrs: (class: "chapter-toc"), for s in sections {
            let sp = _split(s.body)
            html.elem("li", link(s.location())[#html.elem("b", sp.num) #sp.title])
          })
        }
      })
      return
    }

    let band = 3.2in
    let cover = if _print.get() { luma(232) } else { p.accent }
    let ink = if _print.get() { black } else { white }
    pagebreak(weak: true)
    place(top + left, dx: -_margin.x, dy: -_margin.top,
      block(width: _paper.width, height: band, fill: cover, clip: true, {
        // Oversized ghost numeral bleeding off the right edge.
        if parts.num != none {
          place(bottom + right, dx: 0.35in, dy: 0.62in,
            text(size: 250pt, weight: "bold", fill: p.highlight.transparentize(82%), parts.num))
        }
        place(bottom, rect(width: 100%, height: 5pt, fill: p.highlight))
        place(bottom + left, dx: _margin.x, dy: -0.45in, block(width: 5.6in, {
          if parts.num != none {
            text(size: 11pt, tracking: 0.28em, weight: "bold", fill: p.highlight,
              upper[Chapter #parts.num])
            v(0.25em)
          }
          set par(justify: false, leading: 0.5em)
          text(size: 30pt, weight: "bold", fill: ink,
            if parts.title != none { parts.title } else { it.body })
        }))
      }))
    v(band - _margin.top + 0.3in)

    if sections.len() > 0 {
      block(width: 100%, above: 0pt, below: 1.8em, {
        text(size: 9pt, tracking: 0.18em, weight: "bold", fill: p.accent, upper[In this chapter])
        v(0.2em)
        line(length: 100%, stroke: 0.6pt + p.accent)
        v(0.1em)
        set text(size: 10pt, weight: "regular")
        for s in sections {
          let sp = _split(s.body)
          link(s.location(), block(above: 0.55em, below: 0.55em, grid(
            columns: (3.2em, 1fr),
            text(weight: "bold", fill: p.accent, sp.num),
            [#sp.title #box(width: 1fr, repeat(gap: 0.3em, text(fill: p.hair)[.])) #counter(page).display(at: s.location())],
          )))
        }
      })
    }
  }
}

#let _section-heading(it) = {
  let parts = _split(it.body)
  _section.update(parts.num)
  _reset-boxes()
  context {
    let p = _pal()
    let title = if parts.title != none { parts.title } else { it.body }
    if _html() {
      return html.elem("h3", attrs: (class: "section"), {
        if parts.num != none { html.elem("span", attrs: (class: "section-num"), parts.num) }
        title
      })
    }
    // Sticky is off: a long run of still-empty sections would chain into one
    // block too tall for any page and get pushed off it.
    block(width: 100%, above: 2.1em, below: 1.2em, sticky: false, {
      set par(justify: false)
      set text(weight: "regular")
      grid(columns: (auto, 1fr), column-gutter: 0.7em, align: horizon,
        if parts.num != none {
          box(fill: p.accent, inset: (x: 6.5pt, y: 4.5pt), radius: 3pt,
            text(size: 12.5pt, weight: "bold", fill: p.badge-ink, parts.num))
        },
        text(size: 15pt, weight: "bold", fill: p.ink, title))
      v(0.35em)
      line(length: 100%, stroke: 0.5pt + p.hair)
    })
  }
}

#let _subsection-heading(it) = context {
  let p = _pal()
  if _html() { return html.elem("h4", attrs: (class: "subsection"), it.body) }
  block(above: 1.6em, below: 0.75em, sticky: true,
    text(size: 12pt, weight: "bold", fill: p.accent, it.body))
}

// =========================================================== PAGE PARTS ====
#let _is-opener(pg) = query(heading.where(level: 1)).any(h => h.location().page() == pg)

// Running head: chapter on the left, current section on the right, both links.
#let _header() = context {
  let pg = here().page()
  let chapters = query(heading.where(level: 1)).filter(h => h.location().page() < pg)
  if _is-opener(pg) or chapters.len() == 0 { return }
  let p = _pal()
  let ch = chapters.last()
  let cp = _split(ch.body)
  let secs = query(heading.where(level: 2)).filter(h =>
    h.location().page() >= ch.location().page() and h.location().page() <= pg)
  let here-secs = secs.filter(h => h.location().page() == pg)
  let sec = if here-secs.len() > 0 { here-secs.first() } else if secs.len() > 0 { secs.last() }
  set text(size: 8.5pt, fill: p.muted)
  grid(columns: (1fr, auto), align: (left + bottom, right + bottom),
    link(ch.location(), text(tracking: 0.08em, upper(
      if cp.num != none [Chapter #cp.num #h(0.3em)·#h(0.3em) #cp.title] else { cp.title }))),
    if sec != none {
      let sp = _split(sec.body)
      link(sec.location())[#text(weight: "bold", fill: p.accent, sp.num)#h(0.5em)#sp.title]
    })
  v(-0.45em)
  line(length: 100%, stroke: 0.4pt + p.hair)
}

// Footer: course name and page number; the number links back to the contents.
#let _footer(course, contents) = context {
  let p = _pal()
  let num = text(weight: "bold", fill: p.accent, counter(page).display())
  set text(size: 8.5pt, fill: p.muted)
  grid(columns: (1fr, auto), align: (left, right),
    text(tracking: 0.08em, upper(course)),
    if contents { link(<bc-contents>, num) } else { num })
}

// ------------------------------------------------------------------ cover --
#let _cover(title, subtitle, course, school, author, source) = context {
  let eyebrow = if school != none { school } else if course != title { course }
  let p = _pal()
  if _html() {
    return html.elem("header", attrs: (class: "cover"), {
      if eyebrow != none { html.elem("div", attrs: (class: "cover-course"), eyebrow) }
      html.elem("h1", title)
      if subtitle != none { html.elem("div", attrs: (class: "cover-subtitle"), subtitle) }
      if author != none { html.elem("div", attrs: (class: "cover-author"), author) }
      if source != none { html.elem("div", attrs: (class: "cover-source"), source) }
    })
  }
  let fill = if _print.get() { luma(236) } else { p.accent }
  let ink = if _print.get() { black } else { white }
  let panel = 6.3in
  page(margin: 0pt, header: none, footer: none, {
    block(width: 100%, height: panel, fill: fill, clip: true, above: 0pt, below: 0pt, {
      // Cover art: a left Riemann sum under a smooth curve.
      let f(x) = 1.35 + 0.55 * calc.sin(0.9 * x - 0.4) + 0.12 * x
      let (x0, x1, n) = (0.0, 10.0, 20)
      let sx = _paper.width / (x1 - x0)
      let sy = 0.8in
      let base = 3.3in
      let dx = (x1 - x0) / n
      for i in range(n) {
        let x = x0 + i * dx
        place(dx: x * sx, dy: base - f(x) * sy, rect(width: dx * sx, height: f(x) * sy,
          fill: ink.transparentize(90%), stroke: 0.6pt + ink.transparentize(72%)))
      }
      let pts = range(121).map(k => {
        let x = x0 + k * (x1 - x0) / 120
        (x * sx, base - f(x) * sy)
      })
      place(curve(stroke: 2.2pt + p.highlight,
        curve.move(pts.first()), ..pts.slice(1).map(q => curve.line(q))))
      place(dy: base, line(length: 100%, stroke: 0.8pt + ink.transparentize(50%)))
      place(bottom, rect(width: 100%, height: 7pt, fill: p.highlight))

      place(bottom + left, dx: _margin.x, dy: -0.55in, block(width: 6.5in, {
        if eyebrow != none {
          text(size: 11pt, tracking: 0.3em, weight: "bold", fill: p.highlight, upper(eyebrow))
          v(0.5em)
        }
        set par(justify: false, leading: 0.45em)
        text(size: 42pt, weight: "bold", fill: ink, title)
        if subtitle != none {
          v(0.35em)
          text(size: 17pt, fill: ink.transparentize(15%), subtitle)
        }
      }))
    })
    place(bottom + left, dx: _margin.x, dy: -0.9in, block(width: 6.5in, {
      set par(justify: false)
      if author != none { text(size: 13pt, weight: "bold", fill: p.ink, author); v(0.8em) }
      line(length: 2.2in, stroke: 1.2pt + p.accent)
      v(0.5em)
      if source != none { text(size: 9.5pt, fill: p.muted, source) }
    }))
  })
}

// --------------------------------------------------------------- contents --
#let _toc-entry(it) = context {
  if _html() { return it }
  let p = _pal()
  let parts = _split(it.element.body)
  let num = if parts.num != none { parts.num } else { [] }
  let title = if parts.title != none { parts.title } else { it.element.body }
  if it.level == 1 {
    link(it.element.location(), block(above: 1.3em, below: 0.6em, sticky: true, grid(
      columns: (2.6em, 1fr, auto),
      text(size: 12pt, weight: "bold", fill: p.accent, num),
      text(size: 12pt, weight: "bold", title),
      text(size: 12pt, weight: "bold", fill: p.accent, it.page()),
    )))
  } else {
    link(it.element.location(), block(above: 0.5em, below: 0.5em, grid(
      columns: (2.6em, 3em, 1fr),
      [],
      text(fill: p.muted, num),
      [#title #box(width: 1fr, repeat(gap: 0.3em, text(fill: p.hair)[.])) #it.page()],
    )))
  }
}

#let _contents() = context {
  let p = _pal()
  let heading-block = [
    #text(size: 11pt, tracking: 0.3em, weight: "bold", fill: p.accent, upper[Contents])
    #v(0.2em)
    #line(length: 100%, stroke: 1.2pt + p.accent)
  ]
  if _html() {
    return html.elem("section", attrs: (class: "contents"), {
      [#html.elem("h2")[Contents] <bc-contents>]
      // Built by hand so entries read "4.2 The Mean Value Theorem".
      let entry(h) = {
        let parts = _split(h.body)
        link(h.location())[#if parts.num != none { html.elem("b", parts.num) } #if parts.title != none { parts.title } else { h.body }]
      }
      let all = query(heading.where(level: 1).or(heading.where(level: 2)))
      html.elem("nav", attrs: (class: "toc"), html.elem("ol", {
        let i = 0
        while i < all.len() {
          let ch = all.at(i)
          let secs = ()
          i += 1
          while i < all.len() and all.at(i).level == 2 {
            secs.push(all.at(i))
            i += 1
          }
          html.elem("li", {
            entry(ch)
            if secs.len() > 0 { html.elem("ol", for s in secs { html.elem("li", entry(s)) }) }
          })
        }
      }))
    })
  }
  page(header: none, numbering: "i",
    footer: align(center, text(size: 8.5pt, fill: p.muted, context counter(page).display("i"))), {
      [#heading-block <bc-contents>]
      v(0.6em)
      outline(title: none, depth: 2)
    })
}

// -------------------------------------------------------------- HTML css --
#let _css(t) = ":root{" + t.pairs().map(((k, v)) => "--" + k + ":" + v.to-hex()).join(";") + "}" + "
html{scroll-behavior:smooth}
body{margin:0 auto;max-width:46rem;padding:0 1.25rem 6rem;color:var(--ink);
font:1.06rem/1.62 'Latin Modern Roman','New Computer Modern','Sitka Text',Charter,Cambria,Georgia,serif}
math{font-family:'Latin Modern Math','New Computer Modern Math','STIX Two Math','Cambria Math',math}
a{color:inherit;text-decoration:none}
p:has(> .top-link){margin:0}
p{text-align:justify;hyphens:auto}
/* Full-bleed bands: the shadow paints the color out to both window edges. */
.cover,.chapter{position:relative;background:var(--accent);color:#fff;
box-shadow:0 0 0 100vmax var(--accent);clip-path:inset(0 -100vmax -5px)}
.cover::after,.chapter::after{content:'';position:absolute;left:0;right:0;bottom:-5px;height:5px;
background:var(--highlight);box-shadow:0 0 0 100vmax var(--highlight);clip-path:inset(0 -100vmax)}
.cover-course,.chapter-num{color:var(--highlight);font-weight:bold;opacity:1!important}
.cover{margin:0 0 calc(3rem + 5px);padding:4.5rem 0 3rem}
.cover-course{letter-spacing:.3em;text-transform:uppercase;font-size:.85rem;opacity:.8}
.cover h1{font-size:2.8rem;line-height:1.1;margin:.4rem 0}
.cover-subtitle{font-size:1.3rem;opacity:.9}
.cover-author{margin-top:1.5rem;font-weight:bold}
.cover-source{margin-top:1rem;font-size:.85rem;opacity:.75}
.contents h2{letter-spacing:.3em;text-transform:uppercase;font-size:1rem;color:var(--accent);
border-bottom:2px solid var(--accent);padding-bottom:.3rem}
.toc ol{list-style:none;padding:0;margin:0}
.toc > ol > li{margin:1rem 0 .3rem;font-weight:bold}
.toc a,.chapter-toc a{display:grid;grid-template-columns:2.6em 1fr;align-items:baseline}
.toc > ol > li > a b{color:var(--accent)}
.toc ol ol{margin:.3rem 0 0 2.6em;font-weight:normal;columns:2;column-gap:2rem}
.toc ol ol li{margin:.15rem 0;break-inside:avoid}
.toc ol ol b{color:var(--muted);font-weight:normal}
.contents a:hover,.chapter-toc a:hover{color:var(--accent);text-decoration:underline}
.chapter{margin:5rem 0 calc(2rem + 5px);padding:2.5rem 0 2rem}
.chapter-num{letter-spacing:.28em;text-transform:uppercase;font-size:.85rem;opacity:.8}
.chapter h2{font-size:2.2rem;line-height:1.15;margin:.3rem 0 1rem}
.chapter-toc{list-style:none;padding:0;margin:0;columns:2;font-size:.92rem}
.chapter-toc li{margin:.15rem 0;break-inside:avoid}
.chapter-toc b{opacity:.8}
h3.section{font-size:1.4rem;margin:2.6rem 0 1rem;padding-bottom:.35rem;border-bottom:1px solid var(--hair)}
.section-num{display:inline-block;background:var(--accent);color:var(--badge-ink);border-radius:4px;
padding:.05rem .45rem;margin-right:.6rem;font-size:1.1rem}
h4.subsection{color:var(--accent);font-size:1.1rem;margin:1.8rem 0 .6rem}
.box{margin:1.4rem 0;padding:.75rem 1rem;border-radius:4px}
.box-name{font-weight:bold;font-variant:small-caps;margin-right:.4rem}
.box-title{font-style:italic}
.box-title::before{content:'('}.box-title::after{content:')'}
.box-body p:first-child{margin-top:.3rem}
.box-body p:last-child{margin-bottom:0}
.theorem{padding:0;border:1.5px solid var(--theorem);background:color-mix(in srgb,var(--theorem) 5%,white);overflow:hidden}
.theorem .box-head{background:var(--theorem);color:#fff;padding:.35rem 1rem}
.theorem .box-body{padding:.5rem 1rem .8rem}
.definition{background:color-mix(in srgb,var(--definition) 8%,white);border-left:5px solid var(--definition);border-radius:0 4px 4px 0}
.definition .box-name{color:var(--definition)}
.formula{border:4px double var(--formula);background:color-mix(in srgb,var(--formula) 4%,white)}
.formula .box-name{color:var(--formula)}
.example{border-left:3px solid var(--example);border-radius:0;padding:.2rem 1rem}
.example .box-name{color:var(--example)}
.note{background:color-mix(in srgb,var(--note) 8%,white);border-left:2px solid var(--note);font-size:.95rem}
.note .box-name{color:var(--note)}
.warning{border:1.5px dashed var(--warning)}
.warning .box-name{color:var(--warning)}
.proof,.solution{margin:.8rem 0 1.2rem 1rem}
.qed{float:right}
.solution strong{color:var(--example)}
.objectives{border:1.5px solid var(--accent);border-radius:4px;margin:1.5rem 0;overflow:hidden}
.objectives-head{background:color-mix(in srgb,var(--accent) 10%,white);color:var(--accent);font-weight:bold;font-variant:small-caps;padding:.4rem 1rem}
.objectives ol{margin:.6rem 0;padding-left:2.6rem}
.epigraph{margin:1.5rem 0 2rem auto;max-width:62%;font-style:italic}
.epigraph footer{text-align:right;font-style:normal;color:var(--muted);font-size:.9rem}
.workspace{width:100%}
.lines{height:calc(var(--n) * 2.2rem);background:repeating-linear-gradient(transparent 0 calc(2.2rem - 1px),var(--hair) calc(2.2rem - 1px) 2.2rem)}
.plane{text-align:center;margin:1.2rem 0}
.plane svg{display:block;margin:0 auto}
math[display=block]{margin:.9rem 0}
.top-link{position:fixed;right:1.2rem;bottom:1.2rem;background:var(--accent);color:#fff;
padding:.45rem .8rem;border-radius:999px;font-size:.85rem;box-shadow:0 2px 8px rgba(0,0,0,.2)}
@media (max-width:640px){.toc ol ol,.chapter-toc{columns:1}.cover h1{font-size:2.2rem}.chapter h2{font-size:1.8rem}}
@media print{.top-link{display:none}.chapter{break-before:page}}
"

// ================================================================== NOTES ==
#let notes(
  title: "AP Calculus BC",
  subtitle: "Course Notes",
  course: "AP Calculus BC",
  school: none,
  theme: themes.classic,
  author: none,
  source: none,
  print: false,
  cover: true,
  contents: true,
  body,
) = {
  set document(title: title)
  set text(font: "New Computer Modern", size: 11pt, lang: "en")
  set par(justify: true, leading: 0.66em, spacing: 1.05em)
  // Pages only exist in the PDF; HTML export would warn about the rule.
  show: body => context {
    set page(
      width: _paper.width,
      height: _paper.height,
      margin: _margin,
      header-ascent: 40%,
      header: _header(),
      footer: _footer(course, contents),
    ) if not _html()
    // Browsers raise a superscript prime twice, so in HTML `f'` becomes a
    // plain f followed by the prime.
    let html = _html()
    show math.attach: it => {
      let f = it.fields()
      let key = ("t", "tr").find(k => f.at(k, default: none) != none and f.at(k).func() == math.primes)
      let others = f.keys().filter(k => k not in ("base", key) and f.at(k) != none)
      if html and key != none and others.len() == 0 {
        let n = f.at(key).count
        it.base
        math.class("normal", ("′", "″", "‴").at(n - 1, default: "′" * n))
      } else { it }
    }
    body
  }
  set heading(numbering: none)
  set list(indent: 0.5em, body-indent: 0.6em)
  set enum(indent: 0.5em, body-indent: 0.6em)
  set table(stroke: 0.5pt + luma(170), inset: 6pt)
  show math.equation.where(block: true): set block(above: 0.95em, below: 0.95em)
  show heading.where(level: 1): _chapter-heading
  show heading.where(level: 2): _section-heading
  show heading.where(level: 3): _subsection-heading
  // Boxes are figures, which normally refuse to split across pages.
  show figure: set block(breakable: true)
  show figure: it => if type(it.kind) == str and it.kind.starts-with("bc-") { _render-box(it) } else { it }
  show ref: it => {
    let el = it.element
    if el != none and el.func() == figure and type(el.kind) == str and el.kind.starts-with("bc-") {
      context link(el.location())[#el.supplement~#_number-at(el.location(), el.kind)]
    } else { it }
  }
  show outline.entry: _toc-entry

  _print.update(print)
  _theme.update(theme)
  context if _html() {
    html.elem("style", _css(if print { _grays } else { theme }))
    if contents { html.elem("a", attrs: (class: "top-link", href: "#bc-contents"))[↑ Contents] }
  }
  if cover { _cover(title, subtitle, course, school, author, source) }
  if contents { _contents() }
  counter(page).update(1)
  body
}
