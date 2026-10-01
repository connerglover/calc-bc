#import "template.typ": *
#import "@preview/cetz:0.5.2"
#import "@preview/cetz-plot:0.1.4": plot
#show: notes.with(
  theme: themes.carmel,
  title: "AP Calculus BC",
  subtitle: "Course Notes",
  source: [Based on Hass, Joel, et al. _Thomas' Calculus: Early Transcendentals._ 15th ed., Global ed., Pearson Education Limited, 2024.],
  school: "Carmel Catholic High School",
  course: "Carmel Catholic · AP Calculus BC",
)

= Chapter 1 -- Functions

#note[This chapter is review from Precalculus.
I think this chapter is mostly supplemental.
But it's in the textbook and is important for the AP test.]

== Section 1.1 -- Functions and Their Graphs

Functions are a tool for modeling the real world.
They can be represented by an equation, a graph, a table, or a verbal description.

=== Functions; Domain and Range

In each case, the value of one variable depends on the value of another.
In most cases, $y$ is a function of $x$, symbolically represented as $y = f(x)$.
The symbol $f$ represents the function, the letter $x$ is the input or, more accurately, _independent variable_, and $y$ is the _dependent variable_ or output value of $f$ at $x$.
A rule is classified as a function if and only if there is exactly one output for all possible inputs.

#definition()[A _function_ $f$ from a set $D$ to a set $Y$ is a rule that assigns a single value $f(x)$ in $Y$ to each $x$ in $D$.]

The set $D$ represents all possible input values and is called the _domain_. 
The domain of $f$ would sometimes be denoted by $D(f)$.
The _natural domain_ is the largest set of real $x$-values for which the formula gives real y-values. 

The set of all output values $f(x)$ as $x$ varies through $D$ is called the _range_ of the function.
A function is said to be _real-valued_ when its range is a set of real numbers.

Often a function is given by a formula that describes how to calculate the output value from the input variable.
For instance, $y = x^2$.

=== Graphs of Functions

If $f$ is a function with domain $D$, its _graph_ contains the points in the Cartesian plane whose coordinates are the input-output pairs for $f$.
In set notation the graph is ${(x, f(x))|x in D}$.

To graph a function, plot the points $(x,y)$ that satisfy the equation on a Cartesian plane, and draw a smooth curve (labeled with its equation) through the plotted points.

=== Representing a Function Numerically

Another way functions can be represented is _numerically_ through a table of values.
Using this table, a graph of the function can be sketched.
A graph containing only the points in the table is called a _scatterplot_.

=== The Vertical Line Test for a Function

A function can only have one value $f(x)$ for each $x$ in $D(f)$. 
If $a$ is in the domain of the function $f$, then the vertical line $x=a$ will intersect the graph of $f$ at a single point $(a, f(a))$.

=== Piecewise-Defined Functions

Sometimes a function is described in pieces by using different formulas on different parts of its domain.
It's written as

$ f(x) = cases(
  g(x) & x < -1,
  h(x) & -1 <= x < 1,
  i(x) & x >= 1,
) $

=== Increasing and Decreasing Functions

Functions are classified based on how they respond to increasing inputs to understand the direction of change in a system.

#definition[Let $f$ be a function defined on an interval $I$ and let $x_1$ and $x_2$ be two distinct points in $I$.
+ If $f(x_2) > f(x_1)$ whenever $x_1 < x_2$, then $f$ is said to be _increasing_ on $I$. 
+ If $f(x_2) < f(x_1)$ whenever $x_1 < x_2$, then $f$ is said to be _decreasing_ on $I$.
]

=== Even Functions and Odd Functions: Symmetry

Functions can be categorized by their geometric symmetry to simplify algebraic analysis and graphing.

#definition[Let $f$ be a function and let $y = f(x)$
+ If $f(-x)=f(x)$ for all $x$ in $D(f)$, then $f$ is said to be an _even function of $x$_.
+ If $f(-x)=-f(x)$ for all $x$ in $D(f)$, then $f$ is said to be an _odd function of $x$_.
]

The graph of an even function is _symmetric about the $y$-axis_, and the graph of an odd function is _symmetric about the origin_.
A graph is symmetric about the origin if a rotation of $180 degree$ about the origin leaves the graph unchanged.

