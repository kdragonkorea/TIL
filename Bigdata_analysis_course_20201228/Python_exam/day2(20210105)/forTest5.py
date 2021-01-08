startNum = int(input("시작 숫자 : "))
endNum = int(input("종료 숫자 : "))
incNum = int(input("증가치 숫자 : "))

for num in range(startNum, endNum+1, incNum) :
    print(num, end=" ")

#  입력한 시작 숫자 ~ 종료 숫자 까지 입력한 증가치 숫자만큼 반복해서 출력
#  출력 전 위 코드를 이해하지 못하였다.
#  위 코드는 입력한 시작 숫자 부터 종료 숫자까지 출력하지만, 증가치 만큼의 숫자를 건너 띄어서 출력하고 종료된다.
