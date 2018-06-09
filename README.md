# Motivation

Purpose of this repository is to test how we can

* store the graph in semantically meaningful way (MathML)
* automatically verify graph correctness using symbolic computation

# Current stage

There are four vertices in the graph and two edges. Vertices 1-3 are simple derivation using the two edges. Vertex 4 is an expression that second transition is using as a substitution (to show graph can use itself to derive things).

To check correctness run

`python test.py`

Expected output

```
* parsing edge transition1.xml...  OK
  LHS after inference rule...  OK
  RHS after inference rule...  OK
* parsing edge transition2.xml...  OK
  LHS after inference rule...  OK
  RHS after inference rule...  OK
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
