# 15 bit fibonacci lfsr with taps at 15 and 1.
# Feadback polynomial: x^15 + x + 1
def step(lfsr):
    bit = (lfsr >> 14) ^ lfsr
    lfsr = ((lfsr << 1) & 0x7FFF) | (bit & 1)
    return lfsr

def fib_lfsr(n, seed = 1):
    lfsr = step(seed)
    period = 1

    while lfsr != seed:
        lfsr = step(lfsr)
        period += 1
    
    return period

n = 6
rands = fib_lfsr(n)

print(rands)