def calcrange(begin, end):
    sum = 0
    for num in range(begin, end + 1):
        sum += num
    return sum

print("3 ~ 7 =", calcrange(3, 7))
print("1 ~ 100 =", calcrange(1, 100))  # 예시로 만들었음


