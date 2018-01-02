import numpy as np
lines = [line.rstrip('\n') for line in open('./p067_triangle.txt')]
triangle = np.array([[int(col) for col in row.split(' ')] for row in lines])

for r in range(len(triangle) - 1, 0, -1):
    for c in range(len(triangle[r])-1):
        triangle[r-1][c] = max(triangle[r-1][c]+triangle[r][c], triangle[r-1][c]+triangle[r][c+1])

print(triangle[0])

