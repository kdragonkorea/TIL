# 함수명 : print_triangle_withdeco
# 매개변수 : 2개(숫자와 데코문자,데코문자는 기본값 ‘%’로 정한다.) / 리턴값 : 없음
# 기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
# 숫자 2 만 전달시
#              %
#             %%
# 숫자 5 와 데코문자 ‘*’ 전달시
#              *
#             **
#            ***
#           ****
#          *****
# 전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는 처리하지 않는다.
# 숫자를 다양하게 지정해서 print_triangle_withdeco () 함수를 호출해 본다.

# 2021-01-14 복습 (삼각형을 반대로 출력하는 방법에 대해서 다시 고민해보자)
def print_triangle_withdeco(num, x='%'):
    if 1 <= num <= 10:
        for i in range(1, num+1):
            print((num-i)*' ',i * x)
    else:
        pass

print_triangle_withdeco(8, '#')

























# 소스리뷰
# def print_triangle_withdeco(a,b='%'):
#     if 1<=a<=10:
#         for i in range(1,a+1):
#             print(' '*(a-i),b * i)
#
#
# print_triangle_withdeco(3,'*')
# print_triangle_withdeco(5, '^')
# print_triangle_withdeco(6)
# print_triangle_withdeco(13)