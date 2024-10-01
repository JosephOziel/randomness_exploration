# https://github.com/rossilor95/lcg-python/blob/main/lcg.py

from typing import Iterator

def lcg(m: int, a: int, c: int, seed: int) -> Iterator[int]:
    x = seed
    while True:
        yield x
        x = (a * x + c) % m

def rand_float_samples(n_samples: int, seed: int = 354132778823482374) -> list[float]:
    m: int = 2**64
    a: int = 6364136223846793005
    c: int = 1442695040888963407

    shift = 32 # 32 if mod is 2^64, 16 if mod is 2^32
    gen = lcg(m, a, c, seed)
    sequence_div = []
    sequence = []
    seq_short = []

    for i in range(0, n_samples):
        rand: float = next(gen)
        sequence_div.append(rand / m)
        sequence.append(rand)
        seq_short.append(rand >> shift)

    return (sequence_div, sequence, seq_short)

n = 15
rand_sequence_div, rand_sequence, seq_short = rand_float_samples(n)

# print(rand_sequence_div)
print("full: %s\n" % rand_sequence)
print("16 bit shifed: %s" % seq_short)