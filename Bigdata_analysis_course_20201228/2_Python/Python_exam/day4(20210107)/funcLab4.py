#   함수명 : print_triangle / 매개변수 : 1개 / 리턴값 : 없음
#   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
#   ex) 2 전달시
#   *
#   * *
#   ex) 5 전달시
#   *
#   **
#   ***
#   ****
#   *****
#   전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는
#   처리하지 않고 그냥 리턴한다. 숫자를 다양하게 지정해서 print_triangle() 함수를 호출해 본다.

#   2021-01-12 복습(소스리뷰와 동일하게 구현하였음)
def print_triangle(n):
    if 1 <= n <= 10:
        for i in range(1, n+1):
            print('*' * i)
    else:
        return

print_triangle(10)
print_triangle(11)



#   review(2021-01-08)
# if를 먼저쓰고 for를 사용하여 반복을 하게 되면 가독성이 좋아지는 것 같다.

# def print_triangle(n):
#     if 1<= n <= 10:
#         for i in range(1,n+1):
#             print("*" * i)
#     else:
#         pass

# print_triangle(5)
# print_triangle(7)
# print_triangle(3)
print_triangle(12)
