from collections import defaultdict

FILE_NAME = r'aoc2024/day23/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = [x.split('-') for x in f.read().splitlines()]

    connections = defaultdict(set)
    for pc1, pc2 in data:
        connections[pc1].add(pc2)
        connections[pc2].add(pc1)
    return connections


def bron_kerbosch(graph, P=None, R=None, X=None):
    """
    Bron-Kerbosch algorithm to find largest cliques in a graph.
    Returns a generator of cliques
    """
    P = set(graph.keys()) if P is None else P
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        vertex = P.pop()
        yield from bron_kerbosch(graph, P=P & graph[vertex], R=R | {vertex}, X=X & graph[vertex])
        X.add(vertex)


if __name__ == '__main__':
    candidates = [pc for pc in connections if pc.startswith('t')]
    pc_trios = {tuple(sorted((pc, pc2, pc3))) for pc in candidates
                for pc2 in connections[pc] for pc3 in connections[pc2]
                if pc in connections[pc3]}

    answer_23a = len(pc_trios)
    print(f'{answer_23a}')

    cliques = sorted(bron_kerbosch(connections), key=len, reverse=True)
    answer_23b = ','.join(sorted(cliques[0]))
    print(f'{answer_23b}')