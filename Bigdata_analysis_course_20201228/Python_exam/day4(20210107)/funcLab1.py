#    1) 함수명 : print_book_title / 매개변수 : 없음 / 리턴값 : 없음 / 기능 : 파이썬 교재명을 화면에 출력
#    2) 함수명 : print_book_publisher / 매개변수 : 없음 / 리턴값 : 없음 / 기능 : 파이썬 교재의 출판사명을 화면에 출력
#    3) print_book_title() 함수를 3회 호출하고 print_book_publisher() 함수를 5회 호출한다.

# 2021-01-12 복습(if를 어떻게 써야할지 몰랐음)
# def print_book_title():
#     print("파이썬정복")
# def print_book_publisher():
#     print("한빛미디어")
#
# for i in range(1,6):
#     if i


#2021-01-10 복습 (함수를 만들고 for문으로 3회 5회 반복은 잘 구현하였지만, for문을 한번을 사용해서 구현을 하지 못하였다)
# def print_book_title():
#     print("파이썬정복")
#
# def print_book_publisher():
#     print("한빛미디어")
#
# for i in range(3):
#     print_book_title()
#
# for i in range(5):
#     print_book_publisher()

#review(2021-01-07)
# def 를 정의하는 것은 잘 코딩하였으나 마지막 3회, 5회 출력하는 것을 반복문과 if문으로 구현해야할 것을 생각하지 못하였다.

# 풀이
# for i in range(1,6):
#     if i <= 3:
#         print_book_title()
#         print_book_publisher()
#     else:
#         print_book_publisher()

