# 인터페이스

> **인터페이스란?**

- 서로 다른 두 시스템, 장치, 소프트웨어 따위를 서로 이어주는 부분, 또는 그런 접속 장치
- GUI - Graphic User Interface
  - 프로그램과 사용자 사이의 접점

<br>

> **인터페이스 작성**

- 최고 수준의 추상화 단계 : 일반 메서드는 모두 abstract 형태
  - JDK 8에서 default method와 static method 추가
- 형태
  - 클래스와 유사하게 interface 선언
  - 멤버 구성
    - 모든 멤버변수는 public static final이며 생략 가능
    - 모든 메서드는 public abstract이며 생략 가능

<br>

> **인터페이스 상속**

- 클래스와 마찬가지로 인터페이스도 extends를 이용해 상속이 가능
- 클래스와 다른 점은 인터페이스는 다중 상속이 가능
  - 헷갈릴 메서드 구현 자체가 없다.

<br>

> **인터페이스 구현과 객체 참조**

- 클래스에서 implements 키워드를 사용해서 interface 구현
- implements한 클래스는
  - 모든 abstract메서드를 override해서구현하거나
  - 구현하지않을 경우 abstract 클래스로 표시해야 함
- 여러 개의 interface implements가능
- 다형성은 조상 클래스 뿐 아니라 조상 인터페이스에도적용

<br>

> **인터페이스의 필요성**

- 구현의 강제로 표준화 처리
  - abstract 메서드 사용
- 인터페이스를 통한 간접적인 클래스 사용으로 손쉬운 모듈 교체 지원
- 서로 상속의 관계가 없는 클래스들에게 인터페이스를 통한 관계 부여로 다형성 확장
- 모듈 간 독립적으로 프로그래밍 가능 → 개발 기간 단축
- 구현의 강제로 표준화 처리 → 손쉬운 모듈 교체 지원
- 서로 상속의 관계가 없는 클래스들에게 인터페이스를 통한 관계 부여로 다형성 확장
- 독립적인 프로그래밍으로 개발 기간 단축

<br>

> **default method**

- 인터페이스에 선언 된 구현부가 있는 일반 메서드
  - 메서드 선언부에 default modifier 추가 후 메서드 구현부 작성
    - 접근 제한자는 public으로 한정됨(생략 가능)
  - 필요성
    - 기존에 interface 기반으로 동작하는 라이브러리의 interface에 추가해야 하는 기능이 발생
    - 기존 방식으로라면 모든 구현체들이 추가되는 메서드를 override 해야 함
    - default 메서드는 abstract가 아니므로 반드시 구현해야 할 필요는 없어짐
- default method의 충돌
  - JDK 1.7이하의 java에서는 interface method에 구현부가 없으므로 충돌이 없었음
  - 1.8부터 default method가생기면서 동일한 이름을 갖는 구현부가 있는 메서드가 충돌
  - method 우선 순위
    - super class의 method 우선 : super class가 구체적인 메서드를 갖는 경우 default method는 무시됨
    - interface간의 충돌 : 하나의 interface에서default method를 제공하고 다른 interface에서도 같은 이름의 메서드(default 유무와 무관)가 있을 때 sub class는 반드시 override해서 충돌 해결

<br>

> **static method**

- interface에 선언된 static method
  - 일반 static 메서드와 마찬가지로 별도의 객체가 필요 없음
  - 구현체 클래스 없이 바로 인터페이스 이름으로 메서드에 접근해서 사용 가능

<br>

### **Generics**

- 다양한 타입의 객체를다루는 메서드, 컬렉션 클래스에서 컴파일 시에 타입 체크
  - 미리 사용할 타입을명시해서 형 변환을 하지 않아도 되게 함
    - 객체의 타입에 대한 안정성 향상 및 형 변환을 번거로움 감소

<br>

> **표현**

- 클래스 또는 인터페이스 선언 시 <>에 타입 파라미터 표시
  - Class_Name : Raw Type
  - Class_name<T> : Generic Type
- 타입 파라미터
  - 특별한 의미의 알파벳 보다는 단순히 임의의 참조형 타입을 말함
  - T : reference Type, E : Element, K : Key, V : Value
- 객체 생성
  - 변수 쪽과 생성 쪽의 타입은 반드시 같아야 함

<br>

> **사용**

- 컴파일 타입에 타입 파라미터들이 대입된 타입으로 대체 됨

<br>

> **type parameter의 제한**

- 필요에 따라 구체적인 타입 제한 필요
  - 계산기 프로그램 구현 시 Number 이하의 타입 (Byte, Short, Integer…)로만 제한
    - type parameter 선언 뒤 extends 와 함께 상위 타입 명시
  - 인터페이스로 제한할 경우도 extends 사용
  - 클래스와 함께 인터페이스 제약 조건을 이용할 경우 &로 연결

<br>

> Generic Type 객체를 할당 받을 때 와일드 카드 이용

- generic type에서 구체적인 타입 대신 사용
  
  | 표현                        | 설명                      |
  | ------------------------- | ----------------------- |
  | Generic type<?>           | 타입에 제한이 없음(Object)      |
  | Generic type<? extends T> | T 또는 T를 상속받은 타입들만 사용 가능 |
  | Generic type<? super T>   | T 또는 T의 조상 타입만 사용 가능    |

<br>

> **Generic Method**

- 파라미터와 리턴타입으로 type parameter를 갖는 메서드
  - 메서드 리턴 타입 앞에 타입 파라미터 변수 선언
  - [제한자] <타입_파라미터, […]> 리턴_타입 메서드_이름(파라미터){}
