SHORTEST PATHS LAB EXAMINATION - DA5300 LAB 9
==========================================

Structure follows the supplied BST lab ZIP, adapted for shortest paths.
This is a practice package prepared from the supplied Lab 9 PDF.
The command interface, tests and marking scheme are practice additions.

Student submits: rollnumber.py
Run: python rollnumber.py test.txt

Commands:
V n       start/reset a directed graph with n vertices (0..n-1)
E u v w   add directed edge u -> v with integer weight w
D s       Dijkstra distances from source s
B s       Bellman-Ford distances, or NEGATIVE CYCLE if reachable from s
F         Floyd-Warshall matrix, or NEGATIVE CYCLE if any cycle exists
C         True if any negative cycle exists, otherwise False

Unreachable distances print INF. Distance vectors use spaces (no brackets).
Matrix rows print on separate lines. D prints INVALID: NEGATIVE EDGE when
its adjacency matrix has a negative weight. Insertions print nothing.
Inputs use unique ordered edge pairs and no nonnegative self-loops; negative
self-loops are allowed. This preserves the PDF's provided matrix helper as-is.
Blank lines and lines beginning with # are ignored.

Student public check:
1. Complete shortest_paths_boilerplate.py.
2. Save/copy the completed program as shortest_paths.py.
3. Run: python public_evaluate.py
4. Public score is out of 5 (one mark per public test).

Reference answer:
python ans.py public1.txt
To check the provided answer with the public evaluator, copy ans.py to
shortest_paths.py first.

Examiner:
Put submissions in one folder, e.g. submissions/ID25M806.py.
Run: python evaluate.py submissions
Private score is out of 10; total is out of 15.
All 5 public and all 10 private tests and their expected outputs are included.
A test earns 1 mark only when all outputs match. Whitespace is normalized.
Timeout: 3 seconds per test. Python 3; standard library only.

Read QUESTIONS.md for tasks and ANSWERS.md for explanations and a correction
to the Floyd-Warshall matrix printed in the original PDF.
