def differtwovalue(a, b):
    if a > b:
        return a - b
    elif a < b:
        return b - a
    else:
        return 0

import random
for i in range(5):
    data1 = random.randint(1, 30)
    data2 = random.randint(1, 30)
    data3 = differtwovalue(data1, data2)
    print(f'{data1}와 {data2}의 차는 {data3} 입니다.')

# review(2021-01-08)
# differtwovalue함수를 정의할 때 return은 한번만 사용하도록 시도해보자.

# def differtwovalue(x1,x2):
#     if a >= b:
#         c = a - b
#     else:
#         c = b - a
#     return c
#
# import random
# for i in range(1,6):
#     a = random.randint(1,30)
#     b = random.randint(1,30)
#     print(a,"와",b,"의 차는",differtwovalue(a,b),"입니다.")