=== Common Functions

A variety of important types of functions are frequently encountered in calculus.

==== Linear Functions

A _linear function_ is a function of the form $f(x) = m x + b,$ where $m$ and $b$ are constants.
Its graph is a line with slope $m$ and $y$-intercept $b$.

Linear functions are special because their rate of change is constant.
The $b$'s cancel and the factor $x_2 - x_1$'s cancels, so the average rate of change between _any_ two points is $m$.
No other kind of function has this property.

#formula(title: "Slope-intercept form")[
  $ y = m x + b $
]

Since the slope is constant, a single point $(x_1, y_1)$ and the slope $m$ can model the whole line.
This is made simple with the point-slope form.

#formula(title: "Point-slope form")[
  $ y - y_1 = m (x - x_1) $
]

==== Power Functions

A _power function_ is a function of the form $f(x) = x^a$, where $a$ is constant.
Depending on the value of $a$, the function can behave in several ways.

In the case of $f(x) = x^a$, where $a$ is a positive integer, the domain is all real numbers and the graph passes through $(0, 0)$ and $(1, 1)$.
If $a$ is even, the graph of the function is even, and its range is $[0, oo)$.
If $a$ is odd, the graph of the function is odd, and its range is $(-oo, oo)$.
As $a$ increases, the graph gets flatter on $(-1, 1)$ and steeper for $|x| > 1$.

In the case of $f(x) = x^a$, where $a$ is a negative integer, the function is $1\/x^(-a)$ and $0$ is excluded from its domain.
If $a$ is even, the graph of the function is even, increasing for negative $x$, decreasing for positive $x$, and its range is the positive real numbers.
If $a$ is odd, the graph of the function is odd and decreasing on each side of zero.

In the case of $f(x) = x^a$, where $a = p\/q$ is a fraction in lowest terms, the function is $(root(q, x))^p$.
If $q$ is even, the domain is the nonnegative real numbers, since even roots of negative numbers are undefined.
If $q$ is odd, the domain is all real numbers.
If $p$ is even, the range is the nonnegative real numbers (positive if $a < 0$).
If $a$ is negative, zero is also excluded from the domain.

==== Polynomials

A _polynomial_ is a function of the form $f(x) = a_n x^n + a_(n-1) x^(n-1) + dots.c + a_1 x + a_0$, where $n$ is a nonnegative integer, called the degree, and the numbers $a_0, a_1, dots.c, a_n$ are real constants, called the coefficients.
The domain is $(-oo,oo)$ for all polynomials.

==== Rational Functions

A _rational function_ is a function of the form $f(x) = p(x)/q(x)$, where p and q are polynomials.
The domain is all real numbers for which $q(x) != 0$.

==== Algebraic Functions

An _algebraic function_ is a function constructed from polynomials using algebraic operations (addition, multiplication, division, taking roots).
All rational functions are algebraic, but not all algebraic functions are rational.

==== Trigonometric Functions

The six basic _trigonometric functions_ are functions that relate an angle to a ratio of side lengths in a right triangle.
They are discussed further in Section 1.3.

==== Exponential Functions

An _exponential function_ is a function of the form $f(x) = a^x$, where $a > 0$ and $a != 1$.
They are discussed further in Section 1.4.

==== Logarithmic Functions

A _logarithmic function_ is a function of the form $f(x) = log_a x$, where the base $a != 1$ is a positive constant.
They are the _inverse functions_ of exponential functions.
They are discussed further in Section 1.5.

==== Transcendental Functions

A _transcendental function_ is any non-algebraic functions, such as the trigonometric functions, inverse trigonometric, exponential, logarithmic functions. 

== Section 1.2 -- Combining Functions; Shifting and Scaling Graphs

Functions can be combined or transformed in many ways to form new functions and better model real-world situations.

=== Sums, Differences, Products, and Quotients

Functions can be added, subtracted, multiplied, and divided to produce new functions. Functions can also be multiplied by constants.
Suppose $f$ and $g$ are functions and $c$ is a real number.

