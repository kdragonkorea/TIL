'''비어있는 리스트를 하나 만들고 이 안에 1~45 사이의 난수를 추출하여 6개를 저장하는데
    동일한 숫자가 중복하여 저장되지 않게 만들기'''

a = []
import random
num = random.randint(1, 45)
a = num
print("행운의 로또번호: ", a)
