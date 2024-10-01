#!/usr/bin/python3
import z3

m = 2**64 # put the mod value of the lcg. must be known

# need three terms, and the mod
seq = [122074694, 1086340560, 339298720] # put 3 sequence values generated from an LCG with any seed. (can use the lcg.py program)
assert len(seq) == 3

s0, s1, s2 = seq # list(map(lambda x: int(x * m), seq))

a, c = z3.BitVecs('a c', 64) #z3.Ints('a c')

solver = z3.Solver()

solver.add(a > 0, c > 0)
solver.add(s1 == z3.LShR(z3.URem((a * s0 + c), m), 32))
solver.add(s2 == z3.LShR(z3.URem((a * s1 + c),m), 32))

# PREDICTS INCCORECTLY!!!
if solver.check() == z3.sat:
    model = solver.model()

    print("a: ", model[a])
    print("c: ", model[c])
    predict = ((model[a].as_long() * s2 + model[c].as_long()) % m) >> 32
    print("next: ", predict) 