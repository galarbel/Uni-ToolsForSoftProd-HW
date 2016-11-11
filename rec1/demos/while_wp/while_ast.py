"""
AST (Abstract Syntax Tree) classes for While language
"""


# Abstract Classes

class AST(object):
    pass

class Expr(AST):
    pass

class ArithExpr(Expr):
    pass

class BoolExpr(Expr):
    pass

class Statement(AST):
    pass


# Statements

class Skip(Statement):
    def __repr__(self):
        return 'Skip()'
    def __str__(self):
        return 'skip'

class Assign(Statement):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    def __repr__(self):
        return 'Assign({}, {})'.format(self.lhs, self.rhs)
    def __str__(self):
        return '{} := {}'.format(self.lhs, self.rhs)

class Comp(Statement):
    def __init__(self, S1, S2):
        self.S1 = S1
        self.S2 = S2
    def __repr__(self):
        return 'Comp({}, {})'.format(self.S1, self.S2)
    def __str__(self):
        return '{} ; {}'.format(self.S1, self.S2)

class If(Statement):
    def __init__(self, b, S1, S2):
        self.b = b
        self.S1 = S1
        self.S2 = S2
    def __repr__(self):
        return 'If({}, {}, {})'.format(self.b, self.S1, self.S2)
    def __str__(self):
        return 'if ({}) then ({}) else ({})'.format(self.b, self.S1, self.S2)

class While(Statement):
    def __init__(self, b, I, S):
        self.b = b
        self.I = I
        self.S = S
    def __repr__(self):
        return 'While({}, {}, {})'.format(self.b, self.I, self.S)
    def __str__(self):
        return 'while ({}) invariant ({}) do ({})'.format(self.b, self.I, self.S)

class Assert(Statement):
    def __init__(self, b):
        self.b = b
    def __repr__(self):
        return 'Assert({})'.format(self.b)
    def __str__(self):
        return 'assert {}'.format(self.b)

class Assume(Statement):
    def __init__(self, b):
        self.b = b
    def __repr__(self):
        return 'Assume({})'.format(self.b)
    def __str__(self):
        return 'assume {}'.format(self.b)




# Arithmetic Expressions

class ALit(ArithExpr):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'ALit({})'.format(self.value)
    def __str__(self):
        return str(self.value)

class Var(ArithExpr):
    def __init__(self, var_name):
        self.var_name = var_name
    def __repr__(self):
        return 'Var({})'.format(self.var_name)
    def __str__(self):
        return self.var_name

class Plus(ArithExpr):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def __repr__(self):
        return 'Plus({}, {})'.format(self.a1, self.a2)

class Times(ArithExpr):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def __repr__(self):
        return 'Times({}, {})'.format(self.a1, self.a2)

class Minus(ArithExpr):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def __repr__(self):
        return 'Minus({}, {})'.format(self.a1, self.a2)


# Boolean Expressions

class BLit(ArithExpr):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'BLit({})'.format(self.value)

class Eq(BoolExpr):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def __repr__(self):
        return 'Eq({}, {})'.format(self.a1, self.a2)

class LE(BoolExpr):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def __repr__(self):
        return 'LE({}, {})'.format(self.a1, self.a2)

class Not(BoolExpr):
    def __init__(self, b):
        self.b = b
    def __repr__(self):
        return 'Not({})'.format(self.b)

class And(BoolExpr):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def __repr__(self):
        return 'And({}, {})'.format(self.b1, self.b2)

class Or(BoolExpr):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def __repr__(self):
        return 'Or({}, {})'.format(self.b1, self.b2)

class Implies(BoolExpr):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def __repr__(self):
        return 'Implies({}, {})'.format(self.b1, self.b2)

class ForAll(BoolExpr):
    def __init__(self, variables, b):
        self.variables = variables
        self.b = b
    def __repr__(self):
        return 'ForAll({}, {})'.format(self.variables, self.b)


# helper functions


def FV(e):
    """
    Returns the set of free variables in e
    """

    if type(e) is ALit:
        return set()

    elif type(e) is Var:
        return set([e.var_name])

    elif type(e) is Plus:
        return FV(e.a1) | FV(e.a2)

    elif type(e) is Times:
        return FV(e.a1) | FV(e.a2)

    elif type(e) is Minus:
        return FV(e.a1) | FV(e.a2)

    elif type(e) is BLit:
        return set()

    elif type(e) is Eq:
        return FV(e.a1) | FV(e.a2)

    elif type(e) is LE:
        return FV(e.a1) | FV(e.a2)

    elif type(e) is Not:
        return FV(e.b)

    elif type(e) is And:
        return FV(e.b1) | FV(e.b2)

    elif type(e) is Or:
        return FV(e.b1) | FV(e.b2)

    elif type(e) is Implies:
        return FV(e.b1) | FV(e.b2)

    elif type(e) is ForAll:
        return FV(e.b) - set(e.variables)

    else:
        assert False # Error


def substitute(e, x, y):
    """
    e is an expression
    returns the exoression obtained from e by substiting y instead of x.
    y is an expression
    x is a string - the name if a variable
    """

    if type(e) is ALit:
        return e

    elif type(e) is Var and e.var_name == x:
        return y

    elif type(e) is Var and e.var_name != x:
        return e

    elif type(e) is Plus:
        return Plus(substitute(e.a1, x, y), substitute(e.a2, x, y))

    elif type(e) is Times:
        return Times(substitute(e.a1, x, y), substitute(e.a2, x, y))

    elif type(e) is Minus:
        return Minus(substitute(e.a1, x, y), substitute(e.a2, x, y))

    elif type(e) is BLit:
        return e

    elif type(e) is Eq:
        return Eq(substitute(e.a1, x, y), substitute(e.a2, x, y))

    elif type(e) is LE:
        return LE(substitute(e.a1, x, y), substitute(e.a2, x, y))

    elif type(e) is Not:
        return Not(substitute(e.b, x, y))

    elif type(e) is And:
        return And(substitute(e.b1, x, y), substitute(e.b2, x, y))

    elif type(e) is Or:
        return Or(substitute(e.b1, x, y), substitute(e.b2, x, y))

    elif type(e) is Implies:
        return Implies(substitute(e.b1, x, y), substitute(e.b2, x, y))

    elif type(e) is ForAll and x in e.variables:
        return e

    elif type(e) is ForAll and x not in e.variables:
        return ForAll(e.variables, substitute(e.b, x, y))

    else:
        assert False # Error


def compose(statements):
    if len(statements) == 0:
        return Skip()
    elif len(statements) == 1:
        return statements[0]
    else:
        return Comp(compose(statements[:-1]), statements[-1])
