#factors
from math import sqrt
n = 70
num = n
list = []
for i in range(1,int(sqrt(num))):
    if num % i == 0:
        list.append(i)
        if num % i != i:
            list.append(num//i)
list.sort()
print(list)
        