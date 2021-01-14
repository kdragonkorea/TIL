dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic.keys())   # 출력예상값: 다시 생각해 보기
print(dic.values()) # 출력예상값: 다시 생각해 보기
print(dic.items())  # 출력예상값: 다시 생각해 보기

keylist = dic.keys()
for key in keylist:
    print(key)

valuelist = dic.values()
for value in valuelist:
    print(value)

itemlist = dic.items()
for item in itemlist:
    print(item)

itemlist = dic.items()  # 가장 많이 사용한다. 한번 호출에 두가지를 불러오기 때문에
for key,value in itemlist:
    print(key, value, sep="-")