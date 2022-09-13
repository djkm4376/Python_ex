# map을 사용하여 형 변환과 여러개의 인수를 input을 통해 동시에 진행 시킨다.
# 형태는 map(변환할 형, input().split())

a1, a2, a3, a4 = map(int, input('네 수를 입력하세요 : ').split())

avg = (a1 + a2 + a3 + a4) / 4

u = (((a1 - avg)**2) + ((a2 - avg)**2) + ((a3 - avg)**2) + ((a4 - avg)**2)) / 4


print('평균 : {}'.format(str(avg)))
print('분산 : {}'.format(str(u)))