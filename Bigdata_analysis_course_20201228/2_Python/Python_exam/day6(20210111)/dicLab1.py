# 다음 내용으로 구성되는 딕셔너리를 하나 생성한다.
# 키 : red, blue, green, yellow, orange, black, white, violet, pink, lime
# 값 : https://www.w3schools.com/colors/colors_picker.asp 사이트에 가서 이 칼라들의
# #으로 시작하는 RGB 값을 찾아서 사용한다.
# 사용자에게 “칼라명을 영문으로 입력하세요 :”를 출력하면서 칼라명 한 개를 입력받고 미리 생성한 딕셔너리에서
# 그 칼라에 해당하는 RGB 값을 추출해서 “xx 칼라의 RGB 값은 xxx 입니다” 를 출력하며
# 딕셔너리에 없는 칼라명이 입력된 경우에는 “xx 칼라의 RGB 값을 찾을 수 없습니다”

dict = {'red':'ff0000',
'blue':'0000ff',
'green':'008000',
'yellow':'ffff00',
'orange':'ffa500',
'black':'000000',
'white':'ffffff',
'violet':'ee82ee',
'pink':'ffc0cb',
'lime':'00ff00'}
print(dict)