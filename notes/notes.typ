#import "template.typ": *
#import "@preview/cetz:0.5.2"
#import "@preview/cetz-plot:0.1.4": plot
#show: notes.with(
  theme: themes.carmel,
  title: "AP Calculus BC",
  subtitle: "Course Notes",
  source: [Based on Demana, Franklin D., et al. _Calculus: Graphical, Numerical, Algebraic._ 6th ed., AP ed., Pearson, 2020.],
  school: "Carmel Catholic High School",
  course: "Carmel Catholic · AP Calculus BC",
)

= Chapter 0 -- Prerequisites for Calculus

== Section 0.1 -- Linear Functions

=== Increments and Slope

Unlike algebra, calculus doesn't deal with exact values or inequalities.
Instead it deals with changing quantities, rates of change, and Increments.

#definition(title:"Increments")[
  The change in a variable is called an _increment_ in that variable.
  Let x be a variable.

  $ Delta x = x_2 - x_1$
]

Using increments, you cna find the _rate of change_ or slop of any _linear function_.
 
#definition(title: "Slope")[
  Let $(x_1, y_1)$ and $(x_2, y_2)$ be two points on the graph of a linear function.

  $ m = (Delta y)/(Delta x) "or" (y_2 - y_1)/(x_2 - x_1) $

  Such that $m$ is the slope.
]

=== Point-Slope Equation of a Linear Function

There are many ways to represent a linear function between two variables, but the most useful way in calculus is the Point-Slope Form.

#formula(title: "Point-slope form")[
  $ y - y_1 = m(x - x_1) $
]

=== Other Linear Equation Forms

Other forms will rarely be shown because the point-slope equation conveys the information so well, and it's very convenient for Calculus.

The slope-intercept form is very useful for modeling real world problems and is very popular in Algebra.

#formula(title: "Slope-intercept form")[
  $ y = m x + b $
]

The standard form is useful in linear algebra.

#formula(title: "Standard form")[
  $ A x + B y = C $
]

Contrary to the textbook (and Mr. T's hellish notes), the general linear form is it's own distinct thing.
I don't understand how the use for this differs from standard form, but I felt the need to distinguish between the two.

#formula(title: "General linear formula")[
  $ A x + B y + C = 0$
]

=== Parallel and Perpendicular Lines

Linear functions cna have parallel and perpendicular lines.
For a line to be parallel, it's slope must be equal.
For a line to be perpendicular, it's slope must be reciprocated and reflected.

#definition(title: "Perpendicular slope")[
  Let $m_1$ be a constant representing the slope of a linear equation.

  $ m_2 = - 1 / m_1 $
]

=== Applications of Linear Functions

// I need to fix this

Modeling a data set as a linear equation is a common use and relatively simple.
Find the slope and then use one pair fo values with the point slope form to determine the equation.

=== Solving Two Linear Equations Simultaneously 

// I need to fix this

Just like simplify it so one variable is on the same side and then divide by the coefficient so the system has both equations equal y or x or whatever.
Then, set them equal to each other, solve for some variable, and then input it into the equation from before that was set to equal y and that's y.
Boom. I don't wanna explain it but it's pretty easy.

== Section 0.2 -- Functions and Graphs

=== Functions

A function is a rule that relates exactly one output to every input in it's domain.
A function can be used to model nearly any relationship where one variable depends on another.

#definition(title: "Function")[
  $ y = f(x) $
]

=== Domains and Ranges

Every function has two important sets of values: the domain $D$ and the range $R$.
The domain is defined as the largest set of $x$ values for which the formula gives real $y$ values.
The range is defined as every valid output for a given function.
Domains and ranges of many real-valued functions of a real variables re intervals or combinations of interval. //rephrase
The intervals may be open, closed, or half-open and finite or infinite. //rephrase

=== Viewing and Interpreting Graphs

=== Even Functions and Odd Functions -- Symmetry

The graphs of _even_ and _odd_ functions have important symmetry properties.

#definition(title: "Even Function")[
  $ f(-x) = x $
]

