from while_ast import *


prog1 = compose([
    Assume(Eq(Var('x'), ALit(0))),
    
    Assign('x', Plus(Var('x'), ALit(1))),
    
    If(Eq(Var('x'), ALit(1)),
       Assign('y', ALit(2)),
       Assign('y', ALit(3))),
    
    Assert(Eq(Var('y'), ALit(2))),
])


prog2 = compose([
    Assume(Eq(Var('x'), ALit(0))),
    
    Assign('x', Plus(Var('x'), ALit(1))),
    
    If(Eq(Var('x'), ALit(1)),
       Assign('y', ALit(2)),
       Assign('y', ALit(3))),
    
    Assert(Eq(Var('y'), ALit(3))),
])


prog3 = compose([
    Assign('i', ALit(0)),
    #Assign('j', ALit(1)),
    Assume(LE(ALit(1), Var('j'))),

    While(LE(Var('i'), Var('n')),
          LE(ALit(0), Var('i')),
          #And(LE(ALit(0), Var('i')), LE(ALit(0), Var('j'))),
          Assign('i', Plus(Var('i'), Var('j'))))

    #Assert(Eq(Var('y'), ALit(3))),
])

prog4 = compose([
    Assume(Eq(Var('x'), Var('x0'))),
    Assume(Eq(Var('y'), Var('y0'))),

    Assume(LE(ALit(0), Var('x'))),
    Assume(LE(ALit(0), Var('y'))),

    While(Not(LE(Var('y'), ALit(0))),
          #BLit(True),

          #Eq(Plus(Var('x'), Var('y')),
          #   Plus(Var('x0'), Var('y0'))),

          And(
              And(LE(ALit(0), Var('x')), LE(ALit(0), Var('y'))),
              Eq(Plus(Var('x'), Var('y')), Plus(Var('x0'), Var('y0')))),
          
          compose([
              Assign('x', Plus(Var('x'), ALit(1))),
              Assign('y', Minus(Var('y'), ALit(1))),
          ])),

    Assert(Eq(Var('x'), Plus(Var('x0'), Var('y0')))),
])
