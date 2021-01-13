# 2021-01-13 실습
# (1) s1 = "pythonjavascript" 에서 의 길이를 출력한다.
# (2) s2 = "010-7777-9999" 에서 01077779999 을 출력한다.
# (3) s3 = "PYTHON" 에서 NOHTYP 를 출력한다.
# (4) s4 = "Python" 에서 python 을 출력한다.
# (5) s5 = "https://www.python.org/" 에서 www.python.org 만을 뽑아서 출력한다.
# (6) 주민등록 번호에서 7자리 숫자를 사용해서 남성, 여성을 판별한다. (1,3 : 남성, 2,4 : 여성)
# s6 = '891022-2473837'
# (7) s7 = '100' 에서 s7 값을 정수형 숫자로 그리고 실수형 숫자로 변환하여 출력한다.
# (8) s8 = ' The Zen of Python' 에서 ' n' 문자가 몇 개인지 출력한다.
# (9) s8 에서 ' Z'  의 위치를 출력한다.
# (10) s8 에서 모두 대문자로 변환한 후 공백단위로 분리해서 리스트로 만들어 출력한다.

s1 = "pythonjavascript"
print('(1)에 대한 결과: ',len(s1))

s2 = "010-7777-9999"
phone_number = s2.split("-")
print('(2)에 대한 결과: ',"".join(phone_number))

# s3 = "PYTHON"
# print(reversed(s3))

s4 = "Python"
print('(4)에 대한 결과: ',s4)

s5 = "https://www.python.org/"
print('(5)에 대한 결과: ',s5[8:22])

s6 = '891022-2473837'
print('(6)에 대한 결과: ',s6[7])

s8 = ' The Zen of Python'
print('(8)에 대한 결과: ',s8.count('n'))

print('(9)에 대한 결과: ',s8.find('Z'))

print('(10)에 대한 결과: ',s8.upper())


