# [ 실습 3 ]
#   1부터 10사이의 난수를 하나, 30부터 40사이의 난수를 하나 추출
#   첫 번째 난수부터 두 번째 난수까지의 숫자들 중에서 짝수의 합을 구해 다음 형식으로 출력
#   형식: X 부터 Y 까지의 짝수의 합 : XX

# 2021-01-09 풀이 (for문을 이용할 때 범위에 변수를 지정하는 방법을 생각하지 못했다)
import random
X = random.randint(1, 10)
Y = random.randint(30, 40)
SUM = 0     # 변수를 만들때 항상 초기화를 하는 습관이 필요하다.

for i in range(X, Y+1):
    if i % 2 == 0:
        SUM = SUM + i
print(X,"부터",Y,"까지의 짝수의 합:", SUM)

# 코드리뷰
# import random
# num1 = random.randint(1,10)
# num2 = random.randint(30,40)
# sum = 0
#
# for i in range(num1, num2+1):
#     if i%2==0:
#         sum += i
#
# print(num1, '부터', num2, '까지의 짝수의 합:', sum)

# 2021-01-06 풀이
# import random
# x = random.randint(1, 10)
# y = random.randint(30, 40)
# print(x, y)
# if x % 2 == 0 and y % 2 == 0:
#     print('X 부터 Y 까지의 짝수의 합: ', x+y)


