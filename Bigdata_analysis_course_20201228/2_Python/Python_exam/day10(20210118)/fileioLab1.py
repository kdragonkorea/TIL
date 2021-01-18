# 다음 내용을 생성해서 c:/iotest/today.txt 라는 파일에 저장한다.
# c:/iotest 디렉토리의 존재여부를 채크하고 존재하지 않으면 새로이 생성한다.
# 출력 내용은 다음과 같습니다. (XXX는 본인의 별명(^^))
# 오늘은 2021년 01월 18일입니다.
# 오늘은 월요일입니다.
# 나는 X요일에 태어났습니다.
# 파일에 위의 내용을 저장한 다음에 화면에는“저장이 완료되었습니다.”를 출력한다.

# 2021-01-18 풀이

import os
if not os.path.isdir("c:/iotest"):
    os.mkdir("c:/iotest")
    print("c:/iotest 폴더 생성")
else :
    print("c:/iotest 폴더는 이미 존재!!")

f = open("c:/iotest/today.txt", "wt", encoding="UTF-8")
print(f)
f.write("""오늘은 2021년 01월 18일입니다.
오늘은 월요일입니다.
나는 월요일에 태어났습니다.""")
f.close()

try:
    f = open("c:/iotest/today.txt", "rt", encoding="UTF-8")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    if f :
        f.close()
print("저장이 완료되었습니다.")
