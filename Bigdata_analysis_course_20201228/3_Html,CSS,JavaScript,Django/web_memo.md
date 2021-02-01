[TOC]

# 자바스크립트

* 웹 페이지의 동적인 처리를 구현하는 프로그래밍 언어
* HTML 파일 안에 구현하는 프로그래밍 언어로서 `인터프리터 언어` 
* `<script>`태그의  컨텐트로 작성하거나 HTML 태그에 정의된 속성의 값으로 작성
* 구문: 파이썬 그리고 R과 많은 부분 비슷한 구문을 가지고 있으며, 3개 모두 `인터프리터 언어`로 분류
  * 변수 정의 방법과 처리 가능한 데이터 타입
  * 연산자와 제어문
  * 배열(array) - 파이썬에서는 리스트
  * 함수 정의 방법, 함수 사용 방법(호출), 함수는 일급 객체 (파이썬과 비슷함)
  * 객체 생성 방법 (1/21 교육 예정)
    * 클래스를 가지고 객체를 생성하는 방법
    * {}를 사용해서 객체를 생성하는 방법 - 객체리터럴 방법 (더 많이 사용)
  * 이벤트 처리하는 방법, DOM 객체를 통해서 HTML태그를 제어하는 방법 (1/21 교육 예정)
  * jQuery:  JavaScript의 대표적인 API로 간단한 자바스크립트 구현을 지원



## 주요 3개 호출문

* **window.alert() 호출:** 사용자에게 메세지를 보여주고 확인받는 용도
* **window.prompt() 호출:** 사용자로 부터 데이터를 입력받는 용도
* **window.confirm() 호출:** yes 또는 no 둘중 하나를 입력받는 용도



## 제어문

#### 조건제어문: if, switch

```javascript
if(조건식)
    수행문장;

if(조건식){
    수행문장;
    수행문장;
    ...
}
    
if(조건식){
 	수행문장;
else
    ...
}

if(조건식){
    수행문장;
else if(조건식)
    수행문장;
else if (조건식)
    수행문장;
else
    수행문장;
}
```

#### 반복제어문: for, while, do~while

* 일반(전통)for - [exam7-1](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam7_1.html)

  ```javascript
  for(초기식;조건식;증감식)
      반복수행문장
  for(변수정의와초기화식;반복처리를계속할지결정하는조건식;변수의값을변화시키는식)
  for(var num=1; num < 11; num+=1) ---> 10번 반복
  for(var num=10; num > 0; num-=1) ---> 10번 반복
  for(var num=10; num < 20; num+=1) ---> 10번 반복
  for(var num=1; num <= 50; num+=1) ---> 1부터 50까지의 값을 1씩 증가시키면서 처리하시오.
  for(var num=1; num <= 50; num+=2)   ---> 1부터 50까지의 값을 2씩 증가시키면서 처리하시오.
  ```

* 향상된for, for-each, for-in   :  for (변수정의 in 배열 또는 객체)

  ```javascript
  a = [10,20,30,40,50]  // 배열, array
  //파이썬
  for data in a :
  print(data)   --> 10 20 30 40 50 이 행단위로 값출력
  //자바스크립트
  for(var i in a) {
  window.alert(i);  --> 0, 1, 2, 3, 4 와 같이 인덱스로 출력
  }
  //자바스크립트
  for(var i in a) {
  window.alert(a[i]); --> 10, 20, 30, 40, 50 각 인덱스의 데이터를 출력
  }
  ```

* while - [exam7-2](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam7_2.html)

  ```javascript
  while(조건식)
      반복문장;
  
  while(true)
      무한반복문장;
  ```

#### 분기제어문: break, continue

* break :  반복문을 종료해라
* continue : 다음 반복으로 계속해서 진행해라.



## API : Application Programming Interface

