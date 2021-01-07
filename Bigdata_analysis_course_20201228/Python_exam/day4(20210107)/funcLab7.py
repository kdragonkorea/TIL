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