# 1. 비어있는 리스트를 하나 생성하여 listnum 이라는 변수에 저장한다.
listnum = []

# 2. 1~50 사이의 난수를 10개 추출하여 listnum 에 추출 순서대로 저장한다. (for문 사용)
# 2021-01-17 복습(난수 10개를 각각 다르게 리스트에 추가하는 방법에 대해서 다시 연습해보자)
import random
for i in range(10):
    a = random.randint(1, 50)
    listnum.append(a)

# 3. listnum의 모든 값들을 출력한다.(이 때 반복문을 사용하지 않아도 된다.)
# 2021-01-17 복습
print(listnum)

# 4. 리스트에서 10보다 작은 값들은 100으로 변경한다. (for문 사용)
# 2021-01-17 복습 (범위를 range(10)이 아니라 listnum으로 하였는데 왜 안되는걸까??)
for i in range(10):
    if listnum[i] < 10:
        listnum[i] = 100

# 5. listnum의 모든 값들을 출력한다.(이 때 반복문을 사용하지 않아도 된다.)
print(listnum)

# 6. 인덱싱 방법으로 listnum의 첫 번째 데이터를 출력한다.
# 2021-01-17 복습
print(listnum[0])

# 8. 인덱싱 방법으로 listnum의 마지막 데이터를 출력한다.
# 2021-01-17 복습
print(listnum[-1])

# 9. 슬라이싱 방법으로 listnum의 두 번째 데이터부터 여섯 번째 데이터만 추출하여 출력한다.
# 2021-01-17 복습
print(listnum[1:6])

# 10. 슬라이싱 방법으로 listnum의 데이터를 역순으로 출력한다.
# 2021-01-17 복습(역순으로 출력하는 방법 다시 해보기)
print('역순',listnum[::-1])

# 11. 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.
# 2021-01-17 복습
print(listnum[:])

# 12. 인덱싱 방법으로 5번째 데이터를 삭제한다.
# 2021-01-17 복습(인덱싱으로 데이터 삭제하는 방법 다시 해보기)
del listnum[4]
print(listnum[:])

# 13. 슬라이싱 방법으로 2~3번째 데이터를 삭제한다.
# 2021-01-17 복습(슬라이싱으로 데이터 삭제하는방법에 대해서 다시 해보기)
listnum[1:3] = []
print(listnum[:])













# import random
#
# for x in range(10):
#     a = random.randint(1, 50)
#     listnum.append(a)  # 변수 1번만 사용하기 때문에 우측처럼 사용해도 가능하다.
#     listnum.append(random.randint(1,50))
# print(listnum)
#
# # 방법1
# for x in range(10):
#     if listnum[x] < 10:
#         listnum[x] = 100
#
# # 방법2: 읽는 것만해서는 아래와 같이 해도 되지만 읽고 변경해야 하기 때문에 인덱싱을 사용해야한다.
# # for e in listnum:
# #     if e < 10:
# #         e = 100