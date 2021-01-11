def printdeco(*p, deco="@") :   # 기본값을 가지고 있는 일반 변수는 가변인수 뒤에 올수 있다.
    for data in p :
        print(deco, data, deco)
    print()

printdeco(1,2,3,4,5)
printdeco("가", "나")
printdeco(True, "A", 10, deco="$")
