Purpose of this repository is to test how we can

* store the graph in semantically meaningful way (MathML)
* automatically verify graph correctness using symbolic computation

Current stage:

There are four vertices in the graph and two edges. Vertices 1-3 are simple derivation using the two edges. Vertex 4 is an expression that second transition is using as a substitution (to show graph can use itself to derive things).

To check correctness run

`python test.py`

To see the initial (hardcoded) example run

`python derive.py`
