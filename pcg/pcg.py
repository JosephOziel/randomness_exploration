# https://www.pcg-random.org/
# created from c implementation pcg-basic
class PCG:
    def __init__(self, state = int('0x853c49e6748fea9b', 16), inc = int('0xda3e39cb94b95bdb', 16)):
        self._state = state
        self._inc = inc

    def pcg32_srandom(self, initstate, initseq):
        self._state = 0
        self._inc = (initseq << 1) | 1
        self.pcg32_random()
        self._state += initstate
        self.pcg32_random()

    # def pcg32_random(self):
    #     oldstate = self._state
    #     self._state = oldstate * 6364136223846793005 + self._inc # the lcg part (with the multiplier!)
    #     xorshifted = ((oldstate >> 18) ^ oldstate) >> 27
    #     xorshifted = xorshifted & 0xFFFFFFFF
    #     rot = oldstate >> 59
    #     res = (xorshifted >> rot) | (xorshifted << ((-rot) & 31))
    #     return res & 0xFFFFFFFF

    def pcg32_random(self):
        oldstate = self._state
        self._state = oldstate * 6364136223846793005 + self._inc & (1 << 64) - 1
        xorshifted = ((oldstate >> 18) ^ oldstate) >> 27 & (1 << 32) - 1
        rot = oldstate >> 59
        res = (xorshifted >> rot) | (xorshifted << ((-rot) & 31))
        return res & (1 << 32) - 1
    
    def pcg32_boundedrand(self, bound):
        threshold = -bound % bound

        while True:
            r = self.pcg32_random()
            if r >= threshold:
                return r % bound
            
pcg = PCG()
import time
pcg.pcg32_srandom(int(time.time()), 69)

# not 32-bit numbers
for i in range(5):
    print(pcg.pcg32_boundedrand(6))