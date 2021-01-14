def kim():
    temp = "김과장의 함수"  # 지역변수 = 함수 안에서 정의한 변수, (전역변수 = 함수 밖에서 정의한 변수)
    print(temp)

def lee():
    temp = 2 ** 10
    return temp

def park(a):
    temp = a * 2
    print(temp)

kim()
print(lee())
park(6)
#print(temp)  temp라는 변수는 모두 각 함수의 지역함수이기 때문에 전역변수로 사용이 불가함
