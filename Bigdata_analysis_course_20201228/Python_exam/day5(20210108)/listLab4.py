listnum = list()

import random

for x in range(10):
    a = random.randint(1, 50)
    listnum.append(a)  # 변수 1번만 사용하기 때문에 우측처럼 사용해도 가능하다. listnum.append(random.randint(1,50))
print(listnum)

# 방법1
for x in range(10):
    if listnum[x] < 10:
        listnum[x] = 100

# 방법2: 읽는 것만해서는 아래와 같이 해도 되지만 읽고 변경해야 하기 때문에 인덱싱을 사용해야한다.
# for e in listnum:
#     if e < 10:
#         e = 100

print(listnum)

print(listnum[0])

# 문제7

print(listnum[0])
print(listnum[-1])
print(listnum[1:6])
print(listnum[:])
print(listnum[4])
print(listnum[:])
listnum[1:3] = []
print(listnum[:])



#r = random.randint(1, 50)
# r1 = random.randint(1, 50)
# r2 = random.randint(1, 50)
# ..
# r10 = random.randint(1, 50)
# listnum = [r1, r2, r3, ...r10]
# listnum = [ri, ri+1, ...ri+10]


# for 반복물을 이용해서 1~50 사이의 난수를 10개 추출
# for i in range(10):
#     ri = random.randint(1, 50)
#     print(ri)


# for i in range(10):
#     i = random.randint(1, 50)


