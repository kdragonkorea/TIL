# 제한시간 10분
# listnum = [10, 5, 7, 21, 4, 8, 18]
# for i in range(7):
#     if listnum[i] >= listnum[0] and listnum[1] and listnum[2] and listnum[3] and listnum[4] and listnum[5] and listnum[6]
#         print('최대값: ', listnum[i])
#     else:
#         continue

listnum = [10, 5, 7, 21, 4, 8, 18]
result1 = listnum[0]
result2 = listnum[0]
for x in range(1, len(listnum)):
    samp = listnum[x]
    if result1 > samp:
        result1 = samp
    elif result2 > samp:
        result2 = samp

print("최소값:",result1,"최대값:",result2)