# [ 실습 4 ]
# 1. forLab4.py 라는 소스를 만든다.
# 2. evenNum 변수와 oddNum 변수의 값을 0으로 대입한다.
# 3. 1 부터 100 까지의 값 중에서
#    짝수의 합은 evenNum 에 누적하고
#    홀수의 합은 oddNum 에 누적한다.
# 4. 수행 결과는 다음과 같이 출력한다.
#
#     1부터 100까지의 숫자들 중에서
#     짝수의 합은 XXX 이고
#     홀수의 합은 YYY 이다.

evenNum = 0
oddNum = 0
for i in range(1, 101):
    if i % 2 == 0:
        evenNum = evenNum + i # evenNum += i
    else:
        oddNum = oddNum + i # oddNum += i

print(f'1부터 100까지의 숫자들 중에서\n짝수의 합은 {evenNum} 이고\n홀수의 합은 {oddNum} 이다.')