#definition(title: "Odd Function")[
  $ f(-x) = -x $
]

Functions can be neither even or odd, and, in the specific case of $f(x)=0$, can be both even and odd.

You can also evaluate function party with the graph.
Even functions are symmetric with respect to the $y$-axis.
Odd functions are symmetric about the origin.

=== Piecewise-Defined Functions

Piecewise functions use more than one formula to define the output.

#definition(title:"Piecewise-defined functions")[
  $ f(x) = cases(
    g(x) "if" x > a,
    h(x) "otherwise",
  ) $
]

=== Absolute Value Function

#definition(title:"Absolute function")[
  $ |x| = cases(
    -x "if" x < 0,
    x "if" x >= 0
  ) $
]

=== Composite Functions

 

== Section 0.3 -- Exponential Functions

=== Exponential Growth

=== Exponential Decay

=== Compound Interest

=== The Number $e$

== Section 0.4 -- Parametric Equations

=== Relations

=== Circles

=== Ellipses

=== Lines and Other Curves

== Section 0.5 -- Inverse Functions and Logarithms

=== One-to-One Functions

=== Inverses

=== Finding Inverses

=== Logarithmic Functions

=== Properties of Logarithms

=== Applications

== Section 0.6 -- Trigonometric Functions

=== Radian Measure

=== Graphs of Trigonometric Functions

=== Periodicity

=== Even and Odd Trigonometric Functions

=== Transformations of Trigonometric Graphs

=== Inverse Trigonometric Functions

= Prologue -- Foundations of Calculus

== Section P.1 -- Velocity and Distance

=== Finding Distance

=== Finding Velocity

= Chapter 1 -- Limits and Continuity

== Section 1.1 -- Rates of Change and Limits

=== Average and Instantaneous Velocity

=== Definition of Limit

=== Properties of Limits

=== One-Sided and Two-Sided Limits

=== Squeeze Theorem

== Section 1.2 -- Limits Involving Infinity

=== Finite Limits as $x -> plus.minus infinity$

=== Squeeze Theorem Revisited

=== Infinite Limits as $x -> a$

=== End Behavior Models

=== "Seeing" Limits as $x -> plus.minus infinity$

== Section 1.3 -- Continuity

=== Continuity at a Point

=== Continuous Functions

=== Algebraic Combinations

=== Composites

=== Intermediate Value Theorem for Continuous Functions

== Section 1.4 -- Rates of Change, Tangent Lines, and Sensitivity

=== Average Rates of Change

=== Tangent to a Curve

=== Slope of a Curve

=== Normal to a Curve

=== Velocity Revisited

=== Sensitivity

= Chapter 2 -- Derivatives

== Section 2.1 -- Derivative of a Function

=== Definition of Derivative

=== Notation

=== Relationships Between the Graphs of $f$ and $f'$

=== Graphing the Derivative from Data

=== One-Sided Derivatives

== Section 2.2 -- Differentiability

=== How $f'(a)$ Might Fail to Exist

=== Differentiability Implies Local Linearity

=== Numerical Derivatives on a Calculator

=== Differentiability Implies Continuity

=== Intermediate Value Theorem for Derivatives

== Section 2.3 -- Rules for Differentiation

=== Positive Integer Powers, Multiples, Sums, and Differences

=== Products and Quotients

=== Negative Integer Powers of $x$

=== Second and Higher Order Derivatives

== Section 2.4 -- Velocity and Other Rates of Change

=== Instantaneous Rates of Change

=== Motion Along a Line

=== Sensitivity to Change

=== Derivatives in Economics

== Section 2.5 -- Derivatives of Trigonometric Functions

=== Derivative of the Sine Function

=== Derivative of the Cosine Function

=== Simple Harmonic Motion

=== Jerk

=== Derivatives of the Other Basic Trigonometric Functions

= Chapter 3 -- More Derivatives

== Section 3.1 -- Chain Rule

=== Derivative of a Composite Function

=== "Outside-Inside" Rule

=== Repeated Use of the Chain Rule

