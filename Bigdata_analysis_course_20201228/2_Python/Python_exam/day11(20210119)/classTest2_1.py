class Student :
   def __init__(self):          # 객체 생성시 자동으로 생성되는 메소드
       print("인스턴스 생성!!")
       print(self)

   def __del__(self):           # 객체 생성시 자동으로 생성되는 메소드
       print("인스턴스 삭제!!")

st1 = Student()
st2 = Student()
st3 = Student()

print(type(st1), st1)
print(type(st2), st2)
print(type(st3), st3)

print("[ st1이 참조하고 있는 Student 인스턴스 삭제]")
del st1

print("종료")