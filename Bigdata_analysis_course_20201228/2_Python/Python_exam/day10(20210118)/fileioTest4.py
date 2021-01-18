f = open("live.txt", "rt", encoding="UTF-8", errors='ignore')
print("[seek기능 처리가능]" if f.seekable() else "[seek기능 처리불가]" )
f.seek(12,0)               # seek은 원하는 곳 부터 출력(bite수를 적용/한글3byte,빈칸은1byte)
text = f.read()
f.close()
print(text)

# =============== append  ===============
f = open("live.txt", "at", encoding="UTF-8")    # at은 append와 같다.
f.write("\n\n[추가]푸쉬킨 형님의 말씀이었습니다.")
f.close()

# =============== withas  ===============
with open("live.txt", "rt", encoding="UTF-8") as f:      # with는 자동으로 close를 발생함.
   text = f.read()
print(text)
