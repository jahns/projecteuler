def nextCollatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

largest = -1
start = -1

for i in range(999999, 1, -1):
    count = 0
    nxt = nextCollatz(i)
    while nxt != 1:
        count += 1
        nxt = nextCollatz(nxt)
    if count > largest:
        largest = count
        start = i

print(start)

