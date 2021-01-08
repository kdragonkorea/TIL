for x in range(1, 51):
    if x % 10 == 0:
        print('+', end= '')
    else:
        print('-', end = '') # --------+---------+ 50번을 출력

for x in range(1, 5):
    print('-' * 9, end = '')
    print('+', end = '')  # (---------+) 4번 반복 출력

x = 1
while x <= 50:
    if x % 10:
        print('-', end= '')
    else:
        print('+', end = '')
    x += 1 # 뭔소린지 모르겠음..

for x in range(1, 51):
    if x % 5 == 0:
        print('+', end= '')
    else:
        print('-', end = '')  # ----+ ... 총 50번 반복 출력

for x in range(1, 51):
    if x % 10 == 5:
        print('+', end= '')
    else:
        print('-', end = '')  #  ----+---------+ ... 총 50번 반복 출력