=== Slopes of Parametrized Curves

=== Power Chain Rule

== Section 3.2 -- Implicit Differentiation

=== Implicitly Defined Functions

=== Lenses, Tangents, and Normal Lines

=== Derivatives of Higher Order

=== Rational Powers of Differentiable Functions

== Section 3.3 -- Derivatives of Inverse Trigonometric Functions

=== Derivatives of Inverse Functions

=== Derivative of the Arcsine

=== Derivative of the Arctangent

=== Derivative of the Arcsecant

=== Derivatives of the Other Three

== Section 3.4 -- Derivatives of Exponential and Logarithmic Functions

=== Derivative of $e^x$

=== Derivative of $a^x$

=== Derivative of $ln x$

=== Derivative of $log_a x$

=== Power Rule for Arbitrary Real Powers

= Chapter 4 -- Applications of Derivatives

== Section 4.1 -- Extreme Values of Functions

=== Absolute (Global) Extreme Values

=== Local (Relative) Extreme Values

=== Finding Extreme Values

== Section 4.2 -- Mean Value Theorem

=== Mean Value Theorem

=== Physical Interpretation

=== Increasing and Decreasing Functions

=== Other Consequences

== Section 4.3 -- Connecting _f′_ and _f″_ with the Graph of _f_

=== First Derivative Test for Local Extrema

=== Concavity

=== Points of Inflection

=== Second Derivative Test for Local Extrema

=== Learning About Functions from Derivatives

== Section 4.4 -- Modeling and Optimization

=== A Strategy for Optimization

=== Examples from Mathematics

=== Examples from Business and Industry

=== Examples from Economics

=== Modeling Discrete Phenomena with Differentiable Functions

== Section 4.5 -- Linearization, Sensitivity, and Differentials

=== Linear Approximation

=== Differentials

=== Sensitivity Analysis

=== Absolute, Relative, and Percentage Change

=== Sensitivity to Change

=== Newton's Method

=== Newton's Method May Fail

== Section 4.6 -- Related Rates

=== Related Rate Equations

=== Solution Strategy

=== Simulating Related Motion

= Chapter 5 -- The Definite Integral

== Section 5.1 -- Estimating with Finite Sums

=== Accumulation Problems as Area

=== Rectangular Approximation Method (RAM)

=== Volume of a Sphere

=== Cardiac Output

== Section 5.2 -- Definite Integrals

=== Riemann Sums

=== Terminology and Notation of Integration

=== Definite Integral as an Accumulator Function

=== Definite Integral and Area

=== Constant Functions

=== Integrals on a Calculator

=== Discontinuous Integrable Functions

== Section 5.3 -- Definite Integrals and Antiderivatives

=== Properties of Definite Integrals

=== Average Value of a Function

=== Mean Value Theorem for Definite Integrals

=== Connecting Differential and Integral Calculus

== Section 5.4 -- Fundamental Theorem of Calculus

=== Fundamental Theorem, Antiderivative Part

=== Graphing the Accumulator Function $integral_a^x f(t) dif t$

=== Fundamental Theorem, Evaluation Part

=== The Real Meaning of the Fundamental Theorem

=== Area Connection

=== Analyzing Antiderivatives Graphically

== Section 5.5 -- Trapezoidal Sums

=== Trapezoidal Approximations

=== Other Algorithms

=== Error Analysis

= Chapter 6 -- Differential Equations and Mathematical Modeling

== Section 6.1 -- Slope Fields and Euler's Method

=== Differential Equations

=== Slope Fields

=== Euler's Method

== Section 6.2 -- Antidifferentiation by Substitution

=== Indefinite Integrals

=== Leibniz Notation and Antiderivatives

=== Substitution in Indefinite Integrals

=== Substitution in Definite Integrals

== Section 6.3 -- Antidifferentiation by Parts

=== Product Rule in Integral Form

=== Solving for the Unknown Integral

=== Tabular Integration

=== Inverse Trigonometric and Logarithmic Functions

== Section 6.4 -- Exponential Growth and Decay

