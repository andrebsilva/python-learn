A = frozenset((1, 2, 3, 3, 4, 5, 6))
B = frozenset((4, 5, 6, 6, 7, 8, 9))

C = A.union(B)
print(C)

D = A.intersection(B)
print(D)

E = A.difference(B)
print(E)

F = B.difference(A)
print(F)

G = A.symmetric_difference(B)
print(G)

H = A.copy()
print(H)

X = frozenset((10, 20, 30, 40))
Y = frozenset((2, 4, 6))

print(A.isdisjoint(X))
print(Y.issubset(A))
print(A.issuperset(Y))