## CLI

Command Line interface

커맨드(명령어)를 통해 작동하는 인터페이스



## CLI vs. GUI

* **CLI**: Command Line Interface (터미널)
  * 명령어를 입력하여 컴퓨터를 조작
* GUI: Graphic User Interface (윈도우/보통의 프로그램)



### 기초 명령어

#### (1) pwd

* **pwd**(print working directory): 현재 폴더의 경로
* **~** (home directory): 홈 디렉토리 (git bash 처음 열면 나오는 기본 폴더), 가장 기본이 되는 폴더



### (2) ls

* ls(list): 해당 디렉토리의 내용을 출력



#### (3) cd [폴더명/경로명]

* cd(change directory): 디렉토리(폴더)를 이동/변경, 경로&파일은 `tab`으로 자동완성 가능
* `cd ..`: 상위 디렉토리(폴더)로 이동
* `cd .`: 현재 디렉토리(폴더)로 이동
* `~`: 홈 디렉토리(폴더)로 이동
* `/`: 루트 디렉토리(폴더)로 이동



#### (4) mkdir [폴더명]

* mkdir (make directory): 폴더를 생성



#### (5) rm [파일명]

* rm(remove): 파일을 삭제



#### (6) rm -r [폴더명]

* -r : recursively(재귀적으로) 폴더를 삭제



#### (7) touch [파일명]

* touch : 파일생성



#### (8) cp [파일명] [위치]

* cp(copy) : 파일 복사



#### (9) cp - r [폴더명] [위치]

* 폴더를 복사



#### (10) mv [파일/폴더명]  [바꿀파일/폴더명]

* mv(move): 파일/폴더명 변경
* mv [파일/폴더명] [위치] : 파일 또는 폴더를 **이동**



#### (11) Cat [파일명]

* 내용 출력