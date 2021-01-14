# 함수명 : print_gugudan / 매개변수 : 1개 / 리턴값 : 없음
# 기능 : 전달된 숫자의 구구단을 출력한다.
#  - 전달된 아규먼트가 int 타입인지 체크하고 int 타입이 아니면 그냥 리턴한다.
#  - 전달된 아규먼트가 1~9 사이인지 체크하고 아니면 그냥 리턴한다.
#  - 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다.
# 숫자를 다양하게 지정해서 print_ gugudan() 함수를 호출해 본다.

# 2021-01-12 복습 (반복문은 잘 구현하였지만, 아규먼트 int와 1~9사이의 조건을 다시 구현해보자.
# def print_gugudan(n):
#     if type(n) == int:
#         for i in range(1, 10):
#             print(n,'*',i,'=',n*i)
#     elif n > 9 or n < 1:
#         return
#     else:
#
# print_gugudan(4)


# 소스리뷰
# def print_gugudan(n):
#     if type(n) == int:
#         if 1<=n<=9:
#             for i in range(1,10):
#                 print(n,"*",i,"=",n*i)
#         else:
#             pass
#     else:
#         pass
#
# print_gugudan(4)

# review(2021-01-08)
# 충분히 고민해보고 다시 풀어보고 정답이랑 비교해보자