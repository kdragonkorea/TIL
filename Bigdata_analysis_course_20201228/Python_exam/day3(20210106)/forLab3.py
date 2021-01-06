# [ 실습 3 ]
# 1. forLab3.py 라는 소스를 만든다.
# 2. 1부터 10사이의 난수를 하나 추출한다.
# 3. 30부터 40사이의 난수를 하나 추출한다.
# 4. 첫 번째 난수부터 두 번째 난수까지의 숫자들 중에서 짝수의 합을 구해
# 다음 형식으로 출력한다.
#
#     X 부터 Y 까지의 짝수의 합 : XX

import random
x = random.randint(1, 10)
y = random.randint(30, 40)
print(x, y)
if x % 2 == 0 and y % 2 == 0:
    print('X 부터 Y 까지의 짝수의 합: ', x+y)
