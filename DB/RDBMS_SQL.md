# MySQL

# RDBMS & SQL

### **RDBMS**

- 관계형(Relational) 데이터베이스 시스템

- 테이블 기반(Table based)의 DBMS.
  
  - 데이터를 테이블 단위로 관리.
    
    - 하나의 테이블은 여러 개의 컬럼(Column)으로 구성
  
  - 중복 데이터를 최소화 시킴
    
    - 같은 데이터가 여러 컬럼 또는 테이블에 존재 했을 경우, 데이터를 수정 시 문제가 발생할 가능성이 높아짐 - 정규화
  
  - 여러 테이블에 분산되어 있는 데이터를 검색 시 테이블 간의 관계(join)을 이용하여 필요한 데이터를 검색
    
    <br>

### **SQL (Structured Query Language)**

- Database에 있는 정보를 사용할 수 있도록 지원하는 언어
- 모든 DBMS에서 사용 가능
- Query의 대소문자는 구분하지 않음(단, 데이터의 대소문자는 구분)
  - MySQL은 데이터도 대소문자 구분하지 않음(default 설정) :: binary 함수 이용.
    
    <br>

> **DDL (Data Definition Language) : 데이터 정의어**

- 데이터베이스 객체(table, view, Index, …)의 구조를 정의.

- 테이블 생성, 컬럼 추가, 타입변경, 제약조건 지정, 수정 등
  
  | SQL문   | 설명                     |
  | ------ | ---------------------- |
  | create | 데이터베이스 객체를 생성          |
  | drop   | 데이터베이스 객체를 삭제          |
  | after  | 기존에 존재하는 데이터베이스 객체를 수정 |

- **예시**
  
  > **데이터베이스 생성**
  
  ```sql
  create database 데이터베이스명;
  create database 데이터베이스명
  default character set 값
  collate 값;
  ```
  
  - Character set은 각 문자가 컴퓨터에 저장될 때 어떠한 ‘코드’로 저장 될지에 대한 규칙의 집합을 의미한다.
  - Collation은 특정 문자 셋에 의해 데이터베이스에 저장된 값들을 비교 검색하거나 정렬 등의 작업을 위해 문자들을 서로 ‘비교’ 할 때 사용하는 규칙들의 집합을 의미한다.
    
    <br>
  
  > **데이터베이스 변경**
  
  ```sql
  alter database 데이터베이스명
  default character set 값 collate 값;
  ```
  
  <br>
  
  > **데이터베이스 삭제**
  
  ```sql
  drop database 데이터베이스명;
  ```
  
  <br>
  
  > **데이터베이스 사용**
  
  ```sql
  use 데이터베이스명;
  ```

<br>

> **데이터베이스 생성**

```sql
create database 데이터베이스명;
create database 데이터베이스명
default character set 값
collate 값;
```

- Character set은 각 문자가 컴퓨터에 저장될 때 어떠한 ‘코드’로 저장 될지에 대한 규칙의 집합을 의미한다.

- Collation은 특정 문자 셋에 의해 데이터베이스에 저장된 값들을 비교 검색하거나 정렬 등의 작업을 위해 문자들을 서로 ‘비교’ 할 때 사용하는 규칙들의 집합을 의미한다.

- 예시
  
  > **SELECT, FROM**
  
  ```sql
  SELECT *|{[ALL|DISTINCT] column | expression [alias],...}
  FROM table name;
  ```
  
  - SELECT clause와 FROM clause은 필수
  
  | select clause | description                                  |
  | ------------- | -------------------------------------------- |
  | *             | FROM 절에 나열된 테이블에서 모든 열을 선택                   |
  | ALL           | 선택된 모든 행을 반환. ALL이 default(생략 가능)            |
  | DISTINCT      | 선택된 모든 행 중에서 중복 행 제거                         |
  | column        | FROM절에 나열된 테이블에서 지정된 열을 선택                   |
  | expression    | 표현식은 값으로 인식되는 하나 이상의 값, 연산자 및 SQL 함수의 조합을 뜻함 |
  | alias         | 별칭.                                          |
  
  <br>
  
  > **WHERE**
  
  ```sql
  SELECT *|{[ALL|DISTINCT] column | expression [alias],...}
  FROM table name
  WHERE conditions;
  ```
  
  - WHERE clause : 조건에 만족하는 행을 검색
    
    <br>
  
  > **ORDER BY**
  
  ```sql
  SELECT *|{[ALL|DISTINCT] column | expression [alias],...}
  FROM table name
  WHERE conditions
  ORDER BY col_name1[ASC|DESC][,dol_name2,...];
  ```
  
  - ORDER by clause : 정렬(default : ASC)

<br>

> **데이터베이스 변경**

```sql
alter database 데이터베이스명
default character set 값 collate 값;
```

<br>

> **데이터베이스 삭제**

```sql
drop database 데이터베이스명;
```

<br>

> **데이터베이스 사용**

```sql
use 데이터베이스명;
```

<br>

> **DML(Data Manipulation Language) : 데이터 조작어**

- Data 조작 가능

- 테이블의 레코드를 CRUD(Create, Retrieve, Update, Delete)
  
  | SQL문      | 설명                  |
  | --------- | ------------------- |
  | insert(C) | 데이터베이스 객체에 데이터를 입력  |
  | select(R) | 데이터베이스 객체에서 데이터를 조회 |
  | update(U) | 데이터베이스 객체에 데이터를 수정  |
  | delete    | 데이터베이스 객체에 데이터를 삭제  |

<br>

> **DCL (Data Control Language) : 데이터 제어어**

- DB, Table의 접근권한이나 CRUD 권한을 정의

- 특정 사용자에게 테이블의 검색권한 부여/금지 등
  
  | SQL문   | 설명                |
  | ------ | ----------------- |
  | grant  | 데이터베이스 객체에 권한을 부여 |
  | revoke | 데이터베이스 객체 권한 취소   |

<br>

> **TCL (Transaction Control Language) : 트렌섹션 제어어**

- transaction란 데이터베이스의 논리적 연산 단위
