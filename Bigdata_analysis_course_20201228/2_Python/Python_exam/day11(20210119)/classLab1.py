class Member:
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthday = None

m1 = Member()
m2 = Member()
m3 = Member()

m1.name = 'kim'
m1.account = 'kimm'
m1.passwd = '1234'
m1.birthday = '2021-01-01'

m2.name = 'kang'
m2.account = 'kangg'
m2.passwd = '1234'
m2.birthday = '2021-01-01'

m3.name = 'lee'
m3.account = 'leee'
m3.passwd = '1234'
m3.birthday = '2021-01-01'

print(f'회원1: {s1.name}',{s1.account}')












# 2021-01-10 풀이1
# class Member:
#    def __init__(self, name, account, passwd, birthday):
#        self.name = name
#        self.account = account
#        self.passwd = passwd
#        self.birthday = birthday
#
#    def printMemberInfo(self):
#        print("회원: {}({},{},{})".format(self.name, self.account, self.passwd, self.birthday))
#
# m1 = Member("홍길동",'hong', 1234, '2020-01-01')
#
# m1.printMemberInfo()