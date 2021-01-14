#   [ 실습 5 ] --- continue 문을 사용하지 않고 해결
#   1 부터 50까지의 숫자 중에서 3의 배수에 해당하는 값들의 합을 구한다.
#   단 5의배수는 제외한다.
#   다음과 같은 결과가 되도록 구현한다.
#   결과 = 318

#   2021-01-09 풀이 (소스리뷰와 동일함)
sum = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        sum = sum + i
print("결과 =",sum)









#   2021-01-06 풀이
# data = 0
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 != 0:
#         data = data + i # data += i
# print(f'결과 = {data}')