#table(
  columns: 3,
  table.header[Functions][Formula][Domain],
  [$f + g$], [$(f + g)(x) = f(x) + g(x)$], [$D(f) inter D(g)$],
  [$f - g$], [$(f - g)(x) = f(x) - g(x)$], [$D(f) inter D(g)$],
  [$f times g$], [$(f times g)(x) = f(x) times g(x)$], [$D(f) inter D(g)$],
  [$f \/ g$], [$ (f / g)(x) = f(x) / g(x) $], [$D(f) inter D(g)$ at which $g(x) != 0$],
  [$c times f$], [$(c times f)(x) = c times f(x)$], [$D(f)$]
)

The operator on the left-hand side represents an operation between functions while the operator on the right-hand side represents an operation between the real numbers $f(x)$ and $g(x)$.

=== Composing Functions

Functions can be combined through composition, where the output from one function becomes the input to another.

#definition(title: "Function composition")[
  Suppose $f$ and $g$ are functions.

  $ (f compose g)(x) = f(g(x)) $

  is the composition of $f$ and $g$.
  The domain of $f compose g$ consists of the numbers $x$ in $D(g)$ for which $g(x)$ lies in the domain of $f$.
]

=== Shifting a Graph of a Function

Functions can be shifted by adding a constant to either the output of the existing function or the input variable.

#formula(title: "Vertical Shifts")[
  #columns(2)[
    $y = f(x) + k$

    #colbreak()

    Shifts the graph of $f$ _up_ $k$ units if $k > 0$\
    Shifts the graph of $f$ _down_ $abs(k)$ units if $k < 0$
  ]
  
]

#formula(title: "Horizontal Shifts")[
  #columns(2)[
    $y = f(x + h)$

    #colbreak()

    Shifts the graph of $f$ _left_ $h$ units if $h > 0$\
    Shifts the graph of $f$ _right_ $abs(h)$ units if $h < 0$
  ]
]

=== Scaling and Reflecting a Graph of a Function

Functions can be scaled by multiplying either the output of the existing function or the input variable by a constant $c$, where $c > 1$.
Reflections across the coordinate axes are special cases where $c = -1$.

#formula(title: "Vertical stretch")[
  #columns(2)[
    $y = c f(x)$

    #colbreak()

    Stretches the graph of $f$ vertically by a factor of $c$.
  ]
]

#formula(title: "Vertical compression")[
  #columns(2)[
    $y = 1/c f(x)$

    #colbreak()

    Compresses the graph of $f$ vertically by a factor of $c$.
  ]
]

#formula(title: "Horizontal stretch")[
  #columns(2)[
    $y = f(x\/c)$

    #colbreak()

    Stretches the graph of $f$ horizontally by a factor of $c$.
  ]
]

#formula(title: "Horizontal compression")[
  #columns(2)[
    $y = f(c x)$

    #colbreak()

    Compresses the graph of $f$ horizontally by a factor of $c$.
  ]
]

#formula(title: "Vertical reflection")[
  #columns(2)[
    $y = -f(x)$

    #colbreak()

    Reflects the graph of $f$ across the $x$-axis.
  ]
]

#formula(title: "Horizontal reflection")[
  #columns(2)[
    $y = f(-x)$

    #colbreak()

    Reflects the graph of $f$ across the $y$-axis.
  ]
]

== Section 1.3 -- Trigonometric Functions

=== Angles

=== The Six Basic Trigonometric Functions

=== Periodicity and Graphs of the Trigonometric Functions

=== Trigonometric Identities

=== The Law of Cosines

=== Transformations of Trigonometric Graphs

=== Two Special Inequalities

== Section 1.4 -- Exponential Functions

=== Exponential Behavior

=== The Natural Exponential Function $e^x$

=== Exponential Growth and Decay

== Section 1.5 -- Inverse Functions and Logarithms

=== One-to-One Functions

=== Inverse Functions

=== Finding Inverses

=== Logarithmic Functions

=== Properties of Logarithms

=== Applications

=== Inverse Trigonometric Functions

=== The Arcsine and Arccosine Functions

=== Identities Involving Arcsine and Arccosine

= Chapter 2 -- Limits and Continuity

== Section 2.1 -- Rates of Change and Tangent Lines to Curves

=== Average and Instantaneous Speed

=== Defining the Slope of a Curve

=== Average Rates of Change and Secant Lines

=== Rates of Change and Tangent Lines

== Section 2.2 -- Limit of a Function and Limit Laws

=== An Informal Description of the Limit of a Function

