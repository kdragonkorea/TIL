for dan in range(2, 10):
    print(dan, "단")
    for num in range(2, 10):
        print(dan, "*", num, "=", dan * num, end="\t")
    print()

    # 2단 ~ 9단 출력 (2단일 경우 2단 * 2 ~ 9 = 2 * 2 ~9 를 반복적으로 출력)
    # 2단
    # 2 * 2 = 4 2 * 3 = 6