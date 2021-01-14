for x in range(1, 51):
    if x % 10 == 0 :
        print('+', end= '')
    else:
        print('-', end = '') # 1 ~ 50 사이에서 10으로 나눈 나머지가 0인 경우 +, 아닌 경우 - 를 일렬로 출력 (---+---...)
print()

for x in range(1, 5):
    print('-' * 9, end = '')
    print('+', end = '')
print()

for x in range(1, 51):
    if x % 5 == 0:
        print('+', end= '')
    else:
        print('-', end = '') # 1 ~ 50 5 나눈 나머지가 0인 경우 +, 아닌 경우 - (-----+----...)
print()

for x in range(1, 51):
    if x % 10 == 5:
        print('+', end= '')
    else:
        print('-', end = '') # ---------------------마지막에 +