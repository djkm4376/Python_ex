from cgi import print_arguments


X, Y, Z = 1, 2, 1.5

print(X)        # 1
print(X + Y)    # 3 
print(X+ Y + Z) # 4.5
#print(2X)       # error
print(2 * X)    # 2
print(2.0 + X)  # 3.0
print(X - 1.0)  # 0.0
print(X - 1)    # 0
print(Z - 0.5)  # 1.0
#print(XZ)       # error
print(X * Z)    # 1.5