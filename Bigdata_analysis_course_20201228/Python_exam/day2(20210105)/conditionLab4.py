import random
grade = random.randrange(1, 7)
print(grade)

#if grade == 1 or grade == 2 or grade == 3:
if grade in (1, 2, 3):
    print('x 학년은 저학년입니다.')
else:
    print('x 학년은 고학년입니다.')