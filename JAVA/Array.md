# 배열

> **동일한 타입의 변수를 여러 개 사용하면**

- 변수의 개수 증가
- 코드의 길이 증가
- 반복문 적용 불가
- 변수의 수가 동적으로 결정될 경우, 사용 불가

<br>

> **배열(Array)로 동일 타입 변수 묶어서 사용하기**

- 배열이란?
  - 동일한 타입의 데이터 0개 이상을 하나의 연속된 메모리 공간에서 관리하는 것
- 요소에 접근하는 속도가 매우 빠르다
- 한번 생성하면 크기 변경 불가

<br>

> **Array 만들기 1**

- **타입[] 변수명;**
  - int[] point;
- **타입 변수명[];**
  - string[] names;
- 변수의 타입과 저장하는 데이터의 타입?

```java
int a;
int[] arr;
```

- a : 기초 타입(primitive type)
- arr : 레퍼런스 타입(reference type)
- 기초 타입 외에는 전부 레퍼런스 타입

<br>

> **배열의 생성과 초기화**

- 생성
  
  - new keyword와 함께 저장하려는 데이터 타입 및 길이 지정 : new data type[length]
    - new int[3] : int타입의 자료 3개를 저장할 수 있는 배열을 메모리에 **생성**
    - points = new int[3] : 생성된 배열을 points라는 변수에 할당
    - points는 메모리에 있는 배열을 가리키는 reference 타입 변수

- 배열 요소의 초기화
  
  - 배열의 생성과 동시에 저장 대상 자료형에 대한 기본 값으로 defalut 초기화 진행
    
    | 자료형              | 기본값    | 비고           |
    | ---------------- | ------ | ------------ |
    | boolean          | false  |              |
    | char             | \u0000 | 공백문자         |
    | byte, short, int | 0      |              |
    | long             | 0L     |              |
    | float            | 0.0f   |              |
    | double           | 0.0    |              |
    | 참조형 변수           | null   | 아무것도 참조하지 않음 |

<br>

> **배열의 사용**

- 배열은 index 번호를 가지고 각 요소에 접근 가능
  - index 번호는 0부터 시작
  - 배열의 길이 : 배열이름.length 로 배열의 크기 조회 가능

<br>

> **Array 출력을 편리하게**

- for 문을 통한 출력 대신 Arrays.toString()

<br>

> **Array 만들기 2**

- 생성과 동시에 할당한 값으로 초기화
  - int[] b = new int[] {1, 3, 5, 6, 8}
  - int[] c = {1, 3, 5, 6, 8}
- 선언과 생성을 따로 처리할 경우 초기화 주의

```java
int[] points;
points ={1, 3, 5, 6, 8}; // 컴파일 오류

int [] points;
points = new int[] {1, 3, 5, 6, 8}; // 선언할 때는 배열의 크기를 알 수 없을 때
```

<br>

> **배열의 생성과 메모리 사용 과정**

- int[] points = new int[3]
- 배열 선언 int[] points
- 배열 생성 : new int[3];
  - 메모리에 연속된 공간 차지 → 크기 변경 불가
    - int 타입의 데이터 3개를 담을 수 있는 메모리 공간 확보
  - Type에 대한 default 초기화
- 참조 값 할당 : points = new int[3];
  - 배열의 주소를 변수에 할당하여 참조하게 함
- 요소값에 할당 :
  - points[0] = 1;
  - points[1] = ‘A’
  
  <br>

> for-each with Array

- 가독성이 개선된 반복문으로, 배열 및 Collection에서 사용
- index 대신 직접(element)에 접근하는 변수 제공
  - naturally read only (copied value)
- 사용

```java
int intArray[] = {1 ,3, 5, 7, 9};
for(int x : intArray) {
    System.out.println(x);
}
```

- index를 사용하지 않아도 되지만 사용할 수 없다 → 용도에 따라 사용

<br>

> **Array is Immutable**

- 배열은 최초 메모리 할당 이후, 변경할 수 없음.
- 개별 요소는 다른 값으로 변경이 가능하나, 요소를 추가하거나 삭제할 수는 없다.
- 배열의 참조 변수는 배열이 아닌 주소를 가지고 있는 것

```java
int[] nums = {1, 2, 3};
nums = new int[] {1, 2, 3, 4};
nums[1] = 100;
```

- 위에서 nums에 새로운 배열을 할당한 것이지 배열이 바뀐 것이 아니다

<br>

> **api 제공하는 배열 복사 method**

- System.arrayCopy
- Arrays.copyOf
