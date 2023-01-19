# 23/01/19 함수의 활용

# 함수 응용

### **내장함수**

- 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음



> **map**

- **map(function, iterable)**

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환

- map 활용 사례
  
  - 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때
  
  ```python
  n,m = map(int, input().split())   # 3,5 입력
  print(n,m)   # 3, 5
  print(type(n), type(m))  # <class 'int'> <class'int'>
  ```

> **filter**

- **filter(function, iterable)**

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그결과가 True인 것들을 filter object로 반환

- 예시
  
  ```python
  def odd(n) :
      return n % 2
  numbers = [1, 2, 3]
  result = filter(odd, numbers)
  print(result, type(result)) # <filter object at 000000000000> <class 'filter'>
  print(list(result)  # [1, 3]
  ```

> **zip**

- **zip(*iterables)**

- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

- 예시
  
  ```python
  girls = ['jane', 'ashley']
  boys = ['justion', 'eric']
  pair = zip(girls, boys)
  print(pair, type(pair))  # <zip object at 0x0000000000> <class 'zip'>
  print(list(pair)) # [('jane', 'justion'),('ashley', 'eric')]
  ```

> **lambda 함수**

- **lambda [parameter] : 표현식**

- 람다함수
  
  - 표현식을 계산한 결괏값을 반환하는 함수로, 이름이 없는 함수여서 익명 함수라고도 불림

- 특징
  
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음

- 장점
  
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용 가능

- 예시
  
  ```python
  # 삼각형의 넓이를 구하는 공식 - def
  def triangle_area(b, h) :
      return 0.5 * b * h
  print(triangle_area(5, 6)  # 15.8
  
  # 삼각형의 넓이를 구하는 공식 - 람다
  triangle_area = lambda b, h : 0.5 * b * h
  print(triangle_area(5, 6)  # 15.8
  ```

> **재귀함수(recursive function)**

- 자기 자신을 호출하는 함수

- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  
  - 알고리즘 중 재귀함수로 로직을 표현하기 쉬운 경우가 있음 (예 - 점화식)
  - 변수의 사용이 줄어들며, 코드이 가독성이 높아짐

- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

- 예시
  
  - Factorial
  
  ```python
  # 재귀함수
  def factorial(n) :
      if n == 0 or n == 1 :
          return 1 
      else :
          return n * factorial(n-1)
  print(factorial(4))   # 24
  
  # 반복문
  def fact(n) :
      result = 1 
      while n > 1 :
          result *= n
          n -= 1
      return result
  print(fact(4)) # 24
  ```

<aside>
💡 재귀 함수 주의 사항

- 재귀 함수는 base case에 도달할 때까지 함수를 호출함
- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
- 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

</aside>

> **반복문과 재귀 함수 비교**

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함.
- 재귀 호출은 변수 사용을 줄여줄 수 있음
- 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림.

# 패킹/언패킹(Packing/Unpacking)
