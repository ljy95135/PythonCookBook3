import numpy as np

# list
x = [1, 2, 3, 4]
print(x * 2)  # [1, 2, 3, 4, 1, 2, 3, 4]

# numpy array
ax = np.array([1, 2, 3, 4])
print(ax * 2)
print(ax ** 2)  # [ 1  4  9 16]

grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)

# index
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[1])  # row 1
print(a[:, 1])  # col 1
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)

# add a row to  all rows
print(a + [100, 101, 102, 103])

# conditional assignment
# a for ele in a
print(np.where(a < 10, a, 10))
