import numpy as np
import numpy.linalg

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m, m.T, m.I, sep='\n')
n = np.matrix([[2], [3], [4]])
print(m * n)

print(numpy.linalg.det(m))
print(numpy.linalg.eigvals(m))
x = numpy.linalg.solve(m, n)
print(x)

print(m * x)
