# [ 실습4 ] - while 문으로 무한루프 처리
# 1. whileLab4py 라는 소스를 생성한다.
# 2. 반복 처리해야 하는 기능은 다음과 같다.
# 	사용자로부터 월에 해당하는 숫자를 하나 입력 받는다.
# 	입력된 숫자가 1~12 사이의 값이면
#        	12, 1, 2의 경우엔 x월은 겨울
#         	3, 4, 5의 경우엔 x월은 봄
#         	6, 7, 8의 경우엔 x월은 여름
#         	9, 10, 11의 경우엔 x월은 가을
#        을 출력한다.
#        입력된 숫자가 1~12 사이가 아니면 1~12 사이의 값을 입력하세요! 를 출력하고
#        종료한다.

while True:
    month = int(input("월을 입력하세요: "))
    if month in (12, 1, 2):
        print(f'{month}월은 겨울')
        break
    elif month in (3, 4, 5):
        print(f'{month}월은 봄')
        break
    elif month in (6, 7, 8):
        print(f'{month}월은 여름')
        break
    elif month in (9, 10, 11):
        print(f'{month}월은 가을')
        break
    else:
        print("1 ~ 12 값을 입력해주세요")
