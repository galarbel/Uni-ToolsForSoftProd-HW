"""
k-edge-coloring exercise.
"""
from z3 import *

DEBUG = False

Petersen_V = range(10)
Petersen_E = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),

    (0, 5),
    (1, 6),
    (2, 7),
    (3, 8),
    (4, 9),

    (5, 7),
    (7, 9),
    (9, 6),
    (6, 8),
    (8, 5),
]


def get_k_edge_coloring(k, V, E):
    assert V == range(len(V))
    colors = range(k)
    EdgeNumbers = range(len(E))

    variables = [[Bool('e_{}_color_{}'.format(e, c)) for c in colors] for e in EdgeNumbers]

    s = Solver()

    # every edge has at least one color
    for e in EdgeNumbers:
        s.add(Or([variables[e][c] for c in colors]))

    # every edge has at most one color
    for e in EdgeNumbers:
        for c1 in range(k):
            for c2 in range(c1 + 1, k):
                s.add(Or(Not(variables[e][c1]),
                         Not(variables[e][c2])))

    # every edge has different colors from it's neighbours
    for e in EdgeNumbers:
        v1, v2 = E[e]
        for i in range(e+1, len(EdgeNumbers)):
            if (v1 in E[i]) or (v2 in E[i]):
                for c in colors:
                    s.add(Or(Not(variables[e][c]),
                             Not(variables[i][c])))
    if DEBUG:
        print "Solver is:"
        print s
        print

        print "Checking SAT"
    res = s.check()

    if res == unsat or res == unknown:
        if DEBUG:
            print("UNSAT, No K coloring" if res == unsat else "UNKNOWN")
        return None

    assert res == sat
    if DEBUG:
        print "SAT, Found K coloring"
    m = s.model()
    coloring = dict()
    for e in EdgeNumbers:
        for c in colors:
            if is_true(m[variables[e][c]]):
                coloring[E[e]] = c
                break
    return coloring



def get_k_edge_coloring_core(k, V, E):
    #
    # Your solution here...
    #
    pass


def draw_graph(V, E, coloring={}, filename='graph', engine='circo', directed=False):
    try:
        from graphviz import Graph, Digraph
    except ImportError:
        print "You don't have graphviz python interface installed. Sorry."
        return

    COLORS = ['blue', 'red', 'green', 'pink', 'yellow']
    if directed:
        dot = Digraph(engine=engine)
    else:
        dot = Graph(engine=engine)
    for v in V:
        if v in coloring:
            dot.node(str(v), style="filled", fillcolor=COLORS[coloring[v]])
        else:
            dot.node(str(v))
    for v1, v2 in E:
        if (v1, v2) in coloring:
            dot.edge(str(v1), str(v2), color=COLORS[coloring[(v1, v2)]])
        else:
            dot.edge(str(v1), str(v2))
    dot.render(filename, cleanup=True, view=True)


if __name__ == '__main__':

    print("Peterson 4 col:")
    print(get_k_edge_coloring(4,Petersen_V,Petersen_E))
    print

    print("Peterson 3 col:")
    print(get_k_edge_coloring(3, Petersen_V, Petersen_E))
    print

    print("simple test graph: k=2 V=[0,1,2,3], E= [(0, 1), (0,2)]")
    print(get_k_edge_coloring(2, range(4), [(0, 1), (0, 2)]))
    print
    pass
