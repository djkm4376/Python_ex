a = 0b10110101
b = 0b11011001
c = a + b

print(a, b, c)
print(bin(a & b), a & b)
print(bin(a | b), a | b)
print(bin(a ^ b), a ^ b)
print(bin(a >> 2), a >> 2)
print(bin(a >> 3), a >> 3)
print(bin(a << 2), a << 2)
print(bin(~a), ~a)