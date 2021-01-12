a = 100
print(type(a))
print(a.bit_length())
print(bin(a))

b = 3.14
print(type(b))
print(b.real)
print(b.is_integer())

c = 3+4j
print(type(c))
print(c.real)
print(c.imag)

d = False
print(type(d))
print(d.bit_length())
print(bin(d))

e = " "
print(type(e))
print(e.isspace())
print(e.join("ㅋㅋㅋ"))
# 변수: x
# 메소드: join
# 결과:

f = []
print(type(f))
print(f.extend([1,2,3]))
print(f.reverse())
print(f)
# 변수: x
# 메소드: extend
# 결과:

# 변수: x
# 메소드: reverse
# 결과:

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))

