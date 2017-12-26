import numpy as np
import math
from itertools import combinations

def sumN(n):
    return int(n*(n+1)/2)

def countFactors(n):
    up2n = np.array([i for i in range(1, n + 1)])
    return len(up2n[n % up2n == 0])

for i in range(250, 2000):
    if countFactors(sumN(i)) > 100:
        print(countFactors(sumN(i)))
