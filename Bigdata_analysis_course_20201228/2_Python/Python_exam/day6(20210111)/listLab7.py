# 다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
#     1행 10, 20, 30, 40, 50
#     2행 5, 10, 15
#     3행 11, 22, 33, 44
#     4행 9, 8, 7, 6, 5, 4, 3, 2, 13
# 행단위 합을 구하여 다음과 같이 출력한다.
#     1행의 합은 x 입니다.
#     2행의 합은 x 입니다.
#     3행의 합은 x 입니다.
#     4행의 합은 x 입니다.

# 2021-01-20 복습()
# list7 = [[10, 20, 30, 40, 50],[5, 10, 15],[11, 22, 33, 44],[9,8,7,6,5,4,3,2,13]]
#
# sum=0
# while True:
#
# a = list7[0][0:5]
# b = list7[1][0:3]
# c = list7[2][0:4]
# d = list7[3][0:9]
# print(a, len(a))
# print(b, len(b))
# print(c, len(c))
# print(d, len(d))




# 코드리뷰
list = [[10, 20, 30, 40, 50], [5, 10, 15],
        [11, 22, 33, 44], [9, 8, 7, 6, 5, 4, 3, 2, 13]]

for i in range(4):
    print(i+1,'행의 합은 ',sum(list[i]),' 입니다.',sep='')