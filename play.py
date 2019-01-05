

l=[]
for i in range(5):
    for j in range(10):
        l.append((i, j))

m = [(i, j) for i in range(4) for j in range(9)]

print(l)
print(m)

print(l == m)
