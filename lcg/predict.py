#!/usr/bin/python3
import z3

m = 2**31 # put the mod value of the lcg. must be known

# need three terms, and the mod
seq = [0.9080880177207291, 0.1794773512519896, 0.38375180261209607] # put 3 sequence values generated from an LCG with any seed. (can use the lcg.py program)
assert len(seq) == 3

s0, s1, s2 = list(map(lambda x: int(x * m), seq))

a, c = z3.Ints('a c')

solver = z3.Solver()

solver.add(a > 0, c > 0)
solver.add(s1 == ((a * s0 + c) % m))
solver.add(s2 == ((a * s1 + c) % m))

if solver.check() == z3.sat:
    model = solver.model()

    print("a: ", model[a])
    print("c: ", model[c])
    predict = ((model[a].as_long() * s2 + model[c].as_long()) % m) / m
    print("next: ", predict) 