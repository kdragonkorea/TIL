def print_triangle(n):
    for i in range(0, n):
        if 1 <= n <= 10:
            n = i + 1
            print("*" * n)

print_triangle(13)

#review(2021-01-08)
# if를 먼저쓰고 for를 사용하여 반복을 하게 되면 가독성이 좋아지는 것 같다.

# def print_triangle(n):
#     if 1<= n <= 10:
#         for i in range(1,n+1):
#             print("*" * i)
#     else:
#         pass
#
# print_triangle(5)
# print_triangle(7)
# print_triangle(3)
# print_triangle(12)
