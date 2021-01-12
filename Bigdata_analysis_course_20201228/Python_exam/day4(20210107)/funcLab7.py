#   함수명 : differtwovalue / 매개변수 :  2개 / 리턴값 : 연산 결과
#   기능 : 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴 두 값이 동일하면 0 을 리턴한다.
#   10, 20 이 전달되면 ---> 10 리턴
#   20, 5 가 전달되면 ---> 15 리턴
#   5, 30 이 전달되면 ---> 25 리턴
#   6, 3 이 전달되면  ---> 3 리턴
#   1부터 30 사이의 난수 2 개를 추출하여 2번에서 구현된 함수를 호출하고 결과를 다음 형식으로 출력한다.
#    "X 와 Y 의 차는 W 입니다." ----> 5 회 반복

#2021-01-12 복습
















# def differtwovalue(a, b):
#     if a > b:
#         return a - b
#     elif a < b:
#         return b - a
#     else:
#         return 0
#
# import random
# for i in range(5):
#     data1 = random.randint(1, 30)
#     data2 = random.randint(1, 30)
#     data3 = differtwovalue(data1, data2)
#     print(f'{data1}와 {data2}의 차는 {data3} 입니다.')

# review(2021-01-08)
# differtwovalue함수를 정의할 때 return은 한번만 사용하도록 시도해보자.

# def differtwovalue(x1,x2):
#     if a >= b:
#         c = a - b
#     else:
#         c = b - a
#     return c
#
# import random
# for i in range(1,6):
#     a = random.randint(1,30)
#     b = random.randint(1,30)
#     print(a,"와",b,"의 차는",differtwovalue(a,b),"입니다.")
