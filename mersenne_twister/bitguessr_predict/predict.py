# factor vals.factor | python predict.py

import random 
import sys
from mt_predictor import MT19937Predictor

predictor = MT19937Predictor()
for _ in range(624):
    x = int(sys.stdin.readline())
    print(x) #random.getrandbits(32)
    predictor.setrandbits(x, 32)

print("----------")
for _ in range(25):
    print(f"given: {sys.stdin.readline()} -- predicted: {predictor.getrandbits(32) % 2}")