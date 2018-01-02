import math

# Given a list of primes check if n is divisble by any of them if it is return false
# otherwise return true
def isPrime(n, primes):
    for p in primes:
        if n % p == 0:
            return False
    return True

# Current number of primes
num_prime = 0
# List of primes found
prime_numbers = []
i = 2

while num_prime != 10001:
    if isPrime(i, prime_numbers):
        prime_numbers.append(i)
        num_prime += 1
    i += 1

# Print the answer
print(prime_numbers[-1])
