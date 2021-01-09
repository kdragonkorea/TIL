endFlag = False
for dan in range(2, 10):
    for num in range(2, 10):
        result = dan * num
        if result > 30 :
            endFlag = True
            break
        print(dan, "*", num, "=", result, end="\t")
    if endFlag :
        break
    print()

    # 2중 for문에 if까지 결합되서 어떻게 구현되는지 이해하기가 어렵다.
    # 구구단의 결과가 30보다 크면 중단하지만
    # enFlag가 처음에 왜 False로 정의하였고, 중간에는 True로 표현하는지 모르겠다.