=== Separable Differential Equations

=== Law of Exponential Change

=== Continuously Compounded Interest

=== Radioactivity

=== Modeling Growth with Other Bases

=== Newton's Law of Cooling

== Section 6.5 -- Logistic Growth

=== How Populations Grow

=== Partial Fractions

=== The Logistic Differential Equation

=== Logistic Growth Models

= Chapter 7 -- Applications of Definite Integrals

== Section 7.1 -- Accumulation and Net Change

=== Linear Motion Revisited

=== General Strategy

=== Accumulation of a Rate over Time

=== Coming and Going

=== Net Change from Data

=== Density

=== Work

== Section 7.2 -- Areas in the Plane

=== Area Between Curves

=== Area Enclosed by Intersecting Curves

=== Boundaries with Changing Functions

=== Integrating with Respect to $y$

=== Saving Time with Geometry Formulas

== Section 7.3 -- Volumes

=== Volume as an Integral

=== Square Cross Sections

=== Circular Cross Sections

=== Cylindrical Shells

=== Other Cross Sections

== Section 7.4 -- Lengths of Curves

=== A Sine Wave

=== Length of a Smooth Curve

=== Vertical Tangents, Corners, and Cusps

== Section 7.5 -- Applications from Science and Statistics

=== Work Revisited

=== Fluid Force and Fluid Pressure

=== Normal Probabilities

= Chapter 8 -- Sequences, L'Hospital's Rule, and Improper Integrals

== Section 8.1 -- Sequences

=== Defining a Sequence

=== Arithmetic and Geometric Sequences

=== Graphing a Sequence

=== Limit of a Sequence

== Section 8.2 -- L'Hospital's Rule

=== Indeterminate Form $0\/0$

=== Indeterminate Forms $infinity\/infinity$, $infinity dot 0$, $infinity - infinity$

=== Indeterminate Forms $1^infinity$, $0^0$, $infinity^0$

== Section 8.3 -- Relative Rates of Growth

=== Comparing Rates of Growth

=== Using L'Hospital's Rule to Compare Growth Rates

=== Sequential versus Binary Search

== Section 8.4 -- Improper Integrals

=== Infinite Limits of Integration

=== Integrands with Infinite Discontinuities

=== Test for Convergence and Divergence

=== Applications

= Chapter 9 -- Infinite Series

== Section 9.1 -- Power Series

=== Geometric Series

=== Representing Functions by Series

=== Differentiation and Integration

=== Identifying a Series

== Section 9.2 -- Taylor Series

=== Constructing a Series

=== Series for $sin x$ and $cos x$

=== Beauty Bare

=== Maclaurin and Taylor Series

=== Combining Taylor Series

=== Table of Maclaurin Series

== Section 9.3 -- Taylor's Theorem

=== Taylor Polynomials

=== The Remainder

=== Bounding the Remainder

=== Analyzing Truncation Error

=== Euler's Formula

== Section 9.4 -- Radius of Convergence

=== Convergence

=== $n$th-Term Test

=== Comparing Nonnegative Series

=== Ratio Test

=== Endpoint Convergence

== Section 9.5 -- Testing Convergence at Endpoints

=== Integral Test

=== Harmonic Series and $p$-series

=== Comparison Tests

=== Alternating Series

=== Absolute and Conditional Convergence

=== Intervals of Convergence

=== A Word of Caution

= Chapter 10 -- Parametric, Vector, and Polar Functions

== Section 10.1 -- Parametric Functions

=== Parametric Curves in the Plane

=== Slope and Concavity

=== Arc Length

=== Cycloids

== Section 10.2 -- Vectors in the Plane

=== Two-Dimensional Vectors

=== Vector Operations

=== Modeling Planar Motion

=== Velocity, Acceleration, and Speed

=== Displacement and Distance Traveled

== Section 10.3 -- Polar Functions

=== Polar Coordinates

=== Polar Curves

=== Slopes of Polar Curves

=== Areas Enclosed by Polar Curves

=== Spiral of Archimedes
