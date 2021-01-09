student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리한다.")
    student += 1
print("수행종료")
# 2021-01-09 복습
# 아래와 같이 출력된다.
# '1번 학생의 성적을 처리한다.'
# '2번 학생의 성적을 처리한다.'
# ...
# '5번 학생의 성적을 처리한다.' 를 출력한다.
# '수행종료'

for student in range(1, 6) :
    print(student, "번 학생의 성적을 처리한다.")
print("수행종료")