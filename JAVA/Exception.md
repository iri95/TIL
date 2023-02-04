# 예외의 처리

> **에러와 예외**

- 어떤 원인에 의해 오작동 하거나 비정상적으로 종료되는 경우
- 심각도에 따른 분류
  - Error
    - 메모리 부족, stack overflow와 같이 일단 발생하면 복구할 수 없는 상황
    - 프로그램의 비 정상적 종료를 막을 수 없음 → 디버깅 필요
  - Exception
    - 읽으려는 파일이 없거나 네트워크 연결이 안 되는 등 수습될 수 있는 비교적 상태가 약한 것들
    - **프로그램 코드에 의해 수습될 수 있는 상황**
  - exception handling(예외 처리)란
    - 예외 발생 시 프로그램의 비 정상 종료를 막고 정상적인 실행 상태를 유지하는 것
      - 예외의 감지 및 예외 발생 시 동작할 코드 작성 필요

<br>

> **예외 클래스의 계층**

- checked exception
  - 예외에 대한 대처 코드가 없으면 컴파일이 진행되지 않음
- unchecked exception (RuntimeException의 하위 클래스)
  - 예외에 대한 대처 코드가 없더라도 컴파일은 진행됨

<br>

> **try ~ catch 구문**

```java
try {
    // 예외가 발생할 수 있는 코드
} catch(XXException e) { // 던진 예외를 받음
    // 예외가 발생했을 때 처리할 코드
}
```

<br>

> **Exception 객체의 정보 활용**

- Throwable 의 주요 메서드

| 메서드                           | 설명                                                     |
| ----------------------------- | ------------------------------------------------------ |
| public String getMessage()    | 발생된 예외에 대한 구체적인 메시지를 반환한다                              |
| public Throwable getCause()   | 예외의 원인이 되는 Throwable 객체 또는 null을 반환한다                  |
| public void printStackTrace() | 예외가 발생된 메서드가 호출되기까지 메서드 호출 스택을 출력한다.디버깅의 수단으로 주로 사용된다. |

<br>

> **try-catch 문에서의 흐름**

- try 블록에서 예외가 발생하면
  - JVM이 해당 Exception 클래스의 객체 생성 후 던짐(throw)
    - throw new XXException()
  - 던져진 exception 을 처리할 수 있는 catch 블록에서 받은 후 처리
    - 적당한 catch 블록을 만나지 못하면 예외처리는 실패
  - 정상적으로 처리되면 try-catch 블록을 벗어나 다음 문장 진행
- try 블록에서 어떤한 예외도 발생하지 않은 경우
  - catch문을 거치지 않고 try-catch 블록의 다음 흐름 문장을 실행

<br>

> **다중 exception handling**

- try 블록에서 여러 종류의 예외가 발생할 경우
  - 하나의 try 블록에 여러 개의 catch 블록 추가 가능
    - 예외 종류별로 catch 블록 구성
- 다중 catch 문장 작성 순서 유의 사항
  - JVM이 던진 예외는 catch문장을 찾을 때는 다형성이 적용됨
  - 상위 타입의 예외가 먼저 선언되는 경우 뒤에 등장하는 catch 블록은 동작할 기회가 없음
    - unreachable catch block for Exception
  - 상속 관계가 없는 경우는 무관
  - 상속 관계에서는 작은 범위(자식)에서 큰 범위(조상)순으로 정의

<br>

> **다중 예외 처리를 이용한 checked Exception 처리**

- 예외 처리는 가능한 구체적으로 진행
- 처리하지 않으면 컴파일 불가 : Checked Exception
- 발생하는 예외들을 하나로 처리하기 : catch 문에 Exception을 넣으면 예외 모두 처리 가능
  - 예외 상황별 처리가 쉽지 않음
  - 가급적 예외 상황 별로 처리하는 것을 권장
- 심각하지 않은 예외를 굳이 세분화 해서 처리하는 것도 낭비
  - ‘|’를 이용해 하나의 catch 구문에서 상속관계가 없는 여러 개의 exception 처리
- 계층을 이루도록 예외의 처리를 함( 범위가 작은 것 부터)

<br>

> **try ~ catch ~ finally 구문을 이용한 예외 처리**

- finally는 예외 발생 여부와 상관 없이 언제나 실행
  - 중간에 return을 만나는 경우도 finally 블록을 먼저 수행 후 리턴 실행
  - 주요목적 : try 블록에서 사용한 리소스 반납
  - 생성한 시스템 자원을 반납하지 않으면 장래 resource leak 발생 가능 → close 처리
- finally에서 close를 통한 자원 반납
- 지저분할 수 밖에 없는 finally 블록
  - close 메서드 자체가 IOException 유발 가능
  - FileinputStream생성자에서 IOException 발생 시 fileInput은 null인 상태

<br>

> **try ~ with ~ resources**

- JDK1.7 이상에서 리소스의 자동 close 처리
- try 선언문에 선언된 객체들에 대해 자동 close 호출(finally 역할)
  - 단 해당 객체들이 AutoCloseable interface를 구현할 것
    - 각종 I/O stream, socket, connection
  - 해당 객체는 try 블록에서 다시 할당될 수 없음

<br>

> **throws 키워드를 향한 처리 위임**

- method에서 처리해야 할 하나 이상의 예외를 호출한 곳으로 전달(처리 위임)
  - 예외가 없어지는 것이 아니라 단순히 전달됨
  - 예외를 전달받은 메서드는 다시 예외 처리의 책임 발생
  - 처리하려는 예외의 조상 타입으로 throws 처리 가능

<br>

> **checked exception과 throws**

- checked exception은 반드시 try~catch 또는 throws 필요
- 필요한 곳에서 try~ catch 처리

<br>

> **runtime exception 과 thrwos**

- runtime exception은 throws 하지 않아도 전달되지만 결국은 try~catch로 처리해야 함.

<br>

> **로그 분석과 예외의 추적**

- Throwable의 printStackTrace는 메서드 호출 스택 정보 조회 가능
  - 최초 호출 메서드에서부터 예외 발생 메서드 까지의 스택 정보 출력
- 꼭 확인해야할 정보
  - 예외 종류
  - 예외 원인
  - 디버깅 출발점
    - 직접 작성한 코드를 디버깅 대상으로 삼을 것
    - 참조하는 라이브러리는 과감히 건너뛰기

<br>

> **메서드 재정의와 throws**

- 메서드 재정의 시 조상 클래스 메서드가 던지는 예외보다 부모예외를 던질 수 없다.
  - 부모가 치지 않은 사고를 자식이 칠 수 없다

<br>

> **사용자 정의 예외**

- API에 정의된 exception이외에 필요에 따라 사용자 정의 예외 클래스 작성
- 대부분 Exception 또는 RuntimeException 클래스를 상속받아 작성
  - checked exception 활용 : 명시적 예외 처리 또는 throws 필요
    - 코드는 복잡해지지만 처리 누락 등 오류 발생 가능성은 줄어듦
  - runtime exception 활용 : 묵시적 예외 처리 가능
    - 코드가 간결해지지만 예외 처리 누락 가능성 발생
- 사용자 정의 예외를 만들어 처리하는 장점
  - 객체의 활용 - 필요한 추가정보, 기능 활용 가능
  - 코드의 재사용 - 동일한 상황에서 예외 객체 재사용 가능
  - throws 메커니즘의 이용 - 중간 호출 단계에서 return 불필
