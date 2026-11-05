"""Lab 9 reference solution. Run: python ans.py public1.txt

Dijkstra finalises the nearest unprocessed vertex. A negative edge can later
improve an already finalised distance, breaking that greedy argument.
Example: 0->1 (2), 0->2 (5), 2->1 (-4): the true distance to 1 is 1.

Bellman-Ford needs at most V-1 passes when no reachable negative cycle exists:
a simple path contains at most V-1 edges. An extra improvement detects a
reachable negative cycle. Repeating it makes affected distances unbounded below.
The returned finite working array must NOT be treated as shortest distances
when has_negative_cycle is True.

Floyd-Warshall: after phase k, intermediate vertices are restricted to 0..k.
A negative dist[v][v] reveals a negative closed walk and hence a negative cycle.

Complexities (matrix Dijkstra): time O(V^2), auxiliary space O(V).
Bellman-Ford: time O(V*E), auxiliary space O(V).
Floyd-Warshall: time O(V^3), auxiliary space O(V^2).
Adjacency matrix itself takes O(V^2) space.
"""
import sys


def make_adjacency_matrix(V, edges):
    # Provided helper from the PDF: later repeated edges overwrite earlier ones.
    INF = float('inf')
    W = [[INF] * V for _ in range(V)]
    for i in range(V):
        W[i][i] = 0
    for u, v, w in edges:
        W[u][v] = w
    return W


def dijkstra(W, source):
    """Return single-source distances; reject negative edge weights."""
    V = len(W)
    if any(w < 0 for row in W for w in row):
        raise ValueError('Dijkstra requires non-negative edge weights')
    dist = [float('inf')] * V
    dist[source] = 0
    used = [False] * V
    for _ in range(V):
        u = -1
        for v in range(V):
            if not used[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        if u == -1 or dist[u] == float('inf'):
            break
        used[u] = True
        for v in range(V):
            if not used[v] and dist[u] + W[u][v] < dist[v]:
                dist[v] = dist[u] + W[u][v]
    return dist


def bellman_ford(V, edges, source):
    """Return (dist, has_negative_cycle), considering source-reachable cycles."""
    INF = float('inf')
    dist = [INF] * V
    dist[source] = 0
    for _ in range(V - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    has_negative_cycle = any(
        dist[u] != INF and dist[u] + w < dist[v] for u, v, w in edges
    )
    return dist, has_negative_cycle


def floyd_warshall(W):
    """Return a new all-pairs distance matrix without changing W."""
    V = len(W)
    dist = [row[:] for row in W]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def format_distances(dist):
    return ' '.join('INF' if x == float('inf') else str(x) for x in dist)


def process_file(filename):
    V = None
    edges = []
    out = []
    with open(filename, encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            p = line.split()
            cmd = p[0].upper()
            if cmd == 'V':
                V = int(p[1])
                edges = []
                if V < 1:
                    raise ValueError('V must be positive')
                continue
            if V is None:
                raise ValueError('Start with V n')
            if cmd == 'E':
                u, v, w = map(int, p[1:])
                if not (0 <= u < V and 0 <= v < V):
                    raise ValueError('Invalid vertex')
                edges.append((u, v, w))
            elif cmd in ('D', 'B'):
                source = int(p[1])
                if not 0 <= source < V:
                    raise ValueError('Invalid source')
                if cmd == 'D':
                    W = make_adjacency_matrix(V, edges)
                    if any(w < 0 for row in W for w in row):
                        out.append('INVALID: NEGATIVE EDGE')
                    else:
                        out.append(format_distances(dijkstra(W, source)))
                else:
                    dist, negative = bellman_ford(V, edges, source)
                    out.append('NEGATIVE CYCLE' if negative else format_distances(dist))
            elif cmd in ('F', 'C'):
                dist = floyd_warshall(make_adjacency_matrix(V, edges))
                negative = any(dist[i][i] < 0 for i in range(V))
                if cmd == 'C':
                    out.append(str(negative))
                elif negative:
                    out.append('NEGATIVE CYCLE')
                else:
                    out.extend(format_distances(row) for row in dist)
            else:
                raise ValueError(f'Unknown command: {cmd}')
    return out


def main():
    if len(sys.argv) != 2:
        print('Usage: python ans.py test.txt')
        sys.exit(2)
    print('\n'.join(process_file(sys.argv[1])))


if __name__ == '__main__':
    main()