=== Limits of Function Values

=== The Limit Laws

=== Eliminating Common Factors from Zero Denominators

=== Evaluating Limits of Polynomials and Rational Functions

=== Using Calculators and Computers to Estimate Limits

=== The Sandwich Theorem

== Section 2.4 -- One-Sided Limits

=== Approaching a Limit from One Side

=== Limits at Endpoints of an Interval

=== Precise Definitions of One-Sided Limits

=== Limits Involving $(sin theta)\/theta$

== Section 2.5 -- Limits Involving Infinity; Asymptotes of Graphs

=== Finite Limits as $x -> plus.minus infinity$

=== Limits at Infinity of Rational Functions

=== Horizontal Asymptotes

=== Oblique Asymptotes

=== Infinite Limits

=== Precise Definitions of Infinite Limits

=== Vertical Asymptotes

=== Dominant Terms

== Section 2.6 -- Continuity

=== Continuity at a Point

=== Continuous Functions

=== Inverse Functions and Continuity

=== Continuity of Compositions of Functions

=== Intermediate Value Theorem for Continuous Functions

=== Continuous Extension to a Point

= Chapter 3 -- Derivatives

== Section 3.1 -- Tangent Lines and the Derivative at a Point

=== Finding a Tangent Line to the Graph of a Function

=== Rates of Change: Derivative at a Point

== Section 3.2 -- The Derivative as a Function

=== Calculating Derivatives from the Definition

=== Notation

=== Graphing the Derivative

=== Differentiability on an Interval; One-Sided Derivatives

=== When Does a Function Not Have a Derivative at a Point?

=== Differentiable Functions Are Continuous

== Section 3.3 -- Differentiation Rules

=== Powers, Multiples, Sums, and Differences

=== Derivatives of Exponential Functions

=== Products and Quotients

=== Second- and Higher-Order Derivatives

== Section 3.4 -- The Derivative as a Rate of Change

=== Instantaneous Rates of Change

=== Motion Along a Line: Displacement, Velocity, Speed, Acceleration, and Jerk

=== Derivatives in Economics and Biology

=== Sensitivity to Change

== Section 3.5 -- Derivatives of Trigonometric Functions

=== Derivative of the Sine Function

=== Derivative of the Cosine Function

=== Simple Harmonic Motion

=== Derivatives of the Other Basic Trigonometric Functions

== Section 3.6 -- The Chain Rule

=== Derivative of a Composite Function

=== “Outside-Inside” Rule

=== Repeated Use of the Chain Rule

=== The Chain Rule with Powers of a Function

== Section 3.7 -- Implicit Differentiation

=== Implicitly Defined Functions

=== Derivatives of Higher Order

=== Lenses, Tangent Lines, and Normal Lines

== Section 3.8 -- Derivatives of Inverse Functions and Logarithms

=== Derivatives of Inverses of Differentiable Functions

=== Derivative of the Natural Logarithm Function

=== The Derivatives of $a^x$ and $log_a x$

=== Logarithmic Differentiation

=== Irrational Exponents and the Power Rule (General Version)

=== The Number $e$ Expressed as a Limit

== Section 3.9 -- Inverse Trigonometric Functions

=== Inverses of $tan x$, $cot x$, $sec x$, and $csc x$

=== The Derivative of $y = arcsin u$

=== The Derivative of $y = arctan u$

=== The Derivative of $y = op("arcsec") u$

=== Derivatives of the Other Three Inverse Trigonometric Functions

== Section 3.10 -- Related Rates

=== Related Rates Equations

== Section 3.11 -- Linearization and Differentials

=== Linearization

=== Differentials

=== Estimating with Differentials

=== Error in Differential Approximation

=== Proof of the Chain Rule

=== Sensitivity to Change

=== Converting Mass to Energy

= Chapter 4 -- Applications of Derivatives

== Section 4.1 -- Extreme Values of Functions on Closed Intervals

=== Local (Relative) Extreme Values

=== Finding Extrema

== Section 4.2 -- The Mean Value Theorem

=== Rolle’s Theorem

=== The Mean Value Theorem

=== A Physical Interpretation

=== Mathematical Consequences

=== Finding Velocity and Position from Acceleration

== Section 4.3 -- Monotonic Functions and the First Derivative Test

