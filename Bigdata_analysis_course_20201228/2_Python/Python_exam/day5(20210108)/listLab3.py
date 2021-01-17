# 최댓값과 최솟값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
# 1. 다음 값들로 구성되는 리스트를 생성하여 listnum 에 저장한다.
#    10, 5, 7, 21, 4, 8, 18
# 2. listnum 에 저장된 값들 중에서 최댓값 최솟값을 추출하여 다음과 같이 출력한다.
# 	 최솟값 : 4, 최댓값 : 21

# 2021-01-17 복습(최대값을 소스리뷰를 보고 풀었기 때문에 안보고 풀수 있었다.)
listnum = [10, 5, 7, 21, 4, 8, 18]
datamax = listnum[0]
datamin = listnum[0]
for i in range(1, len(listnum)):
    sample = listnum[i]
    if datamax < sample:
        datamax = sample
    elif datamin > sample:
        datamin = sample
print('최대값: ',datamax,'최소값: ',datamin)









# 2021-01-08 풀이
# listnum = [10, 5, 7, 21, 4, 8, 18]
# for i in range(7):
#     if listnum[i] >= listnum[0] and listnum[1] and listnum[2] and listnum[3] and listnum[4] and listnum[5] and listnum[6]
#         print('최대값: ', listnum[i])
#     else:
#         continue
#
# listnum = [10, 5, 7, 21, 4, 8, 18]
# result1 = listnum[0]
# result2 = listnum[0]
# for x in range(1, len(listnum)):
#     samp = listnum[x]
#     if result1 > samp:
#         result1 = samp
#     elif result2 > samp:
#         result2 = samp
#
# print("최소값:",result1,"최대값:",result2)