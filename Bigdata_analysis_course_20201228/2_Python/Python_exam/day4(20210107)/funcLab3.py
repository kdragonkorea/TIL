#    함수명 : expr
#    매개변수 : 숫자 2개와 연산자 1개 / 리턴값 : 연산 결과 또는  None
#    기능 : 전달된 두 개의 숫자에 대해서 전달된 연산을 처리하고 그 결과를 리턴한다.
#    연산자는 +, -, *, / 만 처리하며 그 외의 연산자는 연산을 하지 않고 None 을 리턴한다.
#    숫자 2개와 연산자 1개를 전달하여 expr() 이라는 함수를 호출한 다음 리턴 결과가 None 이면 수행 불가 를 출력하고
#    그렇지 않으면 연산결과 : XX 를 출력한다.

# 2021-01-12 복습(연산자를 어떻게 내용을 입력해야할지 구현이 안된다. 다시 풀어보자.)
# def expr(num1, num2, y):
#     if num1+num2 == sum:
#         return y


# 2021-01-11 복습()
# def expr(num1, num2, a):
#     if a == '*':
#         a = num1*num2
#         return a
#     elif a == '+':
#         a = num1+num2
#         return a
#     elif a == '-':
#         a = num1-num2
#         return a
#     else:
#         return
# #
# result = expr(3, 6, '*')
#
# if result == None:
#     print('수행불가')
# else:
#     print('연산결과: ',expr(3, 6, '*'))

# result = expr(3,5,"+")
# if result != None:
#     print("연산 결과 :", result)
# else:
#     print("수행 불가")
#
# result = expr(3,5,"#")
# if result == None:
#     print("수행 불가")
# else:
#     print("연산 결과 :", result)











# def expr(a, b):
#     c = a * b
#     return c
#
#
# result = expr(2, 0)
# if result == 0:
#     print("수행불가")
# else:
#     print("연산결과: ", result)


# review(2021-01-08)
# 문제 의미를 정확히 파악하지 못하여서 다시 풀어봐야할 것 같다.

# def expr(num1,num2,x):
#     if x == "+":
#         ans = num1 + num2
#     elif x == "-":
#         ans = num1 - num2
#     elif x == '*':
#         ans = num1 * num2
#     elif x == '/':
#         ans = num1 / num2
#     else:
#         ans = None
#     return ans
#
# result = expr(3,5,"+")
# if result != None:
#     print("연산 결과 :", result)
# else:
#     print("수행 불가")
#
# result = expr(3,5,"#")
# if result == None:
#     print("수행 불가")
# else:
#     print("연산 결과 :", result)