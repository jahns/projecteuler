import numpy as np

n = 2000000

# Make a list from 2 to n
up2n = np.array([i for i in range(n+1)])
up2n[1] = 0
p = 2

# Use a sieve to get only primes
while p < n:
    if up2n[p] != 0 and p*p < n:
        for i in range(p*p, n+1//p + 1, p):
            up2n[i] = 0
    p += 1

print(np.sum(up2n[up2n != 0]))