> 프로그래밍을 할 때 자주 구현되는 기능들을 미리 구현해 놓은 프로그램으로 프로그래밍 언어마다 자기만의 API를 가지고 있으며, 개발환경을 구축할 때 함께 설치되는 API를 표준 API라고 하며 개발자가 필요에 의해 추가로 설치하는 API들을 확장 API 또는 third-party API라고 한다.

* C의 API: 함수
* Java의 API: 클래스(메서드)
* Python, JavaScript, R의 API: 함수, 클래스(메서드)



## 메소드 모음

#### Math.random(): 0 ~ 1 사이의 수를 반환 - [exam8](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam8.html), [exam8-1](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam8_1.html)

#### Math.floor():  정수만 반환

#### console.log(): 



## 연산

- === : 두 데이터의 타입과 값을 동시에 비교연산

- `&&`와 `||` 연산자

  - 논리연산으로 `&&` 앞이 참이면, 뒤를 출력, `||` 앞이 거짓이면, 뒤를 출력

- pre태그 : script의 수행결과에 대해서 자동으로 행을 변경

- 언어별 주석 표기 방법

  | HTML          | CSS        | JavaScript | Python |
  | ------------- | ---------- | ---------- | ------ |
  | <!-- 내용 --> | /* 내용 */ | //내용     | #내용  |




## 배열

> [exam9](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam9.html), [exam10](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam10.html), [exam11](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam11.html)

- 여러  데이터들을 하나의 묶음으로 다루고자 할 때 사용
- 묶을 수 있는 데이터의 갯수에 제한이 없고, 데이터 타입도 제한이 없다.
- 자바스크립트의 배열도 객체로 취급된다.
- 배열 생성 방법 (아래 2개중 자유롭게 사용 가능)
  - 배열 리터럴 방법 
    - ex) [], [1,2,3,4,5], ['aaa', 1, 2, 'bbb', true], [ ,,,,,, ]
  - API를 이용하는 방법
    - ex) new Array(1,2,3,4,5), new Array('aaa', 1, 2, 'bbb', true), new Array(), new Array(8),
- 배열 사용 방법
  - 배열의 크기(배열을 구성하는 엘리먼트의 갯수)
  - 배열객체의 length 라는 속성(변수)의 값을 사용
  - 배열의 요소(원소, 엘리먼트)를 접근하여 L-value, R-value 모두 가능하며 인덱스는 0부터 시작한다.
- 배열의 데이터를 `문자열` 기준으로 분류하는 방법: `배열변수명.sort();`
- 배열의 데이터를 `숫자순` 기준으로 분류하는 방법: `배열변수명.sort(function(a,b){return a-b;});`
- 배열에서 데이터를 추가하는 방법: `배열변수명.push(데이터);`



## 함수

> [exam13](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam13.html), [exam14](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam14.html), [exam15](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam15.html), [exam16](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam16.html), [exam17](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam17.html), [exam18](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/3_Html%2CCSS%2CJavaScript/nginx-1.18.0/html/edu/jsexam/exam18.html)

- 함수를 만드는 방법

  ```javascript
  function 함수명([매개변수...]) {
      함수의 수행 코드들 ...
      return 리턴값;
  }
  
  변수 함수명([매개변수...]) {
      함수의 수행 코드들 ...
      return 리턴값;
  }
  ```

- 자바스크립트에서 함수의 특징

  - 일급객체로 취급되어 함수를 변수에 담아서 사용할 수 있고 함수 호출 시 아규먼트로 전달 가능하며 리턴값을 함수로 전달 가능하다.
  - 함수를 호출할 때 함수에 정의된 매개변수만큼 아규먼트를 전달하지 않아도 호출 가능하다.
  - 함수가 값을 리턴하지 않으면 undefined 가 자동으로 리턴된다.
  - 가변인수를 지원하여 함수 호출 시 아규먼트의 갯수에 제한이 없는 함수를 만들 수 있다. (가변인수 함수를 정의할 때는 매개변수 정의를 생략하고 함수 호출 시 자동으로 만들어지는 arguments 라는 배열을 활용한다)

