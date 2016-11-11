"""
Verification based on weakest liberal precondition (WP) for While language

Implemented according to
http://www.cs.tau.ac.il/~shachar/dl/cav2013.pdf (CAV 2013):
Tables 3 and 4

Other sources:
https://www.lri.fr/~marche/MPRI-2-36-1/2013/poly1.pdf
https://www.lri.fr/~marche/MPRI-2-36-1/2013/slides1.pdf

"""

from while_ast import *


def WP(S, Q):
    """
    Returns the weakest liberal precondition for statement S and formula Q

    Implements Table 3 in CAV 2013
    """

    if type(S) is Skip:
        return Q

    elif type(S) is Assign:
        return substitute(Q, S.lhs, S.rhs)

    elif type(S) is Comp:
        return WP(S.S1, WP(S.S2, Q))

    elif type(S) is If:
        return And(
            Implies(S.b, WP(S.S1, Q)),
            Implies(Not(S.b), WP(S.S2, Q)),
        )

    elif type(S) is While:
        return S.I

    elif type(S) is Assert:
        return And(S.b, Q)

    elif type(S) is Assume:
        return Implies(S.b, Q)

    else:
        assert False # Error

def vc_aux(S, Q):
    """
    Returns VC_aux

    VC_aux is represented as a list of formulas

    Implements Table 4 in CAV 2013
    """
    #return []
    if type(S) in [Skip, Assign, Assert, Assume]:
        return []

    elif type(S) is Comp:
        return vc_aux(S.S1, WP(S.S2, Q)) + vc_aux(S.S2, Q)

    elif type(S) is If:
        return vc_aux(S.S1, Q) + vc_aux(S.S2, Q)

    elif type(S) is While:
        return vc_aux(S.S, S.I) + [
            Implies(And(S.b, S.I), WP(S.S, S.I)),
            Implies(And(Not(S.b), S.I), Q),
            ]

    else:
        assert False # Error


def vc_gen(P, S, Q):
    """
    """
    vc = Implies(P, WP(S, Q))
    for f in vc_aux(S, Q):
        vc = And(vc, f)
    return vc


def verify(P, S, Q):
    import z3
    from convert_to_z3 import to_z3

    vc = vc_gen(P, S, Q)
    vc_z3 = to_z3(vc)
    print vc
    print vc_z3

    s = z3.Solver()
    s.add(z3.Not(vc_z3))
    res = s.check()
    if res == z3.sat:
        print "SAT, counter example found:"
        m = s.model()
        print m
    elif res == z3.unsat:
        print "UNSAT, program verified!"
    else:
        print res


if __name__ == '__main__':
    from examples import *

    prog = prog4

    print prog
    print
    verify(BLit(True), prog, BLit(True))
