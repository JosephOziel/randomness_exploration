#!/usr/bin/python3
import z3
from math import gcd
from functools import reduce

# finding the mod

k = 10 # arbitrary. the higher it is, the better chance we have at guessing the mod

# these values must be the integers (before dividing by m)
seq = [1581808122, 631874002, 485004106, 1943069666, 2118607642, 216855154, 46071146, 234557826, 184882746, 912368914] # put as many items generated in the lcg as k
assert len(seq) == k

pairs = [(seq[x], seq[x+1]) for x in range(0, len(seq)-1)]
t_n = list(map(lambda p: p[1] - p[0], pairs))
triples = [(t_n[x], t_n[x+1], t_n[x+2]) for x in range(0, len(t_n)-2)]
u_n = list(map(lambda t: abs((t[2]*t[0])-(t[1])**2), triples))

def gcd_m(*numbers):
    return reduce(gcd, numbers)

m = gcd_m(*u_n)

seq = [0.42485488299280405, 0.2548829959705472, 0.9643918434157968] # put 3 sequence values generated from an LCG with any seed. (can use the lcg.py program)
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
    print("m: ", m)
    predict = ((model[a].as_long() * s2 + model[c].as_long()) % m) / m
    print("next: ", predict)