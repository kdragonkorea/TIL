def print_triangle(n):
    if 1 <= n <= 10:
        for i in range(n, 0, -1):
            print("@" * i)  #반복문 연습 필요..

print_triangle(4)

# review(2021-01-08)
# 반복문을 빠르게 적용하는게 힘들다. 다시 풀어보자

# def print_triangle(n):
#     if 1<= n <= 10:
#         for i in range(n,0,-1):
#             print("@"*i)
#     else:
#         pass
#
# print_triangle(5)
# print_triangle(7)
# print_triangle(3)
# print_triangle(12)