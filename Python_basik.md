# 23/01/13 Python 기초

### 파이썬 기초

컴퓨터 프로그래밍 언어 == 컴퓨터에게 무언가를 시킬 때 쓰는 말

- **why python?**
  
  1. 쉽다.
  
  2. 강력하다.
  
  3. 많은 사람들이 사용한다.
  - 기술을 사용하기 위한, 결과물을 만들기 위한 기초 학습
  
  

### python의 문법

- 저장
  
  - **변수(Variable)** : 하나의 값을 저장할 수 있는 공간
    - 숫자 : 현실 세계에 존재하는 모든 숫자, 기본적인 연산이 가능.
    - 글자 : 현실 세계에 존재하는 모든 글자, 따옴표로 둘러싼 글자 or 숫자
    - 참/거짓 : True, False 단 두 가지! 조건/반복에 사용됨, None은 값이 없음을 나타냄
  - **리스트(List)** : 여러 개의 연속된 값을 저장할 수 있는 저장 공간
  
  ```python
  menu =['닭고기온메밀국수','토마토 리조또','무파마','김치찜']
  
  print(menu)
  print(menu[3])
  ```
  
  - **딕셔너리(Dictionary)** : 이름표를 단 여러 개의 값을 저장할 수 있는 저장 공간
    
    - **Key**는 중복 불가, **Value**는 중복 가능
    
    ```python
    # student = {'홍진완':50, '김성현':50, '홍진완':49}
    # print(student)
    # 홍진완이 중복되어 value가 50인 홍진완은 삭제되고 49인 홍진완만 남는다.
    
    student = {
        '강남구':'비싸다',
        '종로구':[1,2,3],
        '서대문구':{
                '김구현':13,
                'viktor':['여기도','dict의','value이다.']
            }
        }
    
    menu = [['아침','점심','저녁'],{'강남구':50,'서대문구':47}]
    
    print(student)
    print(menu[0][1])                       # 점심
    print(menu[1]['서대문구'])              # 47
    print(student['서대문구']['viktor'][1]) # dict의
    ```

- 조건
  
  - **if, else**
    - 만약 xxx면 yyy해줘 아니면 zzz해줘
  - **elif :** 추가조건
  
  ```python
  dust = int(input())
  if dust > 70 :
      print('70초과')
  elif dust > 50 :
      print('50초과')
  elif dust >30 :
      print('30초과')
  else:
      print("30이하")
  ```

- 반복
  
  - **while :** while에 해당하는 조건일 동안 계속 반복
  
  ```python
  n = 0           # n이 0일때
  while n < 3:    # 만약 n이 3보다 작다면
      print(n)    # 계속 n을 출력하고,
      n+=1        # n에 1을 더해줘
  ```
  
  - **for**: 여러 개의 값을 저장하는 변수에서 반복하여 값을 꺼내어 사용, in뒤에 iterable한 (순회가능한) 친구들이 온다. Dictionary또한 가능
  
  ```python
  numbers=[1,2,3,4]
  
  # numbers 리스트가 가진 모든 요소를 순회 할 때 까지
  # numbers가 가진 각 요소를 출력
  for num in numbers :
      if num % 2 == 1:
          print(num)
  print("끝났니?")
  
  String = '문자열'
  for char in String:
      print(char)
  
  a = {'이':1,'상':2,'훈':3}
  for i in a:
      print(i)
      print(a[i])
  ```
  
  | while 조건 :                             | for value in dust :     |
  | -------------------------------------- | ----------------------- |
  | 조건이 True인 동안 반복적으로 실행되기에 종료 조건이 반드시 필요 | 범위를 반복하기에 종료 조건이 필요가 없음 |

### 

### Python 함수