- 함수를 사용하는 방법 (호출, R-value)



## 변수

> exam15, exam16, exam17, exam18, exam19, exam20

#### 자바스크립트의 변수 정의

- **var, let, const**
  - const는 상수로 한번 사용하면 변경이 불가하다.
  - let은 2번 이상 변수를 선언할 수 없다?



## 객체

> exam21, exam22, exam23

#### 자바스크립트의 객체 생성방법

- 객체리터럴

  - 배열객체: [1, 'abc', true, 3.4]

  - 객체: {속성명:속성값, 속성명:속성값, ...}

    - 속성명: 자바스크립트의 식별자 규칙(명명규칙), 문자로시작, 문자, 숫자, "_"를 사용할 수 있다.

    - 속성값: 숫자, 문자열, 논리값, 배열, 객체, 함수(메서드)

      ```javascript
      obj={속성명1:100, 속성명2:"둘리",속성명3:function()}
      obj.속성명 = 200 (가능)
      obj.속성명2 + "승리" (가능)
      ```

- 클래스(생성자함수)를 이용하는 방법

  - new Array()
  - new Date() - 현재 날짜를 나타냄

- 내장 객체

  - 개발자가 객체를 생성하지 않아도 자바스크립트 엔진이 자동으로 생성해주는 객체
  - window, document, navigator, screen, location, DOM객체들..



## DOM(Document Object Model) 프로그래밍



### DOM객체

> 브라우저가 웹 페이지를 해석하고 랜더링할 때 인식된 각각의 태그들을 자바스크립트 객체로 생성하며 이 객체들을 DOM 객체라고 한다. 생성되는 DOM 객체들은 부모 자식 관계를 적용하여 트리구조로 구성한다.

### DOM 프로그래밍에서 익혀야 하는 것

- 동적인 처리를 하려는 태그의 DOM 객체를 찾는 방법

  - document.getElementsByTagName
  - document.getElementById
  - document.getElementsByClassName
  - document.querySelectorAll
  - document.querySelector

- DOM 객체 타입

  - Element 타입
  - Attribute 타입
  - Text 타입


### 찾은 DOM 객체를 가지고 필요한 동적처리를 구현하는 방법

- 컨텐트 변경하기

  - dom.innerHTML = "<p>새로운내용</p>"
  - dom.textContent = "새로운내용"

- 스타일 바꾸기

  - dom.style.CSS속성명 = CSS속성값

  - dom.style.color = "red"

  - dom.style.**background-color** = "red" (x)

    background**-**color 는 background**C**olor 로 사용해야 한다.

- 이벤트 핸들러 등록하기 (3가지)

  - 인라인 이벤트 모델(지역적 방식)

    <태그명 on이벤트명="이벤트핸들러코드">

  - 고전 이벤트 모델(전역적 방식)

    DOM 객체를 찾는다

    dom.on이벤트명 = function () {.....}

  - 표준 이벤트 모델(전역적 방식)

    DOM 객체를 찾는다.

    dom.addEventListener("이벤트명",function () { ...})



## jQuery 라이브러리

> API 사용 방법이 일관성 있어서 API를 익히기 쉽다.

html(): innerHTML -

text(): textContent -

val(): value - 

css()

attr()

#### jQuery의 이벤트 핸들러 구현

- $('...').on('이벤트이름',함수)

  $('...').on(자바스크립트객체)



## map

> geolocation, geocoding, ggmap1, ggmap2, ggmap3, ggmap4, ggmap5, ggmap6 

```javascript
function showPosition(position) {
    x.innerHTML="위도: " + position.coords.latitude + "<br />경도: " + position.coords.longitude;
```



# 장고(Django)

- http 상태코드
  - 200: 성공
  - 404: 실패, 잘못 요청
  - 500: 실패, 요청한거 실행 에러

#### HttpRequest 와 HttpResponse

