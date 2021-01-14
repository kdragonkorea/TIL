import random
grade = random.randrange(1, 7)
print(grade)

if 1 <= grade <= 3:
    print('x 학년은 저학년입니다.')
else:
    print('x 학년은 고학년입니다.')