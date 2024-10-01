# https://www.youtube.com/watch?v=ELA8gNNMHoU
import random
from operator import add, sub

n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    op = random.choice([add, sub])
    next_number = op(num1, num2)
print()