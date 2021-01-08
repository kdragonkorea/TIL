# 제한시간 10분
listnum = [10, 5, 7, 21, 4, 8, 18]
result = listnum[0]
for x in range(1, len(listnum)):  # len(listnum) 대신에 7도 사용 가능하지만, 리스트의 데이터 수가 변할 수 있으니 len을 사용하는 것이 좋다.
    samp = listnum[x]
    if result > samp:
        result = samp

print("최소값: ", result)