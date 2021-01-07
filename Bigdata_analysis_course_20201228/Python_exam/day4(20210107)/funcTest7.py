def add(num1, num2) :
    return num1 + num2

r1 = add(10, 20)
v1 = 100; v2 = 200
r2 = add(v1, v2)
print(r1)
print(r2)
print(bool(add(1000, 2000)))  # bool(3000) = True
print(1+add(1000, 2000))
print(2+add(1000, 2000))
print(3+add(1000, 2000))
r3 = add(1000, 2000)  # 변수를 다시 생성함으로써 코드가 더 효율적이다.
print(1+r3)
print(2+r3)
print(3+r3)