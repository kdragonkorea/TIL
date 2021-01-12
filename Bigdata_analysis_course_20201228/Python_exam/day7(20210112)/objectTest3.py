import datetime     # datetime:

print([4,15,2,30,4].count(4))   # 리스트에서 4는 몇개인가?
listv = [4,15,2,30,4]
print(listv.count(4))           # listv에서 4는 몇개인가?

now = datetime.date.today()
print(now, type(now))
print(now.weekday())    # 월:0, 화:1, 수:2, 목:3, 금:4, 토:5, 일:6
print(now.ctime())
print("===2021년 크리스마스===")
christmas = datetime.date(2021, 12, 25)
print(christmas, type(christmas))
print(christmas.weekday())
print(christmas.ctime())