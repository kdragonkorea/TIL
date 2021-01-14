# [ 실습1 ]
# 5부터 10사이의 난수를 추출한다.
# 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다.
# ===>  7이 추출되면
# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16
# 5 -> 25
# 6 -> 36
# 7 -> 49

# review(2021-01-09)-----------코드리뷰와 동일함 그러나 30분정도 이상의 시간 소요가 발생..
import random
r = random.randint(5, 10)
n = 1
while n <= r:
    print(n, "->", n*n)
    n = n + 1









# import random
# data = random.randint(5, 10)
# print(f'출력값: {data}')
# for i in range(1, data+1):
#     print(f'{i} -> {i*i}')  # I * i = i ** 2

