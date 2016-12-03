from z3 import *

I = IntSort()
A    = DeclareSort('A')
a, b = Consts('a b', A)
x, y = Consts('x y', I)

f = Function('f', I, A)
g = Function('g', A, I)
P = Function('P', A, BoolSort())

s = Solver()

s.set(timeout=5000)

# s.add(ForAll([x], g(f(x)) > x))


"""
s.add(ForAll([x], Implies(x % 2 == 0, P(f(x)))))

s.add(ForAll([x], Implies(x % 2 == 1, Not(P(f(x))))))

s.add(ForAll([a], Implies(P(a), g(a) % 2 == 1)))
s.add(ForAll([a], Implies(Not(P(a)), g(a) % 2 == 0)))

#s.add((x + g(f(x))) % 2 == 0)
#s.add((1 + g(f(1))) % 2 == 0)
#s.add(g(f(1)) == 1)

"""


s.add(ForAll([x], Implies(x > 0, P(f(x)))))
s.add(ForAll([x], Implies(x < 0, Not(P(f(x))))))
s.add(ForAll([a], Implies(P(a), g(a) < 0)))
s.add(ForAll([a], Implies(Not(P(a)), g(a) > 0)))

# s.add(ForAll([x], g(f(x)) > x))

#s.add((y * g(f(y))) < 0)

#s.add((5 + g(f(5))) % 2 == 0)

