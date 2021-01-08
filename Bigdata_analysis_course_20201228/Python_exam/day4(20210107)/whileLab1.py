# [ 실습1 ]
# 1. whileLab1.py 라는 소스를 생성한다.
# 2. 5부터 10사이의 난수를 추출한다.
# 3. 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다.
#    ===>  7이 추출되면
#       1 -> 1
#      	2 -> 4
#      	3 -> 9
#      	4 -> 16
#      	5 -> 25
#      	6 -> 36
#      	7 -> 49

import random
data = random.randint(5, 10)
print(f'출력값: {data}')
for i in range(1, data+1):
    print(f'{i} -> {i*i}')  # I * i = i ** 2

# review(2021-01-08)
# while문을 이용해서 다시 연습해보자.