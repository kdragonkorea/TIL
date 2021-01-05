import random
score = random.randrange(0, 100)
print(score)

if score <= 100 and score >= 90:
    print('xx점은 A등급입니다.')
elif score <= 89 and score >= 80:
    print('xx점은 B등급입니다.')
elif score <= 79 and score >= 70:
    print('xx점은 C등급입니다.')
elif score <= 69 and score >= 60:
    print('xx점은 D등급입니다.')
elif score <= 59:
    print('xx점은 F등급입니다.')