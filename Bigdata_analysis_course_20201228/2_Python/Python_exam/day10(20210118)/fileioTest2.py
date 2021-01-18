try:
    f = open("live.txt", "rt", encoding="UTF-8")
    print(f, type(f))
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()

print("*"*20)
f = None
try:
    f = open("live.txt", "rt", encoding="utf8")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    if f :
        f.close()