"""
"""

from z3 import *

p = Bool('p')
q = Bool('q')
r = Bool('r')

f1 = Implies(p, q)
f2 = r == Not(q)
f3 = Or(Not(p), r)

s = Solver()
s.add(f1)
s.add(f2)
s.add(f2)
print s.check()
m = s.model()

# m
# m[p]
# m?
# bool(m[p])
# is_true(m[p])
# is_true?

p = Bool('p')
q = Bool('q')
print And(p, q, True)
print simplify(And(p, q, True))
print simplify(And(p, False))
