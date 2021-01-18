# 제공된 sample.txt 파일을 읽고 sample_yyyy_mm_dd.txt 파일에 그대로 출력하는 프로그램을 구현한다.
# 이 파일은 append 모드로 오픈하여 여러 번 테스트하면 sample.txt 파일의 내용이
# sample_yyyy_mm_dd.txt 파일에 계속 추가되게 한다.
# 위의 내용을 파일에 저장하는 기능이 정상적으로 수행되면 화면에 “저장이 완료되었습니다.”
# FileNotFoundError 발생시 FileNotFoundError 에 대한 메시지 정보를 출력하고 종료한다.

# 2021-01-18 풀이

f1 = None
f2 = None
try:
    f1 = open("sample.txt", "rt", encoding="utf8")
    text1 = f1.read()
    print(text1)
    f2= open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")
    text2 = f2.write(text1)
    print(text2)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f1.close()
    f2.close()
print("저장이 완료되었습니다.")


