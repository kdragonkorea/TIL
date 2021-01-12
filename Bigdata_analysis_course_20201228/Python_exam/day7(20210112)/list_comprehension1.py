# 매우 비효율적
numlist1 = []
numlist1.append(1)
numlist1.append(2)
numlist1.append(3)
numlist1.append(4)
numlist1.append(5)
print("list1 = {}".format(numlist1))

# 효율적
numlist2 = []
for n in range(1,6) :
    numlist2.append(n)
print("list2 = {}".format(numlist2))

# 매우 비효율적
numlist3 =[1,2,3,4,5]
print("list3 = {}".format(numlist3))

# 가장 효율적
numlist4 = [ num for num in range(1, 6) ]
print("list4 = {}".format(numlist4))    # print('f({}.......')

