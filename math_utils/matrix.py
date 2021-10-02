import numpy as np

uv = np.array([[1], [1]])
a = np.array([[1, 2], [2, 3]])
b = np.array([[1, 2], [2, 3]])
c = a.dot(b)

print(uv)
print(a)
print(b)
print(c)

print(f"Determinant {np.linalg.det(a)}")
print(np.linalg.inv(a))

print(a.dot(np.linalg.inv(a)))

print(a.dot(uv))