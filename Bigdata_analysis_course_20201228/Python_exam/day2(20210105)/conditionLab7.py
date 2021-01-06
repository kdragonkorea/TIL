num = int(input('1부터 10사이의 숫자를 하나 입력하세요 :'))
# if 0 < num <= 10 and num%2 == 0:
#     print('짝수')
# elif 0 < num <= 10 and num%2 == 1:
#     print('홀수')
# else:

if 1 < num <= 10:
    if num & 2 == 0:
        print(num, ': 짝수')
else:
    print('1부터 10사이의 값이 아닙니다.')
