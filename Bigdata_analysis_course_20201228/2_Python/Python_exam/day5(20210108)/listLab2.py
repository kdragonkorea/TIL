# 최솟값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
# 2. 다음 값들로 구성되는 리스트를 생성하여 listnum 에 저장한다.
#    10, 5, 7, 21, 4, 8, 18
# 3. listnum 에 저장된 값들 중에서 최솟값을 추출하여 다음과 같이 출력한다.
# 	 최솟값 : 4

# 2021-01-17 복습(최대값을 소스리뷰를 보면서 이해하고 풀어보고 최소값은 소스리뷰 없이 풀어보았다.)
listnum = [10, 5, 7, 21, 4, 8, 18]
datamin = listnum[0]
for i in range(1, len(listnum)):
    sample = listnum[i]
    if datamin > sample:
        datamin = sample
print('최솟값 :',datamin)
