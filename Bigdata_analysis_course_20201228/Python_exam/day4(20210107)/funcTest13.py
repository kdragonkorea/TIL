salerate = 0.9  # 전역변수 = 함수 밖에서 정의한 변수

def kim():
    print("오늘의 할인율 :", salerate)

def lee():
    price = 1000
    print("가격 :", price * salerate)

kim()
salerate = 1.1
lee()
################
price = 1000

def sale():
    price = 500
    print(price)

sale()
print(price)