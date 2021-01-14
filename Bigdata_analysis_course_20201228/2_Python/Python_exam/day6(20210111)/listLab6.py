# for i in range(10, 41, 2):
list1 = [[10, 12, 14, 16],[18, 20, 22, 24],[26, 28, 30, 32],[34, 36, 38, 40]]

print('1행 1열의 데이터: ', list1[0][0])
print('3행 4열의 데이터: ', list1[2][3])
print('행의 갯수 : ', len(list1)) # 행의 list
print('열의 갯수 : ', len(list1[0])) # 0행의 열의 list
print('3행의 데이터들 : ', list1[2][0],list1[2][1],list1[2][2],list1[2][3])
print('2열의 데이터들 : ', list1[1][0],list1[1][1],list1[1][2],list1[1][3])
print('왼쪽 대각선 데이터들 : ', list1[0][0],list1[1][1],list1[2][2],list1[3][3]) # 10 20 30 40
print('오른쪽 대각선 데이터들 : ', list1[0][3],list1[1][2],list1[2][1],list1[3][0]) # 16 22 28 34

for i in range(len(list1)):
    print(list1[i][i],end=" ")
print()

j = len(list1[0])
for i in range(len(list1)):
    print(list1[i][j-1], end=" ")
    j = j - 1