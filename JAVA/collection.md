# Collection

> **자료구조**

- 자료구조(data structure)는 컴퓨터 과학에서 효율적인 접근 및 수정을 가능케 하는 자료의 조직, 관리, 저장을 의미한다. 더 정확히 말해, 자료구조는 데이터 값의 모임, 또 데이터 간의 관계, 그리고 데이터에 적용할 수 있는 함수나 명령을 의미한다.

<br>

> **배열**

- 가장 기본적인 자료 구조
- homogeneous collection : 동일한 데이터 타입만 관리 가능
  - 타입이 다른 객체를 관리하기 위해서는 매번 다른 배열 필요
- Polymorphism
  - Object를 이요하면 모든 객체 참조 가능 → Collection Framework
  - 담을 때는 편리하지만 빼낼 때는 Object로만 가져올 수 있음
  - 런타임에 실제 객체의 타입 확인 후 사용해야 하는 번거로움
- Generic을 이용한 타입 한정
  - 컴파일 타임에 저장하려는 타입 제한 → 형변환의 번거로움 제거

<br>

> **Collection Framework**

- java.util 패키지
  - 다수의 데이터를 쉽게 처리하는 방법 제공 → DB 처럼 CRUD 기능 중요
- collection framework 핵심 interface

| interface              | 특징                                                            |
| ---------------------- | ------------------------------------------------------------- |
| List                   | 순서가 있는 데이터의 집합. 순서가 있으니까 데이터의 중복을 허락                          |
| ex) 일렬로 줄 세우기          |                                                               |
| ArrayList, LinkedList  |                                                               |
| Set                    | 순서를 유지하지 않는 데이터의 집합. 순서가 없어서 같은 데이터를 구별할 수 없음 → 중복 허락하지 않음    |
| ex) 알파벳이 한 종류 씩 있는 주머니 |                                                               |
| HashSet, TreeSet…      |                                                               |
| Map                    | key와 value의 쌍으로 데이터를 관리하는 집합. 순서는 없고 key의 중복 불가, value는 중복 가능 |
| ex) 속성 - 값, 지역번호 - 지역  |                                                               |
| HashMap, TreeMap       |                                                               |

| 분류                                 | Collection          |
| ---------------------------------- | ------------------- |
| 추가                                 | add(E e),           |
| addAll(Collection<? extends E > c) |                     |
| 조회                                 | contains(Object o), |
| containsAll(Collection<?> c),      |                     |
| equals(),                          |                     |
| isEmpty(),                         |                     |
| iterator(),                        |                     |
| size(),                            |                     |
| 삭제                                 | clear(),            |
| removeAll(Collection<?> c),        |                     |
| retainAll(Collection<?> c),        |                     |
| 수정                                 |                     |
| 기타                                 | toArray()           |

<br>

### List 계열

> **특징**

- 순서가 있는 데이터의 집합
- 순서가 있으므로 데이터의 중복을 허락

<br>

> **주요 메서드**

