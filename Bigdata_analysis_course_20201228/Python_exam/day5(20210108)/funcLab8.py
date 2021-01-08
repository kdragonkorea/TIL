# 제한시간 10분 이내에 풀어보자.
def print_triangle_withdeco(a, b = '%'):
    if 1 <= a <= 10:
        for i in range(1, a+1):
            print(' '*(a-i),b * i)

print_triangle_withdeco(9)
print_triangle_withdeco(9, '$')
