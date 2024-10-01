from pylfsr import LFSR

state = list(map(int, [*bin(1 << 30 | 1)[2:]]))

fpoly = [5,3]

L = LFSR(fpoly=fpoly, initstate=state)

k=20

seq_k = L.runKCycle(k)

print(L.arr2str(seq_k))

# IS THIS LIBRARY BROKEN??