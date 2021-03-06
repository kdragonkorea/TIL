# (1) 함수명: sumEven1 / 매개변수: 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다)
# 리턴값: 1개
# (2) 기능: 아규먼트가 몇 개가 전달되든 처리해야 한다. 아규먼트는 1 이상의 숫자만 온다고 정한다.
# 전달된 아규먼트들에서 짝수에 해당하는 숫자들만 합을 계산해서 리턴한다.
# 전달된 아규먼트들 중에 짝수가 없으면 0 을 리턴한다. 아규먼트가 전달되지 않으면 - 1 을 리턴한다.
# (3) 숫자를 다양하게 지정해서 sumEven1() 함수를 호출해 본다.

# 2021-01-25 복습 
# (1) 반복문이 먼저인지 제어문이 먼저인지 고민해보기
# (2) return할 위치 고민하기 

def sumEven1(*p):
    sum = 0
    result = 0
    for i in p:
        if i % 2 == 0:
            sum = sum + i
        else:
            pass
    if len(p) == 0:
        sum = -1
    return sum

print(sumEven1())

















# 2021-01-15 복습 (다시 풀어보기, 변수가 중요)

# def sumEven1(*n):
#     sum = 0
#     for i in n:
#         if i%2==0:
#             sum = sum + i
#     if len(n) == 0:
#         sum = -1
#     return sum
#
# print(sumEven1(1, 2, 4))
# print(sumEven1())
# print(sumEven1(100))

# 코드리뷰
# def sumEven1(*p):
#     ans=0
#     for data in p:
#         if data%2==0:
#             ans+= data
#
#     if len(p)==0:
#         ans=-1
#     return ans
#
# print(sumEven1(1,2,3,4))
# print(sumEven1())
# print(sumEven1(100))
# print(sumEven1(3,5,7))
