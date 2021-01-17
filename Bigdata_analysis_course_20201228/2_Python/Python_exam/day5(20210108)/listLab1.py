# 최댓값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
# 1. 다음 값들로 구성되는 리스트를 생성하여 listnum 에 저장한다.
#       10, 5, 7, 21, 4, 8, 18
# 2. listnum  에 저장된 값들 중에서 최댓값을 추출하여 다음과 같이 출력한다.
#       최댓값 : 21

# 2021-01-17 복습(코드리뷰를 보면서 이해하고, 다시 풀어보았다. 나중에 다시 풀어보자.)
listnum = [10, 5, 7, 21, 4, 8, 18]
datamax = listnum[0]
for i in range(1, len(listnum)):
    sample = listnum[i]
    if datamax < sample:
        datamax = sample
print('최댓값 :',datamax)





















# 2021-01-08 풀이
# listnum = [10, 5, 7, 21, 4, 8, 18]
# result = listnum[0]
# for x in range(1, len(listnum)):  # len(listnum) 대신에 7도 사용 가능하지만, 리스트의 데이터 수가 변할 수 있으니 len을 사용하는 것이 좋다.
#     samp = listnum[x]
#     if result < samp:
#         result = samp
#
# print("최대값: ", result)