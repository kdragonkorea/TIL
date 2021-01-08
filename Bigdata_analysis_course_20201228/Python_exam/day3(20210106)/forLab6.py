# [ 실습 6 ] --- continue 문을 사용해서 해결
# 1. forLab6.py 라는 소스를 생성한다.
# 2. 1 부터 50까지의 숫자 중에서 3의 배수에 해당하는 값들의 합을 구한다.
# 단 5의배수는 제외한다.
# 2. 다음과 같은 결과가 되도록 구현한다.
#
#     	결과 = 318

data = 0
for i in range(1,51):
    if i % 3 == 0:
        if i % 5 == 0:
            continue
        data += i
print(data)