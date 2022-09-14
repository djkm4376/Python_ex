A = {10, 20, 70, 90}
B = {10, 30, 40, 70}

print(A | B)
print(A.union(B))

print( A & B)
print(A.intersection(B))

print(A ^ B)
print(A.symmetric_difference(B))

print({10, 20, 70, 80, 90}.issuperset(A))
print({20, 30, 50} <= A)
# A.issuperset({20, 30, 50})과 동일하다.
print({10, 30, 40} <= B)
print({10, 20, 30, 50, 70, 90} >= A)