# [ 실습5 ] - while 문으로 무한루프 처리
#  	- 사용자로부터 문자열을 하나 입력받아 word 라는 변수에 저장한다.
# 	- word 변수에 저장된 데이터의 길이를 추출하여(문자열 길이는 len() 이라는 함수를 사용한다.) wordlength 라는 변수에 저장한다.
#   - wordlength 라는 변수에 할당된 값에 따라서 다음 기능을 수행한다.
#   - wordlength 라는 변수의 값이 0 이면 반복을 종료한다.
#   - wordlength 라는 변수의 값이 5 이상이고 8 이하이면 아무 기능도 수행하지 않고 입력받는 기능부터 다시 수행한다.
#   - wordlength 라는 변수의 값이 5 미만이면 문자열의 앞과 뒤에 “*” 기호를 붙여서 result 변수에 저장한다.
#   - wordlength 라는 변수의 값이 8 초과이면 문자열의 앞과 뒤에 “$” 기호를 붙여서 result 변수에 저장한다.
#   result 변수의 값을 다음 형식으로 출력한다. '유효한 입력 결과 : ........'

# 2021-01-10 복습(result 변수를 잘 만들어보자, 문자열 입력하는 변수를 반복해야하는지 고민해보자)
while True:
    word = input("문자를 입력하세요: ")
    wordlength = len(word)

    if wordlength == 0:
        break
    elif 5 <= wordlength <= 8:
        continue
    elif wordlength < 5:
        result = "*"+word+"*"
    elif wordlength > 8:
        result = "$"+word+"$"
    print("유효한 입력 결과 :", result)
















# while True:
#     word = input("문자를 입력하세요: ")
#     wordlenth = len(word)
#     if wordlenth == 0:
#         print(wordlenth)
#         break
#     elif 5 <= wordlenth <= 8:  # ok
#         continue
#     elif wordlenth < 5:
#         result = '*'+word+'*'
#     elif wordlenth > 8:
#         result = '$'+word+'$'
#     print(f'유효한 입력 결과 : {result}')
