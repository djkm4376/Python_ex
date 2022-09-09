myTuple = ('a', 'b', 'c', 'd')
print(myTuple)
print(myTuple[1])

myTuple = ("python", (1,2,3), [4, 5, 6])
print(myTuple[0])
print(myTuple[0][2])
print(myTuple[1][1])
print(myTuple[2][0])

myTuple = ('p', 'y', 't', 'h', 'o', 'n')
print(myTuple[1:4])
print(myTuple[:3])
print(myTuple[:])

yourTuple = (10, 20, [1, 3, 5])
print(yourTuple)
#yourTuple[0] = 1 # 오류발생
yourTuple[2][1] = 2 # 가변 객체는 수정 가능
print(myTuple)

Tu_1 = (1, 2, 3)
Tu_2 = (4, 5, 6)
print(Tu_1 + Tu_2)
print(Tu_1 * 2)