| 분류                                          | Collection                | List                               |
| ------------------------------------------- | ------------------------- | ---------------------------------- |
| 추가                                          | add(E e),                 |                                    |
| addAll(Collection<? extends E > c)          | add(int index, E element) |                                    |
| addAll(int index, Collection<? extends E> c |                           |                                    |
| 조회                                          | contains(Object o),       |                                    |
| containsAll(Collection<?> c),               |                           |                                    |
| equals(),                                   |                           |                                    |
| isEmpty(),                                  |                           |                                    |
| iterator(),                                 |                           |                                    |
| size(),                                     | get(int index),           |                                    |
| indexOf(Object o),                          |                           |                                    |
| lastIndexOf(Object o),                      |                           |                                    |
| listIterator(),                             |                           |                                    |
| 삭제                                          | clear(),                  |                                    |
| removeAll(Collection<?> c),                 |                           |                                    |
| retainAll(Collection<?> c),                 | remove(int index)         |                                    |
| 수정                                          |                           | set(int index, E element)          |
| 기타                                          | toArray()                 | subList(int formIndex, int toIndex |

<br>

> **배열과 ArrayList**

- 배열의 장점
  - 가장 기본적인 형태의 자료 구조로 간단하며 사용이 쉬움
  - 접근 속도가 빠름
- 배열의 단점
  - 크기를 변경할 수 없어 추가 데이터를 위해 새로운 배열을 만들고 복사해야 함
  - 비 순차적 데이터의 추가, 삭제에 많은 시간이 걸림
- 배열을 사용하는 ArrayList도 태생적으로 배열의 장-단점을 그대로 가져

<br>

> **LinkedList**

- 각 요소를 Node로 정의하고 Node는 다음 요소의 참조 값과 데이터로 구성됨
  - 각 요소가 다음 요소의 링크 정보를 가지며 연속적으로 구성될 필요가 없다.
- 데이터 삭제 및 추가

<br>

> **LinkedList와 ArrayList의 용도**



| 구분 | 순차 추가/수정/삭제 시
100만건 추가 시 | 비 순차 추가/수정/삭제
10만건 추가 시 | 조회
10만건 조회 시 |
| --- | --- | --- | --- |
| ArrayList | 빠름 | 느림 | 빠름 |
| LinkedList | 느림 | 빠름 | 느림 |

- 결론
  - 특정 클래스가 좋고 나쁨이 아니라 용도에 적합하게 사용해야 함
  - 소량의 데이터를 가지고 사용할 경우는 큰 차이가 없음
  - 정적인 데이터 활용, 단순한 데이터 조회용 : ArrayList
  - 동적인 데이터 추가, 삭제가 많은 작업 : LinkedList

<br>

> **자료 삭제 시 주의 사항**

- index를 이용한 for문
  - 요소가 삭제되면 size가 줄어들기 때문에 index 차감 필요
  - 거꾸로 접근하면 자연스럽게 해결
- forEach 문장은 Collection 크기가 불변해야 함!

<br>

### Set

> **Set interface**

- 순서 없이 주머니에 구슬(데이터)를 넣는 형태
- 순서가 없으므로 데이터를 구별할 index가 없어 중복이 허용되지 않는다.
  - 효율적인 중복 데이터 제거 수단

<br>

### Map

> **Map interface**

- 특징
  - Key와 Value를 하나의 Entry로 묶어서 데이터 관리
    - key : Object 형태로 데이터 중복을 허락하지 않음
    - Value : Object 형태로 데이터 중복이 허락 됨.

| 분류                                       | Map<K, V>               |
| ---------------------------------------- | ----------------------- |
| 추가                                       | put(K key, V value)     |
| putAll(Map<? extends K, ? extends V> m)  |                         |
| 조회                                       | containsKey(Object key) |
| containsValue(Object value)              |                         |
| entrySet()                               |                         |
| keySet()                                 |                         |
| get(Object key)                          |                         |
| values()                                 |                         |
| size()                                   |                         |
| isEmpty()                                |                         |
| 삭제                                       | clear()                 |
| remove(Object key)                       |                         |
| 수정                                       | put(K key, V value)     |
| putAll(Map<? extends K, ? extends V > m) |                         |

### <br>

### 정렬

> **정렬**

- 요소를 특정 기준에 대한 내림차순 또는 오름차순으로 배치하는 것
- 순서를 가지는 Collection들만 정렬 가능
  - List 계열
  - Set에서는 SortedSet의 자식 객체
  - Map에서는 sortedMap의 자식 객체(key 기준)
- Collections의 sort()를 이용한 정렬
  - sort(List<T> list)
    - 객체가 Comparable을 구현하고 있는 경우 내장 알고리즘을 통해 정렬

<br>

> **Comparator 활용**

- 객체가 Comparable을 구현하고 있지 않거나 사용자 정의 알고리즘으로 정렬하려는 경우
  - String을 알파벳 순이 아닌 글자 수 별로 정렬하려면?
- sort(List<T> list, Comparator<? Super T> c)
- 1회성 객체 사용 시 anonymous inner class 사용
  - 클래스 정의, 객체 생성을 한번에 처리
  - 람다 표현식 이용
