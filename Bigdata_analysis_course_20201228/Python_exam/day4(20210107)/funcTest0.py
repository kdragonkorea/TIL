def a() :  #매개변수가 없다. 호출만 가능
    pass

def b() :  #매개변수가 없다. 호출만 가능
    return '올라프'

def c(p) :  #매개변수=p
    return p * 3


result1 = a()
result2 = b()
result3 = c('올라프')
result4 = c(10)

# print(result1)
# print(result2)
print(result3)
# print(result4)
# print('----------------------')
# print(a())  #변수를 정의하지 않고 함수 a를 바로 출력
# print(b())  #변수를 정의하지 않고 함수 b를 바로 출력
# print(c('둘리'))  #변수를 정의하지 않고 함수 c의 매개변수 '둘리'를 바로 출력
# print(c(20))  #변수를 정의하지 않고 함수 c의 매개변수 20을 바로 출력


