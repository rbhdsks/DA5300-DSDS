# DA5300 Laboratory 9 - Shortest Paths in Graphs

Practice format adapted to match the supplied BST lab package. The original
assignment is included as `DA5300_2026_Lab9.pdf`. The command protocol and test
scores are additions for local practice, not official course instructions.

## Input and output

Implement the three functions in `shortest_paths_boilerplate.py`. Keep the
provided matrix helper, file parser and main function. Use the exact function
signatures from the PDF. See `README.txt` for commands and output conventions.
Graphs are directed; missing edges use `float('inf')`, and diagonals start at 0.

## Part A - Dijkstra

Implement `dijkstra(W, source)` for nonnegative weights using repeated minimum
selection and edge relaxation. Return the distances from source to every vertex.
Construct the matrix with the supplied helper. Explain why negative edges can
invalidate Dijkstra's greedy choice.

Graph: V = 5, source = 0.
Edges: (0,1,4), (0,3,1), (3,1,2), (1,2,1), (2,4,3), (3,4,2).
Expected distances: `[0, 3, 4, 1, 3]`.

## Part B - Bellman-Ford

Implement `bellman_ford(V, edges, source)` directly on the edge list. Relax all
edges for at most V-1 passes, stop early if unchanged, and check one extra pass
for a source-reachable negative cycle. Return `(dist, has_negative_cycle)`.

Graph: V = 5, source = 0.
Edges: (0,1,6), (0,2,7), (1,2,8), (1,3,5), (1,4,-4), (2,3,-3),
(2,4,9), (3,1,-2), (4,3,7).
Expected result: `([0, 2, 7, 4, -2], False)`.

## Part C - Floyd-Warshall

Implement `floyd_warshall(W)` using a copy of W and k as the outermost loop.
Return the all-pairs distance matrix. Use Part B's graph. Explain why a negative
diagonal entry reveals a negative cycle. The corrected matrix is in ANSWERS.md;
the PDF's displayed matrix contains incorrect entries.

## Part D - Negative-cycle experiment

Add (4,1,-1) to Part B's graph. Run Bellman-Ford from 0 and Floyd-Warshall.
Report source-reachable cycle detection and negative diagonal detection.
Explain why distances to affected vertices are unbounded below.

## Part E - Run and compare

Use the function calls in the original PDF and the public test files. Compare
time and auxiliary-space complexity of all three implementations. Explain the
difference between detecting a cycle reachable from one source and detecting a
cycle anywhere in a graph. Do not report finite distances as shortest distances
when a relevant negative cycle exists.
