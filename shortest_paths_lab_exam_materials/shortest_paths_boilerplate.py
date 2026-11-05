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
    """Return distances from source; W has non-negative edge weights."""
    # TODO: Initialise distances and processed flags.
    # TODO: Select the unprocessed vertex of minimum distance and relax edges.
    pass


def bellman_ford(V, edges, source):
    """Return (dist, has_negative_cycle); detect source-reachable cycles only."""
    # TODO: Initialise, relax for up to V-1 passes, and stop early if unchanged.
    # TODO: Check whether one more relaxation is possible.
    pass


def floyd_warshall(W):
    """Return a copied all-pairs shortest-distance matrix."""
    # TODO: Copy W; use k, i, j loops; return the result.
    pass


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
        print('Usage: python shortest_paths.py test.txt')
        sys.exit(2)
    print('\n'.join(process_file(sys.argv[1])))


if __name__ == '__main__':
    main()