=== Increasing Functions and Decreasing Functions

=== First Derivative Test for Local Extrema

== Section 4.4 -- Concavity and Curve Sketching

=== Concavity

=== Points of Inflection

=== Second Derivative Test for Local Extrema

=== Graphical Behavior of Functions from Derivatives

== Section 4.5 -- Indeterminate Forms and L’Hôpital’s Rule

=== Indeterminate Form $0\/0$

=== Indeterminate Forms $infinity\/infinity$, $infinity dot 0$, $infinity - infinity$

=== Indeterminate Powers

=== Proof of L’Hôpital’s Rule

== Section 4.6 -- Applied Optimization

=== Examples from Mathematics and Physics

=== Examples from Economics

== Section 4.8 -- Antiderivatives

=== Finding Antiderivatives

=== Initial Value Problems and Differential Equations

=== Antiderivatives and Motion

=== Indefinite Integrals

= Chapter 5 -- Integrals

== Section 5.1 -- Area and Estimating with Finite Sums

=== Area

=== Distance Traveled

=== Displacement Versus Distance Traveled

=== Average Value of a Nonnegative Continuous Function

== Section 5.2 -- Sigma Notation and Limits of Finite Sums

=== Finite Sums and Sigma Notation

=== Limits of Finite Sums

=== Riemann Sums

== Section 5.3 -- The Definite Integral

=== Definition of the Definite Integral

=== Integrable and Nonintegrable Functions

=== The Midpoint Rule

=== Properties of Definite Integrals

=== Area Under the Graph of a Nonnegative Function

=== Average Value of a Continuous Function Revisited

== Section 5.4 -- The Fundamental Theorem of Calculus

=== Mean Value Theorem for Definite Integrals

=== Fundamental Theorem, Part 1

=== Fundamental Theorem, Part 2 (The Evaluation Theorem)

=== The Integral of a Rate

=== The Relationship Between Integration and Differentiation

=== Total Area

== Section 5.5 -- Indefinite Integrals and the Substitution Method

=== Substitution: Running the Chain Rule Backwards

=== Trying Different Substitutions

== Section 5.6 -- Definite Integral Substitutions and the Area Between Curves

=== The Substitution Formula

=== Definite Integrals of Symmetric Functions

=== Areas Between Curves

=== Integration with Respect to y

= Chapter 6 -- Applications of Definite Integrals

== Section 6.1 -- Volumes Using Cross-Sections

#note[Disk and washer methods, plus solids with known cross-sections. The AP exam does not require cylindrical shells (6.2).]

=== Slicing by Parallel Planes

=== Solids of Revolution: The Disk Method

=== Solids of Revolution: The Washer Method

== Section 6.3 -- Arc Length

=== Length of a Curve $y = f(x)$

=== Dealing with Discontinuities in $dif y\/dif x$

=== The Differential Formula for Arc Length

= Chapter 7 -- Integrals and Transcendental Functions

== Section 7.2 -- Exponential Change and Separable Differential Equations

#note[Separable differential equations and exponential growth and decay. Logistic growth is in 16.4.]

=== Exponential Change

=== Separable Differential Equations

=== Unlimited Population Growth

=== Radioactivity

=== Heat Transfer: Newton’s Law of Cooling

= Chapter 8 -- Techniques of Integration

== Section 8.1 -- Using Basic Integration Formulas

== Section 8.2 -- Integration by Parts

=== Product Rule in Integral Form

=== Evaluating Definite Integrals by Parts

== Section 8.5 -- Integration of Rational Functions by Partial Fractions

#note[AP only tests partial fractions with distinct linear factors in the denominator.]

=== General Description of the Method

=== Determining Coefficients by Differentiating

== Section 8.7 -- Numerical Integration

#note[The Trapezoidal Rule is tested; Simpson’s Rule is not.]

=== Approximating Integrals with the Midpoint Rule

=== Trapezoidal Approximations

=== Simpson’s Rule: Approximations Using Parabolas

=== Error Analysis

== Section 8.8 -- Improper Integrals

=== Infinite Limits of Integration

=== The Integral $integral_1^infinity dif x\/x^p$

=== Integrands with Vertical Asymptotes

=== Improper Integrals with a CAS

=== Tests for Convergence and Divergence

