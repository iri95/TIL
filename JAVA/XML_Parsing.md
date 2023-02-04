# XML Parsing

### 공공데이터 소개

> **공공데이터란?**

- 공공기관이 만들어내는 모든 공적인 정보
- 각 공공기관이 보유한 데이터를 개방하여 누구나 원하는 기능에 활용 가능
- [www.data.go.kr](http://www.data.go.kr) 등 회원가입 후 키를 발급받아 사

<br>

> **데이터의 형태**

- CSV
  - comma separated value
  - 용량이 작지만 구조적이지 못함
- xml
  - 태그를 통해 데이터 형식 정의
  - 구조적, 정확한 문법이 필요, 큰 용량
- json
  - JSON(JavaScript Object Notation)을 통해 데이터 형식 정의
  - 구조를 가지며 객체로 다른 언어와 호환

<br>

> **XML**

- Markup Language
  - 태그 등을 이용하여 문서나 데이터의 구조를 명기하는 언어
  - HTML, SGML
- XML
  - Extensible Markup Language
- HTML과 달리
  - 필요에 따라서 태그를 확장해서 사용 가능
  - 정확한 문법을 지켜야 동작 : Well formed

<br>

> **기본 문법**

- 문서의 시작은 <?xml version=”1.0” encoding = “UTF-8”?>로 한다.
- 반드시 rootelement가 존재해야 한다.
  - 나머지 태그들은 Tree 형태로 구성된다.
- 시작 태그와 종료 태그는 일치해야 한다.
- 시작 태그는 key-value 구조의 속성을 가질 수 있다.
  - 속성 값은 “ ”또는 ‘ ‘로 묶어서 표현한다
- 태그는 대소문자를 구별한다.

<br>

> **valid**

- xml 태그는 자유롭게 생성하기 때문에 최초 작성자의 의도대로 작성되는지 확인할 필요
  
  - 문서의 구조와 적절한 요소, 속성들의 개수, 순서들이 잘 지켜졌는가?
  - DTD 또는 Schema를 이용해서 문서의 규칙 작성
  
  |           | DTD                         | 스키마                                |
  | --------- | --------------------------- | ---------------------------------- |
  | 문법        | XML과 유사한 문법                 | XMl 1.0표준에 만족                      |
  | DOM 지원    | DOM 기술을 지원하지 않음             | DOM을 통한 조작 가능                      |
  | 컨텐츠 모델    | 순차, 선택 리스트만 제공              | 순차, 리스트 복합적으로 사용 가능                |
  | 데이터 타입    | 문자열, 토큰, ID와 그 외에 한정된 타입 지원 | 문자열, 숫자, 날짜/시간 및 새로운 형식 정의를 할 수 있음 |
  | Namespace | 전역 이름만 사용                   | 전역/로컬 이름 모두 사용 가능                  |
  | 상속성       | 제공하지 않음                     | 제공                                 |
  | 확장성       | 한계가 있음                      | 제한 없음                              |
  | 기본 제약 조건  | 있음                          | 없음                                 |
  | 동적 스키마    | 불가능-읽기만 가능                  | 가능 - 런타임에 상호작용으로 변경 가능             |

- DTD, Schema를 잘 따른 문서를 valid하다 라고 함

<br>

### 문서의 Parsing - SAX(Simple API for XML)

> **파싱**

- 문서에서 필요한 정보를 얻기 위해 태그를 구별하고 내용을 추출하는 과정
  - 전문적인 parser 활용
- SAX parsar
  - Simple API for XML parsar
  - 문서를 읽으면서 태그의 시작, 종료 등 이벤트 기반으로 처리하는 방식
- DOM parser
  - Document Object Model
  - 문서를 다 읽고 난 후 문서 구조 전체를 자료구조에 저장하여 탐색하는 방식
- SAX는 빠르고 한번에 처리하기 때문에 다양한 탐색이 어렵다.
- DOM은 다양한 탐색이 가능하지만 느리고 무거우며 큰 문설르 처리하기 어렵다.

<br>

> **동작 방식**

- 문서를 읽다가 발생하는 이벤트 기반으로 문서 처리

<br>

### 문서의 Parsing - DOM

> **동작 방식**

- 문서를 완전히 메모리에 로딩 후 필요한 내용 찾기

- DOM Tree
  - 문서를 구성하는 모든 요소를 Node(태그, 속성, 값)로 구성
  - 태그들은 root노드(주소록)을 시작으로 부모-자식의 관계 구성

<br>

> **유용한 API들**

- Node
- Element extends Node

<br>

### 문서의 Parsing - JSON(JavaScript Object Notation)

> **JSON**

- Javascript Object Notation(자바스크립트에서의 객체 표현법)
- 간결한 문법, 단순한 텍스트, 적은 용량으로 대부분의 언어, 대부분의 플랫폼에서 사용 가능
  - 이 기종 간의 데이터 교환에 광범위하게 사용됨
  - 객체를 key-value의 쌍으로 관리
- 다양한 라이브러리를 이용한 간편한 사용
  - jackson-databind, jackson-core, jackson-annotation

<br>

### Swing 활용

> **Swing**

- Java Application에서 사용되는 GUI(Graphic User Interface)를 제공하는 추상적으로 정의돈 도구(컴포넌트) 모음
- Container
  - 다른 컴포넌트들을 배치하기 위한 컴포넌트
  - Container는 다른 Container를 포함할 수 있고 나중에 복합적인 Layout을 구성할 수 있게 한다.
  - JFrame : 독립적으로 사용될 수 있으며 타이틀과 사이즈를 조절할 수 있는 버튼을 가짐
  - JPanel : 반드시 다른 Container에 포함되어야 하며 복합적인 레이아웃 구성에 사용
- 다른 Component
  - JButton
  - JLabel
  - JTextField
  - JTable
  - JList

<br>

> **Layout과 LayoutManager**

- Layout : Component들을 Container에 어떻게 배치할 것인가
- Layoutmanager : Container 별로 Component의 위치와 크기, 배치 방식을 결정하는 객체
- FlowLayout
  - JPanel의 기본 Layoutmanager
  - 요소를 가로로 물 흐르듯이 배치
- BorderLayout
  - JFrame의 기본 LayoutManager
  - 특별한 영역 즉, North, South, West, East, Center에 각각 컴포넌트를 배치한다.
    - Component들을 배칠할 때는 영역을 지정(BoarderLayout.CENTER or “Center”)
    - 사용하지 않는 공간은 크기가 0*0이 되고 Center가 기본이다
    - 각각의 영역에는 하나의 Component를 담을 수 있고 중복해서 담을 경우는 마지막에 담은 컴포넌트만 보인다.
    - 크기를 조절할 때 North와 South는 좌우로, East와 West는 상하로만 늘어난다. Center는 양방향
- Layout 설정
  - 생성자 또는 setLayout 메서드로 layout 변경 가능
- 복합적인 Layout 구성
  - Container 안에 또다른 Container를 배치하는 형태로 복합적인 Layout 구성

<br>

> **이벤트 처리 모델(Delegation Model)**

- 위임형 모델
- 실제로 이벤트가 일어난 것은 component이지만 거기서 처리되는 것이 아니라 이벤트 리스너를 등록시킨 후 위임 받은 handler 클래스 내에 이벤트 처리

<br>

> **이벤트 처리 클래스**

- XX Listener
  - 이벤트 처리에 대한 메서드들을 정의한 인터페이스로 handler는 이 인터페이스를 구현
  - 하나의 component에 여러 개의 event handle을 붙일 수 있다.
    - Implements ActionListener, WindowListener
- XXEventAdapter
  - Listener를 implements 할 경우 사용하지도 않는 이벤트 핸들러까지 다 구현해야 하는 단점
    - 필요한 메서드만 구현할 수 있다면?
  - -xxxEventAdapter implements XXListener
    - 해당 메서드들을 모조리 구현해 놓은 class. 구현 내용은 비어있는 {}
    - 상속받은 후 필요한 것만 override하면 된다
