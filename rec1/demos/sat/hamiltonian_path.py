"""
Example of reduction from Hamiltonian path SAT
"""

from z3 import *
from k_coloring import draw_graph

Petersen_V = range(10)
Petersen_E = [
    (0 , 1),
    (1 , 2),
    (2 , 3),
    (3 , 4),
    (4 , 0),

    (0 , 5),
    (1 , 6),
    (2 , 7),
    (3 , 8),
    (4 , 9),

    (5 , 7),
    (7 , 9),
    (9 , 6),
    (6 , 8),
    (8 , 5),
 ]

simple_V = [0, 1, 2, 3]
simple_E = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3),
]

nopath_V = [0, 1, 2, 3]
nopath_E = [
    (0, 1),
    (1, 2),
    (2, 0),
    (0, 3),
    (1, 3),
    (2, 3),
]

def get_hamiltonian_path(V, E, directed=False):
    n = len(V)
    assert V == range(n)
    steps = range(n)

    variables = [[Bool('v_{}_step_{}'.format(v, i)) for i in steps] for v in V]

    s = Solver()

    # every node must appear at least once
    for v in V:
        s.add(Or([variables[v][i] for i in steps]))

    # every node must appear at most once
    for v in V:
        for i in range(n):
            for j in range(i + 1, n):
                s.add(Or(Not(variables[v][i]),
                         Not(variables[v][j])))

    # every step has at least one node
    for i in steps:
        s.add(Or([variables[v][i] for v in V]))

    # every step has at most one node
    for i in steps:
        for v1 in range(n):
            for v2 in range(v1 + 1, n):
                s.add(Or(Not(variables[v1][i]),
                         Not(variables[v2][i])))

    EE = set()
    for v1, v2 in E:
        EE.add((v1, v2))
        if not directed:
            EE.add((v2, v1))
    # Non-adjacent nodes v1 and v2 cannot be adjacent in the path
    for v1 in V:
        for v2 in V:
            if (v1, v2) not in EE:
                for i in range(n-1):
                    s.add(Or(Not(variables[v1][i]),
                             Not(variables[v2][i+1])))
                    
    print "Solver is:"
    print s
    print

    print "Checking SAT"
    res = s.check()
    if res == unsat:
        print "UNSAT, No Hamiltonian path"
        return None
    elif res == unknown:
        print "Unknown"
        return None
    else:
        assert res == sat
        print "SAT, Found Hamiltonian path"
        m = s.model()
        path = []
        for i in steps:
            for v in V:
                if is_true(m[variables[v][i]]):
                    path.append(v)
                    break
        return path

def path_to_coloring(path):
    coloring = {}
    for i in range(len(path)-1):
        coloring[(path[i], path[i+1])] = 1
        coloring[(path[i+1], path[i])] = 1
    return coloring

if __name__ == '__main__':
    p = get_hamiltonian_path(simple_V, simple_E)
    c = path_to_coloring(p)
    draw_graph(simple_V, simple_E, c, 'simple')

    p = get_hamiltonian_path(Petersen_V, Petersen_E)
    c = path_to_coloring(p)
    draw_graph(Petersen_V, Petersen_E, c, 'Petersen')
