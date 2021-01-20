# 다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
# 'B', 'C', 'A', 'A'
# 'C', 'C', 'B', 'B'
# 'D', 'A', 'A', 'D'
# 다음 내용으로 구성되는 리스트를 하나 생성한다.
# 첫 번째 원소에는 'A' 문자의 개수
# 두 번째 원소에는 'B' 문자의 개수
# 세 번째 원소에는 'C' 문자의 개수
# 네 번째 원소에는 'D' 문자의 개수
# 다음과 형식으로 출력한다.
# A는 x개 입니다.
# B는 x개 입니다.
# C는 x개 입니다.
# D는 x개 입니다.

# 2021-01-20 복습()
list = [['B', 'C', 'A', 'A'], ['C', 'C', 'B', 'B'], ['D', 'A', 'A', 'D']]
list1 = []

# 코드리뷰
# list1=[['B', 'C', 'A', 'A'], ['C', 'C', 'B', 'B'], ['D', 'A', 'A', 'D']]
#
# count1, count2, count3, count4 = 0,0,0,0
# for l in list1:
#     for e in l:
#         if e == 'A':
#             count1+=1
#         elif e == 'B':
#             count2 +=1
#         elif e == 'C':
#             count3 +=1
#         elif e == 'D':
#             count4 +=1
#
# list2 = [count1, count2, count3, count4]
#
# print("A 는 ", list2[0],"개 입니다.", sep="")
# print("B 는 ", list2[1],"개 입니다.", sep="")
# print("C 는 ", list2[2],"개 입니다.", sep="")
# print("D 는 ", list2[3],"개 입니다.", sep="")
#
# for i in range(4) :
#     print(chr(65+i)," 는 ", list2[i], "개 입니다.", sep="")