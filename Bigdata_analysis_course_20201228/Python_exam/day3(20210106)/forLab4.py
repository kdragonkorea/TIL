#   [ 실습 4 ]
#   evenNum 변수와 oddNum 변수의 값을 0으로 대입한다.
#   1 부터 100 까지의 값 중에서 짝수의 합은 evenNum 에 누적하고 홀수의 합은 oddNum 에 누적한다.
#   수행 결과는 다음과 같이 출력한다.
#
#   1부터 100까지의 숫자들 중에서
#   짝수의 합은 XXX 이고
#   홀수의 합은 YYY 이다.

#   2021-01-09 풀이------------------------------------------------------
evenNum = 0
oddNum = 0
for i in range(2, 101, 2):
    evenNum = evenNum + i
for i in range(1, 101, 2):
    oddNum = oddNum + i
print("1부터 100까지의 숫자들 중에서")
print("짝수의 합은",evenNum, "이고")
print("홀수의 합은",oddNum, "이다.")
# for를 한번만 사용해서 다시 구현해보기











# 2021-01-06 풀이
# evenNum = 0
# oddNum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         evenNum = evenNum + i # evenNum += i
#     else:
#         oddNum = oddNum + i # oddNum += i
# print(f'1부터 100까지의 숫자들 중에서\n짝수의 합은 {evenNum} 이고\n홀수의 합은 {oddNum} 이다.')

