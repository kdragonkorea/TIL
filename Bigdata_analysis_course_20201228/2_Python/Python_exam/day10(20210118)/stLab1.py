# 프로그램 수행 중간에 년도와 월을 입력받아 해당년과 월의 달력을 출력한다.
# 년도와 월은 숫자로 입력받아야 하며 숫자가 입력되지 않아서 발생하는 에러를 대비해야 한다.
# ValueError 처리를 통해서 숫자가 입력되지 않은 경우에는 메시지를 내보내고 다시 입력받는다. 잘 할때까지……
# 년도와 월이 제대로 입력되면 해당 년월의 달력을 출력한다.


# 2021-01-19 풀이()
import calendar

while True:
    try:
        year = int(input('해당 년도를 입력하세요: '))
        month = int(input('해당 월을 입력하세요: '))
        print(calendar.month(year, month))
        break
    except ValueError:
        print("년도와 월은 숫자로 입력해주세요.")

