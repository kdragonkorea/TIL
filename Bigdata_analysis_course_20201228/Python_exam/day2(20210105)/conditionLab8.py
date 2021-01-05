import random
oper_num = random.randrange(1, 11)
print(oper_num)
if oper_num == 1 or oper_num == 6:
    print(f'결과값 : {300+50}')
elif oper_num == 2 or oper_num == 7:
    print(f'결과값 : {300-50}')
elif oper_num == 3 or oper_num == 8:
    print(f'결과값 : {300*50}')
elif oper_num == 4 or oper_num == 9:
    print(f'결과값 : {300/50}')
elif oper_num == 5 or oper_num == 10:
    print(f'결과값 : {300%50}')

a = 300
b = 50
data1 = a+b
data2 = a-b
data3 = a*b
data4 = a/b
data5 = a%b
