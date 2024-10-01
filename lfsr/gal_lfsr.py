# 31 bit Galois lfsr with taps at 31 and 4 (should be as good as 31 and 28 while producing "more random" numbers)
# Feedback polynomial: x^31 + x^4 + 1
def step(lfsr):
    return (lfsr >> 1) ^ (0x40000080 * (lfsr & 1))

def gal_lfsr(n, seed = (1 << 30 | 1)):
    lfsr = seed
    rands = [(seed, seed & 1)]
    
    for i in range(n):
        lfsr = step(lfsr)
        rands.append((lfsr, lfsr & 1))

    return rands

n = 20
rands = gal_lfsr(n)

print([x[0] for x in rands])
print(tuple([x[1] for x in rands]))