- HttpRequest - HTTP 프로토콜기반으로 요청이 왔을 때 요청 관련 정보를 제공하는 객체로 뷰함수가 호출될 때 아규먼트로 전달된다. (장고서버가 객체를 생성)
- HttpResponse - HTTP 프로토콜기반으로 온 요청에 대한 응답시 사용하는 객체로 응답 내용을 담게 된다. (HTML 태그문자열, 템플릿을 사용한 랜더객체)



### Django 개발환경 구축방법

#### 가상환경구축

1. `python_venv` 폴더를 원하는 장소에 생성 후 cmd창에서 아래와 같이 입력한다.

   djangovenv생성: `python -m venv djangovenv`

   ```
   C:\Users\kangyong\TIL\Bigdata_analysis_course_20201228\python_venv
   
   C:\Users...\python_venv>python -m venv djangovenv
   ```

2. `djangovenv` 폴더에 `Scripts` 폴더로 이동하여 `activate` 프로그램을 실행한다.

   ```
   C:\Users\...\python_venv>cd djangovenv\Scripts
   
   C:\Users\...\python_venv>cd djangovenv\Scripts>activate
   ```

3. cmd창에서 `activate` 실행한 후 좌측에 `(djangovenv)` 가 붙은 것을 볼 수 있으며, 가상환경이 활성화된 상태로 인식하면 된다. Django 개발 환경을 설치하지 않았을 경우 `pip install django` 를 입력하여 설치를 진행한다.

   ```
   (djangovenv) C:\Users\...\python_venv>cd djangovenv\Scripts>
   
   (djangovenv) C:\Users\...\python_venv>cd djangovenv\Scripts>pip install django
   ```

4. 버전 업그레이드와 관련된 경고문구가 나올 경우 `python -m pip install --upgrade pip` 명령어를 입력해서 업그레이드를 진행한다.

   ```
   (djangovenv) C:\Users\...\python_venv>cd djangovenv\Scripts>python -m pip install --upgrade pip
   ```



## 장고 프로젝트 만들기

1. `DJANGOexam`폴더를 원하는 장소에 생성 후 cmd창에서 해당 폴더로 이동하여 아래와 같이 명령어를 입력하여 장고 프로젝트를 생성한다.

   장고 프로젝트 생성: `django-admin startproject (원하는폴더명)`

   ```
   (djangovenv) C:\Users\...\DJANGOexam>
   
   (djangovenv) C:\Users\...\DJANGOexam>django-admin startproject studyproject(원하는 폴더명으로 변경 가능)
   ```

2. 생성된 studyproject 폴더로 이동하여 `python manage.py runserver`를 입력해서 장고에 내장된 서버를 기동시킨다.

   ```
   (djangovenv) C:\Users\...\DJANGOexam>cd studyproject
   
   (djangovenv) C:\Users\...\DJANGOexam\studyproject>python manage.py runserver
   
   ...
   Quit the server with CTRL-BREAK
   ```

3. 크롬 브라우저에서 http://localhost:800/ 입력하여 요청하면 장고의 기본 웹 페이지가 출력되는 것을 알수 있다.

4. 파이참 File - Settings 에서 장고 프로젝트 생성한 폴더(`studyproject`)를 가상환경으로 선택한다. **(장고강의교안 참조)**

5. 파이참 하단 터미널을 선택하여 학습할 소스들을 작성할 폴더를 생성한다. (firstapp)

   ```
   (djangovenv) C:\Users\...\DJANGOexam\studyproject>
   
   (djangovenv) C:\Users\...\DJANGOexam\studyproject>python manage.py startapp firstapp
   ```

6. 파이참에서 studyproject의 `settings.py`와 `urls.py` 그리고 firstapp의 `views.py` 세 개의 파일을 수정한다. **(장고강의교안 참조)**

