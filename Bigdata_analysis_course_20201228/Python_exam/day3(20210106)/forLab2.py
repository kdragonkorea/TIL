# [ 실습 2 ]
#  다음과 같은 결과가 출력되도록 구현한다.
#   9 : 홀수
#   8 : 짝수
#   7 : 홀수
#   6 : 짝수
#   5 : 홀수
#   4 : 짝수

# 2021-01-09 풀이 (소스리뷰와 동일함)
for i in range(9, 3, -1):
    if i % 2 == 0:
        print(i, ": 짝수")
    else:
        print(i, ": 홀수")


#   2021-01-06 풀이
#   for i in range(9, 3, -1):
#     if i % 2 == 0:
#         print(i, ": 짝수")
#     else:
#         print(i, ": 홀수")

