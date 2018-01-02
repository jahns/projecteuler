# a^2 + b^2 = c^2
# a + b + c = 1000
# c = 1000 - a - b
# c = sqrt(a^2 + b^2)
# sqrt(a^2 + b^2) = 1000 - a - b
# a^2 + b^2 = (1000 - a - b)^2
# Triangle inequality
#a + b > c
# a + b > 1000 - a - b
# 2a + 2b > 1000
# a + b > 500
# Following some algebra for a^2 + b^2 = (1000 - a - b)^2
# b = (1000*(a - 500))/(a-1000)
# 0 < a < 500
import math

def isInteger(a):
    return math.floor(a) == a

for a in range(1, 500):
    b = (1000*(a - 500))/(a-1000)
    c = 1000 - a - b
    if a**2 + b**2 == c**2 and isInteger(a) and isInteger(b) and isInteger(c):
        print(str(a) + ' : ' + str(b) + ' : ' + str(c))

 
