# [ 실습6 ] - while 문으로 무한루프 처리
# 1. whileLab6py 라는 소스를 생성한다.
# 2. 반복 처리해야 하는 기능은 다음과 같다.
# - 숫자를 하나 입력받는다.
# - 입력된 숫자가 0 이면 “종료”라는 메시지를 출력하고 수행을 종료한다.
# - 입력된 숫자가 -10 보다 작거나 10보다 크면 입력 받는 것부터 다시 시작한다.
# - 입력된 숫자가 양수이면 “입력값 : x” 행을 출력한 다음 행에 1부터 입력된 숫자 값까지의 곱한결과를 출력한다.
# - 입력된 숫자가 음수이면 양수로 변경하여 “입력값(부호변경) : x” 를 출력한 다음 행에 1부터 입력된 숫자 값까지의 곱한 결과를 출력한다.
#       5 가 입력되면
#       입력값 : 5
#       120
#       -3 이 입력되면
#       입력값(부호변경) : 3
#       6
#       0 이 입력되면
#       종료
data = int(input())
while True:
    if -10 <= data <= 10:

