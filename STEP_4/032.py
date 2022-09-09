A, B, C = 1, 2, 3

A += A * B + A
B %= A % C % B
C *= C - A ** (A - 3)

print(A)    # 4
print(B)    # 0
print(C)    # -3