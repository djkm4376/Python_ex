jobs={'김연아' : '피겨스케이팅',
      '박지성' : '축구',
      '정현' : '테니스',
      '박태환' : '수영'}

var = input("운동선수 입력 : ")

result = jobs[var]

print('{}(은)는 {} 선수이다.'.format(var, result))