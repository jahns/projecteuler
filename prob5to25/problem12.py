import numpy as np
import math
from itertools import combinations

# We define the nth triagnular number to be the sum of all positive integers less than n
# trianular = n*(n+1)/2
# n*(n+1) must be divisible by 2
# either n = 2k and n+1 = 2k+1 or n+1 = 2k and n = 2k - 1 
# leading to 2k*(2k+1)/2 = (4k^2 + 2k)/2 = 2k^2 + k
# or (2k-1)*2k/2 = (4k^2 - 2k)/2 = 2k^2 - k
# we are looking for k*(2k - 1) or k*(2k + 1) with 500 divisors
# k and 2k -1 or 2k + 1 coprime so we don't need to work about
# overlap. We can now look for k where factors(k*(2k +- 1)) = 500

def sumN(n):
    return int(n*(n+1)/2)

def countFactors(n):
    maxFactor = math.floor(math.sqrt(n))
    factorCount = 0
    for i in range(1, n+1):
        if n % i == 0:  
            factorCount += 1    
    return factorCount

k = 501 # simply because a number can't have more factors than numbers below it

while True:
    km = 2*k - 1 # 2k minus 1
    kp = 2*k + 1 # 2k plus 1

    
    # Count the factors in k*2km1 and k*2kp1
    fcountM = countFactors(km)
    fcountP = countFactors(kp)
    fcountK = countFactors(k)

    if fcountM*fcountK > 500:
        print(km*k)
        break
    if fcountP*fcountK > 500:
        print(kp*k)
        break

    k += 1
    
