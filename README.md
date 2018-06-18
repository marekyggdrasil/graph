# Motivation

Purpose of this repository is to test how we can

* store the graph in semantically meaningful way (MathML)
* automatically verify graph correctness using symbolic computation

# Current stage

There are four vertices in the graph and two edges. Vertices 1-3 are simple derivation using the two edges. Vertex 4 is an expression that second transition is using as a substitution (to show graph can use itself to derive things).

To check correctness run

`python -m unittest -v tests.graph tests.parsing`

Expected something like following as an output

```
testApply (tests.graph.GraphTest) ... ok
testParsing (tests.graph.GraphTest) ... ok
testSubstitute (tests.graph.GraphTest) ... ok
testAddition (tests.parsing.ParsingTest) ... ok
testMultiplication (tests.parsing.ParsingTest) ... ok
testSubtraction (tests.parsing.ParsingTest) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.110s

OK
```

To see the initial (hardcoded) example run

`python derive.py`

Expected output

```
temporarily, as demonstration, it can only derive equation vert3 from vert1

C = E

apply D + eq to both sides of equation

C + D = D + E

substitute with lhs of m + n = x*y*z, map values as {'m': 'C', 'n': 'D'}

x*y*z = D + E

#

```
