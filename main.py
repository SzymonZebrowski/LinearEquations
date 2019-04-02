import numpy as np

N = 965
e = 1

a = np.ones((3, 3))
for i in range(0,3):
    for j in range(0,3):
        print(a[i][j], end=' ')
    print("\n")