7. 파이참 터미널에서 서버를 기동시킨다. (`python manage.py runserver`)

   ```
   (djangovenv) C:\Users\...\DJANGOexam\studyproject>python manage.py runserver
   ```

8. 브라우저(크롬)에서 URL 로 요청하여 정상적으로 출력 되는지 확인한다.



### Query 문자열

> HTTP Client가 HTTP Server 요청시 서버에서 요청하려는 대상의 URI가 전달되는데 이 때 함께 전달될 수 있는 문자열이다.

- name = value형식으로 구성되어야 한다.

- 여러개의 name=value가 사용될 때는 & 기호로 구분되게 구성해야 한다.

- 영문과 숫자는 그대로 전달되지만 한글과 특수문자들은 %기호와 16진수 코드값으로 전달된다. (UTF-8)

- 공백문자는 +기호 또는 %2C로 전달된다.

- Query 문자열을 가지고 HTTP Server에게 정보를 요청할 때는 두가지 요청 방식중에 한개를 선택할 수 있다.

  - GET : Query 문자열이 외부에 보여진다. 요청 URL 뒤에 ? 기호와 함께 전달되기 때문이다.
  - POST : Query 문자열이 외부에 보여지지 않는다. Query 문자열의 길이에 제한이 없다. 

  

#### GET방식과 POST방식의 차이

- POST방식은 query 문자(url)가 노출이 안되기 때문에 `로그인할 때` 또는 보여주고 싶지 않을 때 사용한다. 

- GET방식은 query 문자(url)가 노출되고 관계없을 때 사용한다.



#### XML / JSON

- GML
  - SGML
    - XML: 규격화 시킨 문서를 만들고 싶을 때 사용, 태그명을 용도에 맞게 직접 정의하여 사용 가능하다.
    - HTML: 웹페이지제작에 사용되는 전용 마크업 언어

- JSON (JavaScript Object Notation)



#### AJAX의 핵심내용

- JSON(XML) 형식으로 응답하는 뷰를 준비해야 한다. (템플릿을 거치지 않고 뷰가 직접응답)

- JavaScript만 사용해서 AJAX 요청을 구현하는 방법

  ```
  var xhr = new XMLHttpRequest()
  xhr.onload = 함수
  xhr.open("GET",대상URL,true)
  xhr.send()
  ```

- jQuery API를 사용하여 AJAX 요청을 구현하는 방법

  ```
  $.getJSON("대상URL",함수)
  
  $.ajax({........})
  ```

  

- css table sample: https://www.w3schools.com/bootstrap4/bootstrap_tables.asp
  
- exam24.html
  
  - 카카오맵 AJAX 이용
  
- 서울시 빅데이터 OPEN API
  - json: http://openapi.seoul.go.kr:8088/796143536a756e69313134667752417a/json/LampScpgmtb/1/100/
  - xml: http://openapi.seoul.go.kr:8088/796143536a756e69313134667752417a/xml/LampScpgmtb/1/100/
  
- 



## Django Templates 예제 모음

- `변수와 로직`태그를 사용한 예제

  - [exam4.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam4.html)

  ```
  {% for num in numbers %}
    <li>{{num}}</li>
  {% endfor %}
  ```

  - [exam5.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam5.html)

  ```
  {% if '게스트' == name  and '작성안함' == address %}
  <h1> 이름과 주소를 작성하지 않았군요ㅜㅜ</h1>
  {% else %}
  <h1>당신의 이름은 {{name}} 이고 주소는 {{address}} 이군요</h1>
  {% endif %}
  ```

  - [exam6.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam6.html)

  ```
  {% if num %}
       <h2>결과 값 : {{ num }}</h2>
  {% else %}
      <form method="POST" action="/secondapp/exam6/">
          {% csrf_token %}
          <input type="number" name="number" placeholder="숫자를 입력하세요" required>
          <input type="submit" value="POST방식으로요청~~~">
      </form>
  {% endif %}
  ```

- `block과 extends 태그`를 사용한 예제 (html파일 내용의 반복을 줄여준다)

