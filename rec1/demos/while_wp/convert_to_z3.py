"""

Conversion of while_ast expressions to Z3

"""

import z3

from while_ast import *


def to_z3(e):
    """
    Convert expression to Z3 expression
    """

    if type(e) is ALit:
        return z3.IntVal(e.value)

    elif type(e) is Var:
        return z3.Int(e.var_name)

    elif type(e) is Plus:
        return to_z3(e.a1) + to_z3(e.a2)

    elif type(e) is Times:
        return to_z3(e.a1) *  to_z3(e.a2)

    elif type(e) is Minus:
        return to_z3(e.a1) - to_z3(e.a2)

    elif type(e) is BLit:
        return z3.BoolVal(e.value)

    elif type(e) is Eq:
        return to_z3(e.a1) == to_z3(e.a2)

    elif type(e) is LE:
        return to_z3(e.a1) <= to_z3(e.a2)

    elif type(e) is Not:
        return z3.Not(to_z3(e.b))

    elif type(e) is And:
        return z3.And(to_z3(e.b1), to_z3(e.b2))

    elif type(e) is Or:
        return z3.Or(to_z3(e.b1), to_z3(e.b2))

    elif type(e) is Implies:
        return z3.Implies(to_z3(e.b1), to_z3(e.b2))

    elif type(e) is ForAll:
        return z3.ForAll(
            [z3.Int(v) for v in e.variables],
            to_z3(e.b))

    else:
        assert False, e # Error