- 반복하고 싶은 코드 덩어리를 모아 놓은 것
- Built-in Functions(내장함수) - [내장함수 목록](https://docs.python.org/3.9/library/functions.html)
- Non-built-in functions

### 

### 모듈

- 함수나 변수 등을 모아 놓은 파이썬 파일
1. 함수가 포함된 파일을 불러온다.(import)

2. 함수를 사용한다.
- 예시
  
  ```python
  import random   # 모듈 -> 파이썬 파일 : cntl + click
  
  menu =['닭고기온메밀국수','토마토 리조또','무파마','김치찜']
  
  print(menu)
  print(menu[3])
  
  # print(dir(menu))
  print(dir(random))
  print(random.choice(menu))
  print(menu[random.randint(0, 3)])
  ```
  
  ```python
  import random
  
  # 1~45 숫자를 담은 list 생성
  # range(n,m) = n 부터 m-1 까지의 숫자를 생성
  numbers = list(range(1,46))
  print(numbers)
  
  # number가 가진 숫자 중에 무작위 값을 하나씩 6번 뽑기
  # 리스트가 가지고 있는 값중 무작위 값을 뽑는 법은?
  
  # while문을 사용하여 뽑아 보기
  i=0
  while i <6 :
      # 리스트가 가지고 있는 값중 무작위 값을 뽑는 법은?
      # 만약에 이전번에 내가 뽑은 숫자가 이미 my_lotto 리스트에 들어있다면?
      print(numbers.pop(random.randint(0,44-i)))  # random.sample()와 같음
      i += 1
  
  print(random.sample(numbers, 6))
  
  a = int(input("로또 몇장 살래?"))
  for i in range(0,a) :
      print(random.sample(numbers,6))
  
  def sum(a,b) :
      # code in here
      # while
      # if
      return a + b 
  
  print(sum(1,3))
  ```

### 

### 요청과 응답

- **클라이언트**(정보를 원하는) - **서버**(정보를 주는)

### 

### JSON

- chrome web store에서 JSON viewer 설치-[JSON viewer](https://chrome.google.com/webstore/search/json%20viewer?authuser=1?authuser=1&gclid=Cj0KCQiA_P6dBhD1ARIsAAGI7HDlk9wQzZ6-olw1OfjdRK_VzGgH4cWC5wuhiNY6nX01yayi3MBtS7waAoQEEALw_wcB)
- 데이터만을 주고 받기 위한 표기법
- 파이썬의 Dictionary와 List 구조로 쉽게 변환하여 활용 가능
- API의 응답으로 많이 이용

### 

### API

- 두 소프트웨어가 서로 통신할 수 있게 연결해주는 인터페이스

### 

### requests library

- 파이썬에서 요청을 쉽게 보낼 수 있게 도와주는 모듈

- 3rd party library

- 예시 1 random_age
  
  ```python
  import requests
  
  r = requests.get('<https://api.agify.io/?name=이상훈>').json()
  print(r)
  print(type(r))
  print(r['name'],'의 나이는',r['age'],'입니다.')
  ```

- 예시 2 lotto_api

```python
# 파이썬으로 웹 요청 보낼수 있는 라이브러리 불러오기
import requests
import random

# 동행복권 로또 당첨번호 api 사용하기
# (회차 직접 입력)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개(보너스번호 제외)
# (선택사항) - 보너스 번호 확인하기

drwNO = input("회차를 입력해 주세요 : ")
num = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drwNO}").json()
i = 0

numbers = []
for i in range(1,7)  :
    numbers.append(num[f"drwtNo{i}"])
bonus = num["bnusNo"]
print(f"당첨 번호는 {numbers}, 보너스 번호는 {bonus} 입니다.")

first = [0,0,0,0,0,0]
# 4. 이걸 1000번 반복합니다.
for i in range(1000):
    my_numbers = random.sample(range(1,46),6)   # 1. 로또 번호 6개를 추첨 받는다.
    count = 0
    for my_num in my_numbers:       # 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨번호와 일치 하는지 확인한다.
        if my_num in numbers :      #2-1. 확인하는 방법은 낸 번호 6개를 순회하면서 1049회 당첨번호 목록에 해당 숫자가 있는지
            count +=1               # 있다면 당첨횟수 + 1
                                
                                # 그래서 적중 횟수가 
    if count == 6 :             # 6개면 1등
        print("!!!!!1등!!!!!")
        first[0]+=1
    elif count ==5 and bonus in my_numbers:
        print("2등")
        first[1]+=1
    elif count == 5:            # 5개면 3등
        print("3등")
        first[2]+=1    
    elif count ==4 :            # 4개면 4등
        print("4등")
        first[3]+=1
    elif count == 3 :           # 3개면 5등
        print("5등ㅋ")
        first[4]+=1
    else :                      # 2개 이하면 꽝
        print("꽝ㅋ")
        first[5]+=1

print(f"1등:{first[0]}명, 2등:{first[1]} 3등:{first[2]}명, 4등:{first[3]}, 5등:{first[4]}, 꽝:{first[5]}")
```