- query를 이용하여 GET을 호출

  - [exam8.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam8.html)

- `매개변수`를 사용한 예제

  - [exam10.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam10.html), [exam11.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam11.html), [exam12.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam12.html), [exam14.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam1.html)
  - urls.py

  ```
  path('exam11/<name>/<int:age>', views.exam11, name='exam11'),
  path('exam12/<int:num1>/<num2>', views.exam12, name='exam12'),
  path('exam14/<word>/<int:num1>/<num2>', views.exam14, name='exam14'),
  ```

  - range, sorted를 사용하여 lotto번호 출력: exam18.html
  - current_date를 이용하여 현재 시간 출력: exam19.html

- `Ajax`를 사용한 예제 

  - [exam20.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam20.html)
  - [exam21.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam21.html)
  - [exam22.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam22.html)
  - [exam23.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam23.html)
  - [exam24.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/exam24.html)

- `google map`를 사용한 예제 

  - [ggmap1.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap1.html)
  - [ggmap2.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap2.html), marker 표시
  - [ggmap3.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap3.html), marker 표시, contentString 표시
  - [ggmap4.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap4.html), map사이즈 조절, 현 위치로 출력
  - [ggmap5.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap5.html), js를 이용하여 주소 입력 후 출력
  - [ggmap6.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap6.html), jQuery를 이용하여 주소 입력 후 출력
  - [ggmap7.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/ggmap7.html), marker 5개를 이미지로 출력 후 위도와 경도 평균값 위치로 출력

- `kakao map`를 사용한 예제 

  > 카카오맵: http://apis.map.kakao.com/web/sample/

  - [kkmap1.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap1.html), map만 표시
  - [kkmap2.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap2.html), map과 사용자 control 추가 (지도/스카이뷰, zoom in/out)
  - [kkmap3.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap3.html), 타입 추가 (교통정보, 로드뷰, 지형정보, 지적편집도)
  - [kkmap4.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap4.html), marker 표시
  - [kkmap5.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap5.html), marker 표시, infowindow(글상자) 표시, 텍스트와 링크 표시
  - [kkmap6.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap6.html), marker 표시, infowindow(글상자) 표시(생성/제거)
  - [kkmap7.html](https://github.com/kdragonkorea/TIL/blob/master/Bigdata_analysis_course_20201228/DJANGOexam/studyproject/secondapp/templates/kkmap7.html), marker 여러개 표시, infowindow(글상자), mouseover 이벤트(오버/아웃)

### Django 모델

#### CRUD

> Create, Read, Update, Delete

- SQL에서 CRUD를 (INSERT, SELECT, UPDATE, DELETE) Django에서는 API로 사용 가능하다.

#### Django 가지고 Database를 연동(CRUD)하는 구현 과정

1. 모델 클래스를 생성한다. (models.py)

   Model 이라는 클래스를 상속하고 만들려는 DB테이블의 컬럼 사양에 맞추어 클래스 변수를 정의한다.

2. Django에서 제공하는 명령을 수행시켜서 모델클래스에 알맞는 DB 테이블을 생성한다.
3. 모델클래스를 통해서 CRUD를 구현한다.
   - C - 모델클래스의 객체를 생성한 후 save() 메서드 호출
   - R - `모델클래스.objects.all()`, `모델클래스.objects.filter(...)`, `모델클래스.objects.order_by(...)`, `모델클래스.objects.first()`, `모델클래스.objects.last()`, `모델클래스.objects.count()`

## 장고 모델 DB 테이블의 SQL 만들기

1. 폴더(app)를 생성한다.

   장고 생성: `python manage.py startapp (원하는폴더명)`

   ```
   (djangovenv) C:\Users\...\DJANGOexam>django-admin startproject studyproject(원하는 폴더명으로 변경 가능)
   ```

2. settings에

3. SQLite 생성

4. 