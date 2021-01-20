# 1. 비어있는 리스트를 하나 만들고 이 안에 1~45 사이의 난수를 추출하여 6개를 저장하는데
#    동일한 숫자가 중복하여 저장되지 않게 한다.
# 3. 수행 결과는 다음과 같다.
# 	 행운의 로또번호  : X, X, X, X, X, X

# 2021-01-18 복습(동일한 숫자가 중복되지 않도록 하는 방법에 대해서 다시 생각해보자.)
import random
lottolist = []
while True:
    for i in range(6):
        a = random.randint(1, 45)
        lottolist.append(a)
    print(lottolist)















# 2021-01-11 풀이
# lotto = [lotto_number,lotto_number,lotto_number,lotto_number,lotto_number,lotto_number]
# 동일한 숫자가 반복되는 로또번호
# lotto_number = random.randint(1, 45)
# for i in range(7):
#     lotto = [lotto_number] * i
# print('행운의 로또번호: ',lotto)
# 동일한 숫자가 반복되지 않는 로또번호
# num1 = lotto_number
# num2 = lotto_number
# num3 = lotto_number
# num4 = lotto_number
# num5 = lotto_number
# num6 = lotto_number
# for i in range(7):
#     lotto_number = random.randint(1, 45)
#     lotto = [num1, num2]
# print('행운의 로또번호: ',lotto)

# 코드리뷰
# import random
#
# list = []
# while True:
#     x = random.randint(1,45)
#     if len(list) == 6:
#         break
#     if x in list:
#         continue
#     else:
#         list.append(x)
#
# print('행운의 로또번호 :', list[0], list[1], list[2], list[3], list[4], list[5])