= Chapter 9 -- Infinite Sequences and Series

== Section 9.1 -- Sequences

=== Representing Sequences

=== Convergence and Divergence

=== Calculating Limits of Sequences

=== Using L’Hôpital’s Rule

=== Commonly Occurring Limits

=== Recursive Definitions

=== Bounded Monotonic Sequences

== Section 9.2 -- Infinite Series

=== Geometric Series

=== The $n$th-Term Test for a Divergent Series

=== Combining Series

=== Adding or Deleting Terms

=== Reindexing

== Section 9.3 -- The Integral Test

=== The Integral Test

=== Nondecreasing Partial Sums

=== Error Estimation

== Section 9.4 -- Comparison Tests

=== The Limit Comparison Test

== Section 9.5 -- Absolute Convergence; The Ratio and Root Tests

#note[The Ratio Test is tested; the Root Test is not.]

=== The Ratio Test

=== The Root Test

== Section 9.6 -- Alternating Series and Conditional Convergence

=== Conditional Convergence

=== Rearranging Series

=== Summary of Tests to Determine Convergence or Divergence

== Section 9.7 -- Power Series

=== Power Series and Convergence

=== The Radius of Convergence of a Power Series

=== Operations on Power Series

== Section 9.8 -- Taylor and Maclaurin Series

=== Series Representations

=== Taylor and Maclaurin Series

=== Taylor Polynomials

== Section 9.9 -- Convergence of Taylor Series

#note[Emphasize the Lagrange Error Bound (Taylor’s Theorem with remainder).]

=== Estimating the Remainder

=== Using Taylor Series

=== A Proof of Taylor’s Theorem

== Section 9.10 -- Applications of Taylor Series

=== The Binomial Series for Powers and Roots

=== Evaluating Nonelementary Integrals

=== Arctangents

=== Evaluating Indeterminate Forms

=== Euler’s Identity

= Chapter 10 -- Parametric Equations and Polar Coordinates

== Section 10.1 -- Parametrizations of Plane Curves

=== Parametric Equations

=== Cycloids

=== Brachistochrones and Tautochrones

== Section 10.2 -- Calculus with Parametric Curves

=== Tangent Lines and Areas

=== Length of a Parametrically Defined Curve

=== Length of a Curve $y = f(x)$

=== The Arc Length Differential

=== Areas of Surfaces of Revolution

== Section 10.3 -- Polar Coordinates

=== Definition of Polar Coordinates

=== Polar Equations and Graphs

=== Relating Polar and Cartesian Coordinates

== Section 10.4 -- Graphing Polar Coordinate Equations

=== Symmetry

=== Slope

=== Converting a Graph from the $r theta$-Plane to the $x y$-Plane

== Section 10.5 -- Areas and Lengths in Polar Coordinates

#note[AP tests area in polar coordinates. Polar arc length is not tested.]

=== Area in the Plane

=== Length of a Polar Curve

= Chapter 12 -- Vector-Valued Functions and Motion in Space

== Section 12.1 -- Curves in Space and Their Tangents

#note[AP covers plane curves only. Treat vector-valued functions as $⟨x(t), y(t)⟩$.]

=== Limits and Continuity

=== Derivatives and Motion

=== Differentiation Rules

=== Vector Functions of Constant Length

== Section 12.2 -- Integrals of Vector Functions; Projectile Motion

#note[Focus on recovering position from velocity and on displacement vs. total distance traveled.]

=== Integrals of Vector Functions

=== The Vector and Parametric Equations for Ideal Projectile Motion

=== Projectile Motion with Wind Gusts

= Chapter 16 -- First-Order Differential Equations

== Section 16.1 -- Solutions, Slope Fields, and Euler’s Method

#note[Slope fields and Euler’s method.]

=== General First-Order Differential Equations and Solutions

=== Slope Fields: Viewing Solution Curves

=== Euler’s Method

== Section 16.4 -- Graphical Solutions of Autonomous Equations

#note[Logistic growth: the carrying capacity and where the population grows fastest.]

=== Equilibrium Values and Phase Lines

=== Stable and Unstable Equilibria

=== Newton’s Law of Cooling

=== A Falling Body Encountering Resistance

=== The Logistic Model for Population Growth

=== The Logistic Equation in Neural Networks and Machine Learning
