# Lab 9 answers

Complete runnable implementation: `ans.py`. Function signatures match the PDF.

## Part A

Distances: `[0, 3, 4, 1, 3]`.
Dijkstra finalises the closest unprocessed vertex. With negative edges, a later
path may improve a finalised distance. For example, edges (0,1,2), (0,2,5),
(2,1,-4) give distance 1 to vertex 1, although it is initially finalised at 2.

## Part B

Result: `([0, 2, 7, 4, -2], False)`.
A simple path has at most V-1 edges. After that many full relaxation passes,
an additional possible improvement indicates a reachable negative cycle.
Ignore unreachable starting vertices during relaxation and cycle detection.

## Part C - correction to the PDF

The correct all-pairs matrix for the actual Part B edges is:

```text
0 2 7 4 -2
INF 0 8 3 -4
INF -5 0 -3 -9
INF -2 6 0 -6
INF 5 13 7 0
```

Some entries in the PDF's printed expected matrix are incorrect. For example,
1 -> 4 -> 3 has cost -4 + 7 = 3, improving the printed distance 5; and
2 -> 3 -> 1 has cost -3 - 2 = -5, so this entry is reachable, not INF.
The original PDF is included unchanged. Tests use the corrected matrix.
A negative diagonal means a vertex has a negative-cost closed walk, which
implies a negative cycle. With no negative cycles, each diagonal remains zero.

## Part D

Adding (4,1,-1) creates cycle 1 -> 4 -> 1 of weight -5, reachable from 0.
Bellman-Ford's cycle flag is True. Floyd-Warshall has negative diagonal entries
for vertices 1, 3 and 4. Repeated traversals of the negative cycle decrease path
cost without limit. From source 0, distances to 1, 3 and 4 are unbounded below;
0 and 2 still have finite shortest distances 0 and 7 respectively.
The Bellman-Ford working array and Floyd-Warshall entries associated with the
cycle are not finite shortest distances. The CLI prints NEGATIVE CYCLE.

## Part E - complexity and scope

| Algorithm | Time | Auxiliary space | Scope |
|---|---|---|---|
| Dijkstra, matrix scan | O(V^2) | O(V) | One source, nonnegative weights |
| Bellman-Ford | O(VE), up to V-1 passes plus cycle check | O(V) | One source, negative edges allowed |
| Floyd-Warshall | O(V^3) | O(V^2) | All pairs, negative edges allowed |

The input adjacency matrix itself uses O(V^2) space. Bellman-Ford early stopping
can reduce work on a particular graph. Its cycle flag only covers cycles
reachable from its source; Floyd-Warshall's diagonal check covers every component.
The provided helper assumes ordinary unique ordered edge pairs in the practice
inputs. Do not change it silently to a different parallel-edge convention.
