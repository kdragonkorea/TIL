dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic)

print(dic['boy'])   # 출력 예상값: 소년
print(dic['book'])  # 출력 예상값: 책
# print(dic['student'])  # 출력 예상값: ?
print(dic.get('student'))   # 출력 예상값: ?
print(dic.get('student', '사전에 없는 단어'))  # 출력 예상값: ?

if 'student' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다.")    # 출력 예상값: 이 단어는..

dic['boy'] = '남자애'
dic['girl'] = '소녀'
del dic['book']
print(dic)  # 출력 예상값: ?
