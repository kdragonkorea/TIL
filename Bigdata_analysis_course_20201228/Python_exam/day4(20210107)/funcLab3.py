def expr(a, b):
    c = a * b
    return c


result = expr(2, 0)
if result == 0:
    print("수행불가")
else:
    print("연산결과: ", result)

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