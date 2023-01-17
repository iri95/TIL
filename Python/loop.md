# 23/01/17 제어문

- 순차, 선택, 반복
- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실험(반복)하는 제어가 필요함
- 제어문은 순서도(flowchart)로 표현이 가능
  
  

# 코드 스타일 가이드

- 코드를 ‘어떻게 작성할지’에 대한 가이드라인

- 파이썬에서 제안하는 스타일 가이드(강의에서 사용)
  
  - [PEP8](https://peps.python.org/pep-0008/)

- 각 회사, 프로젝트마다 따로 스타일 가이드를 설정하기도 함
  
  - [Google Style guide](https://google.github.io/styleguide/pyguide.html)

- Space Sensitive
  
  - 문장을 구분할 때, 중괄호({ }) 대신 들여쓰기(indentation)를 사용
  - 들여쓰기를 할 때는 4칸(space키 4번) 혹은 1탬(Tab키 1번)을 입력
    - 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용 → 혼용 금지
  - Tab으로 들여쓰면 계속 탭으로 들여써야 함
  - 원칙적으로는 공백(빈칸, space)사용을 권장 PEP8
    
    

# 조건문

## 조건문 기본

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
  
  

> **기본 형식**

- 조건에는 참/거짓에 대한 조건식
  
  - 조건이 참인 경우 이후 들여쓰기가 되어있는 코드 블록을 실행
  - 이외의 경우 else 이후 들여쓰기가 되어있는 코드 블록을 실행
    - else는 선택적으로 활용할 수 있음
  
  ```python
  if 조건 == True:
      # Run this Code block(True)
  else :
      # Run this Code block(False)
  ```

## 

## 복수 조건문

- 복수의 조건식을 활용한 경우 elif를 활용하여 표현함

```python
if 조건 :
    # Code block
elif 조건 :
    # Code block
elif 조건 :
    # Code block
else :
    # Code block
```

## 

## 중첩 조건문

- 조건문은 다른 조건문에 주업되어 사용될 수 있음
  - 들여쓰기에 유의하여 작성할 것

```python
if 조건 :
    # Code block
        if 조건 :
            # Code block
else :
    # Code block
```

## 

## 조건 표현식(Conditional Expression)

- 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용
- 삼항 연산자(Ternary Operator)로 부르기도 함

```python
True인 경우 값 if 조건 else False인 경우 값
```

# 

# 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
  
  

> 반복문의 종류

1. **while 문**
   
   - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
   - 회수 모르고 특정한 조건을 알고 있을 때

2. **for 문**
   
   - 반복가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음)
   - 반복 횟수 안다
- **반복 제어**
  - break, continue, for-else

## 

## while문

- while 문은 조건식이 참인 경우 반복적으로 코드를 실행
  
  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
  - while문은 무한 루프를하지 않도록 종료 조건이 반드시 필요
  
  ```python
  while 조건 :
      # Code block
  ```



> **복합연산자(In-Place Operator)**

- 복합 연산자는 연산과 할당을 합쳐 놓은 것
  - 예시) 반복문을 통해서 개수를 카운터 하는 경우

```python
a = 0
while a < 5 :   -> 종료 조건
    print(a)
    a += 1      -> 반복시 a가 계속 증가
print('끝')
```

## 

## for 문

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회
  
  - 처음부터 끝까지 모두 순회하므로 별도의 졸료 조건이 필요하지 않음

- iterable
  
  - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
  - 순회형 함수(range, enumerate)
  
  ```python
  for 변수명 in iterable :
      # Code block
  ```



> **딕셔너리(Dictionary) 순회**

- 추가 메서드를 활용하여 순회할 수 있음
  - keys() : Key로 구성된 결과
  - values() : value로 구성된 결과
  - items() : (key,value)의 튜플로 구성된 결과



> **enumerate 순회**

- enumerate()
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['민수', '영희', '철수']
for idx, number in enumerate(members):
    print(idx, number)

'''
0 민수
1 영희
2 철수
'''
```



> **List Comprehension**

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

```python
[code for 변수 in iterable]
[code for 변수 in iterable if 조건식]
```

- 예시
  
  ```python
  # 1~3의 세제곱 리스트 만들기
  cubic_list = [number ** 3 for number in range(1, 4)]
  print(cubic_list)
  ```



> **Dictionary Comprehension**

- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

```python
{key:value for 변수 in iterable}
{key:value for 변수 in iterable if 조건식}
```

- 예시
  
  ```python
  # 1~3의 세제곱 딕셔너리 만들기
  cubic_dict = {number : number ** 3 for number in range(1,4)}
  print(cubic_dict)
  ```

## 

## 반복문 제어

> **break**

- 반복문을 종료

- 예시
  
  ```python
  for i in range(10) :
      if i > 1 :
          print('0과 1만 필요해!')
          break
      print(i)
  '''
  0
  1
  0과 1만 필요해!
  '''
  ```



> **continue**

- continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

- 예시
  
  ```python
  for i in range(6) :
      if i % 2 == 0 :
          continue
      print(i)
  '''
  1
  3
  5
  '''
  ```



> **for-else**

- 끝까지 반복문을 실행한 이후에 else 문 실행

- **break를 통해 중간에 종료되는 경우 else문은 실행되지 않음**

- 예시
  
  ```python
  for char in 'apple' :
      if char == 'b':
          print('b!')
          break
  else :
      print('b가 없습니다')
  # b가 없습니다
  ```
  
  ```python
  for char in 'banana' :
      if char == 'b'
          print('b!')
          break
  else :
      print('b가 없습니다')
  # b!
  ```

> 
> 
> **pass**

- 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)
- 반복문 아니어도 사용가능
- 예시
