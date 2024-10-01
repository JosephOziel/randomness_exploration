# 31 bit fibonacci lfsr with taps at 31 and 28.
# Feadback polynomial: x^31 + x^28 + 1
def fib_lfsr(n, seed = (1 << 30 | 1)):
    lfsr = seed
    rands = [(seed, seed & 1)]

    for i in range(n):
        bit = (lfsr >> 30) ^ (lfsr >> 27)
        lfsr = ((lfsr << 1) & 0x7FFFFFFF) | (bit & 1)
        rands.append((lfsr, lfsr & 1))
    
    return rands

n = 20
rands = fib_lfsr(n)

print([x[0] for x in rands])
print(tuple([x[1] for x in rands]))

# doesnt look super random