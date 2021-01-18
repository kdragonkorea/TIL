try:
    f = open("live.txt", "rt", encoding="UTF-8")    # rt=read text
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
finally:                # 참/불참인 경우를 지정해서 주는 것이 에러를 방지할 수 있다.
    if f :              # f가 참인 경우 f
        f.close()       # f가 참이 아닌 경우 close