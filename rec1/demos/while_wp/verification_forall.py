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
    using ForAll for loop invariants
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
        e = And(Implies(And(S.b, S.I), WP(S.S, S.I)),
                Implies(And(Not(S.b), S.I), Q))
        return And(S.I, ForAll(FV(e), e))

    elif type(S) is Assert:
        return And(S.b, Q)

    elif type(S) is Assume:
        return Implies(S.b, Q)

    else:
        assert False # Error


def vc_gen(P, S, Q):
    """
    """
    return Implies(P, WP(S, Q))


def verify(P, S, Q):
    import z3
    from convert_to_z3 import to_z3

    vc = vc_gen(P, S, Q)
    vc_z3 = to_z3(vc)
    print "vc:"
    print vc
    print
    print "vc_z3:"
    print vc_z3
    print

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
