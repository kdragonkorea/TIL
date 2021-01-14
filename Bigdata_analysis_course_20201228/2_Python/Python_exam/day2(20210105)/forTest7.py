for dan in range(2, 10):
    for num in range(2, 10):
        result = dan * num
        if result > 30 :
            break
        print(dan, "*", num, "=", result, end="\t")
    print()

    # 구구단에서 결과값이 30보다 작은 것들만 나열
    # 2 * 2 = 4    2 * 3 = ...
    # 3 * 2 ..
    # ..
    # 9 * 3 = 27