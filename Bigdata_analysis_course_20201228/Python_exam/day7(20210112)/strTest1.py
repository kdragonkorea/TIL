# =============== index  ===============
s = "python"
print(s[2])
print(s[-2])

# =============== stringindex  ===============
s = "python"
for c in s:
    print(c, end="")

# =============== slice  ===============
s = "python"
print("\n"+s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])
print(s[2:4])

# =============== slice2  ===============
file = "20171224-104830.jpg"
print("촬영 날짜 : " + file[4:6] + "월 " + file[6:8] + "일")
print("촬영 시간 : " + file[9:11] + "시 " + file[11:13] + "분")
print("확장자 : " + file[-3:])
# .의 위치를 찾아서 +1부터 끝까지 출력한다.
print(file.index("."))
print("확장자 : " + file[file.index(".")+1:])

# =============== slice3  ===============
yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])

# =============== unpacking  ===============
a,b,c,d,e,f,g = yoil
print(a,b,c,d,e,f,g)

# find와 index 출력 결과가 동일하지만 help를 이용해서 차이점을 알 수 있다.
help(s.find)
help(s.index)