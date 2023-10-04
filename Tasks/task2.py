#complete

import numpy as np 
A=[]
N = int(input('Insert no of row for square matrix: '))
A = [[int(input()) for x in range (N)] for y in range(N)]
Det = np.linalg.det(A)
print(" {0:.2f}".format(Det))
print("%.2f" %Det)