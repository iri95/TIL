# File/IO

### 노드 스트림

> **I/O와 Stram**

- I/O? 데이터의 입력(input)과 출력(output)
- 데이터는 한쪽에서 주고 한쪽에서 받는 구조로 되어있음
  - 이때 입력과 출력의 끝단 : 노드(Node)
  - 두 노드를 연결하고 데이터를 전송할 수 있는 개념 : 스트림(Stream)
    - 물의 흐름이나 전기의 흐름과 같은 개념
  - 스트림은 단 방향으로만 통신이 가능하며 하나의 스트림으로 입력과 출력을 같이 처리할 수 없다

<br>

> **Node Stream의 종류와 naming**

- Node stream : node에 연결되는 스트림



<br>

> **InputStram의 주요 메서드**

| 메서드 명   | 선언부와 설명                                                                                |
| ------- | -------------------------------------------------------------------------------------- |
| read()  | public abstract int read() throws IOException                                          |
|         | byte 하나를 읽어서 int로 변환한다. 더 이상 읽을 값이 없으면 -1을 리턴한다.                                       |
|         | public int read(byte b[]) throws IOException                                           |
|         | 데이터를 읽어서 b를 채우고 읽은 바이트의 개수를 리턴한다. 0이 리턴되면 더 이상 읽을 값이 없는 상황이다                           |
|         | public int read(byte b[], int offset, int len) throws IOException                      |
|         | 최대 len 만큼 데이터를 읽어서 b의 offset부터 b에 저장하고 읽은 바이트 개수를 리턴한다. 따라서 len+offset은 b의 크기 이하여야 한다. |
| close() | public void close() throws IOException                                                 |
|         | 종료해서 자원을 반납한다.                                                                         |

<br>

> **Reader의 주요 메서드**

| 메서드 명   | 선언부와 설명                                                                                       |
| ------- | --------------------------------------------------------------------------------------------- |
| read()  | public int read() throws IOException                                                          |
|         | char 하나를 읽어서 int로 반환한다. 더 이상 읽을 값이 없으면 -1을 리턴한다                                               |
|         | public int read(char cbuf[]) throws IOException                                               |
|         | 데이터를 읽어서 cbuf를 채우고 읽은 문자의 개수를 리턴한다. 0이 리턴 되면 더 이상 읽을 값이 없는 상황이다                               |
|         | abstract int read(char cbuf[], int off, int len) throws IOException                           |
|         | 최대 len 만큰 데이터를 읽어서 cbuf의 offset부터 cbuf에 저장하고 읽은 char 개수를 리턴한다. 따라서 len+off는 cbuf의 크기 이하여야 한다. |
|         | public int read(java.nio.CharBuffer target) throws IOException                                |
|         | 데이터를 읽어서 target에 저장한다. target은 cbuf를 대체한다                                                     |
| close() | public void close() throws IOException                                                        |
|         | 스트림을 종료해서 자원을 반납한다.                                                                           |

<br>

> **OutputStream**

| 메서드 명   | 선언부와 설명                                                          |
| ------- | ---------------------------------------------------------------- |
| write() | public abstract void write(int b) throws IOException             |
|         | b의 내용을 byte로 출력한다.                                               |
|         | public void write(byte b[]) throws IOException                   |
|         | b를 문자열로 변환해서 출력한다.                                               |
|         | public void write(byte b[], int off, int len) throws IOException |
|         | b의 off부터 off+len-1만큰을 문자열로 변환해서 출력한다.                            |
| close() | public void close() throws IOException                           |
|         | 스트림을 종료해서 자원을 반납한다. close()는 내부적으로 flush()를 호출한다.                |
| flush() | public void flush() throws IOException                           |
|         | 버퍼가 있는 스트림에서 버퍼의 내용을 출력하고 버퍼를 비운다.                               |

<br>

> **Writer**

| 메서드 명    | 선언부와 설명                                                                       |
| -------- | ----------------------------------------------------------------------------- |
| write()  | public void write(int c ) throws IOException                                  |
|          | b의 내용을 char로 출력한다.                                                            |
|          | public void write(char cbuf[]) throws IOException                             |
|          | cbuf를 문자열로 변환해서 출력한다.                                                         |
|          | public void write(char cbuf[], int off, int len ) throws IOException          |
|          | cbuf의 off부터 off+len-1만큼을 문자열로 변환해서 출력한다.                                      |
|          | public void write(String str) throws IOException                              |
|          | str을 출력한다.                                                                    |
|          | public void write(String str, int off, int len) throws IOException            |
|          | str의 off부터 off+len-1만큼을 출력한다.                                                 |
| append() | public Writer append(CharSequence csq) throws IOException                     |
|          | csq를 출력하고 Writer를 리턴한다.                                                       |
|          | public Writer append(CharSequence csq, int start, int end) throws IOException |
|          | csq의 start부터 end 까지를 출력하고 Writer를 리턴한다.                                       |
| close()  | public void close() throws IOException                                        |
|          | 스트림을 종료해서 자원을 반납한다. close()는 내부적으로 flush()를 호출한다.                             |
| flush()  | abstract public void flush() throws IOException                               |
|          | 버퍼가 있는 스트림에서 버퍼의 내용을 출력하고 버퍼를 비운다.                                            |

<br>

> **FIle**

- 가장 기본적인 입출력 장치 중 하나로 파일과 디렉터리를 다루는 클래스

| 메서드 명              | 선언부와 설명                                                         |
| ------------------ | --------------------------------------------------------------- |
| File()             | public File(String pathname)                                    |
|                    | pathname에 해당하는 파일을 생성한다. 경로 없이 파일을 생성하면 애플리케이션을 시작한 경로가 된다.     |
|                    | public File(String pathname, String child)                      |
|                    | parent 경로 아래 child를 생성한다.                                       |
|                    | public File(File pathname, String child)                        |
|                    | parent 경로 아래 child를 생성한다.                                       |
|                    | public File(URI uri)                                            |
|                    | file로 시작하는 URI 객체를 이용해 파일을 생성한다.                                |
| createNewFile()    | public boolean createNewFile() throws IOException               |
|                    | 새로운 물리적인 파일을 생성한다.                                              |
| mkdir()            | public boolean mkdir()                                          |
|                    | 새로운 디렉토리를 생성한다.                                                 |
| mkdirs()           | public boolean mkdirs()                                         |
|                    | 경로상에 없는 모든 디렉터리를 생성한다.                                          |
| delete()           | public boolean delete()                                         |
|                    | 파일 또는 디렉토리를 삭제한다.                                               |
| getName()          | public String getName()                                         |
|                    | 파일의 이름을 리턴한다                                                    |
| getPath()          | public String getPath()                                         |
|                    | 파일의 경로를 리턴한다.                                                   |
| getAbsolutePath()  | public String getAbsolutePath()                                 |
|                    | 파일의 절대 경로를 리턴한다.                                                |
| getCanonicalPath() | public String getCanonicalPath() throws IOException             |
|                    | 파일의 정식 경로를 리턴한다. 정식 경로는 절대 경로이며 경로 내에 . 또는 ..의 상대경로 기호가 없는 경로이다 |
| isDirectory()      | public boolean isDirectory()                                    |
|                    | 파일이 디렉토리인지 리턴한다                                                 |
| isFile()           | public boolean isFile()                                         |
|                    | 파일이 파일인지 리턴한다.                                                  |
| length()           | public long length()                                            |
|                    | 파일의 길이를 리턴한다                                                    |
| listFiles()        | public File[] listFiles()                                       |
|                    | 파일이 디렉토리인 경우 자식 파일들을 File[]형태로 리턴한다.                            |

<br>

> **FileInputStream, FileOutputStream**

| 메서드 명              | 선언부와 설명                                                                           |
| ------------------ | --------------------------------------------------------------------------------- |
| FileInputStream()  | public FileInputStream(String name) throws FileNotFoundException                  |
|                    | name 경로의 파일을 읽는 FileInputStream을 생성한다                                             |
| FileOutputStream() | public FileOutputStream(String name) throws FileNotFoundException                 |
|                    | name 경로의 파일에 출력하는 FileOutputStream을 생성한다.                                         |
|                    | public FileOutputStream(String name, boolean append) throws FileNotFoundException |
|                    | name 경로의 파일에 출력하는 FileOutputStream을 생성한다. 기존에 파일이 있다면 뒤에 이어 쓴다.                   |

- String name 대신 File 객체 사용 가능

<br>

### 보조 스트림

> **보조 스트림 : Filter Stream, Processing**

- 다른 스트림에 부가적인 기능을 제공하는 스트림
  - ex) 문자 set 변환, buffering, 기본 데이터 형의 전송, 객체 입출력
- 스트림 체이닝(Stream Chaining)
  - 필요에 따라 여러 보조 스트림을 연결해서 사용 가능
  
  <br>

> **보조 스트림의 종류**

| 기능                      | byte 기반             | char 기반 |
| ----------------------- | ------------------- | ------- |
| byte 스트림을 char 스트림으로 변환 | InputStreamReader   |         |
| OutputStreamWriter      |                     |         |
| 버퍼링을 통한 속도 향상           | BufferedInputStream |         |
| BufferedOutputStream    | BufferedReader      |         |
| bufferedWriter          |                     |         |
| 객체 전송                   | ObjectInputStream   |         |
| ObjectOutputStream      |                     |         |

- 생성 - 이전스트림을 생성자의 파라미터에 연결
- 종료 - 보조 스트림의 close()를 호출하면 노드 스트림의 close() 까지 호출됨

<br>

> **사용할 스트림의 결정 과정**

- 노드의 종류 → 타입은 문자열인가 바이트인가? → 방향이 무엇인가 → 추가 기능이 필요한가?

<br>

### **보조 스트림의 활용**

> **InputStreamReader & OutputStreamWriter**

- byte기반 스트림을 char 기반으로 변경해주는 스트림
  - 문자열을 관리하기 위해서는 byte 단위보다 char 단위가 유리
  - 키보드에서 입력(byte stream)받은 데이터를 처리할 경우 등
- 변환 시 encoding 지정 가능

| 메서드 명                | 선언부와 설명                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| InputStreamReader()  | public InputStreamReader(InputStream in)                                                           |
|                      | 기본 캐릭터 셋을 이용해서 InputStreamReader를 생성한다.                                                            |
|                      | public InputStreamReader(InputStream in, String carseName) throws UnsupportedEncodingException     |
|                      | charsetName을 이용해 InputStreamReader를 생성한다.                                                          |
|                      | public InputStreamReader(InputStream in, Charset cs)                                               |
|                      | cs를 이용해 InputStreamReader를 생성한다.                                                                   |
| OutputStreamWriter() | public OutputStreamWriter(OutputStream out)                                                        |
|                      | 기본 캐릭터 셋을 이용해 OutputStreamWriter를 생성한다.                                                            |
|                      | public OutputStreamWriter(OutputStream out, String charseName) throws UnsupportedEncodingException |
|                      | charsetName을 이용해 OutputStreamWriter를 생성한다.                                                         |
|                      | public OutputStreamWriter(OutputStream out, Charset cs)                                            |
|                      | cs를 이용해 OutputStreamWriter를 생성한다.                                                                  |

<br>

> **Bufferd 계열**

- 스트림의 입/출력 효율을 높이기 위해 버퍼를 사용하는 스트림

| 메서드 명                  | 선언부와 설명                                                |
| ---------------------- | ------------------------------------------------------ |
| bufferedInputStrea()   | public BufferedInputStrea(InputStream in)              |
|                        | in을 이용해 크기가 8192인 버퍼를 갖는 BufferedInputStream을 생성한다.    |
|                        | public BufferedInputStrea(InputStream in, int size)    |
|                        | in을 이용해 크기가 size인 버퍼를 갖는 BufferedInputStream을 생성한다.    |
| BufferedOutputStream() | public BufferdOutputStream(OutputStream out)           |
|                        | out을 이용해 크기가 8192인 버퍼를 갖는 BufferedOutputStream을 생성한다.  |
|                        | public BufferdOutputStream(OutputStream out, int size) |
|                        | out을 이용해 크기가 size인 버퍼를 갖는 BufferedOutputStream을 생성한다.  |

- BufferedReader & BufferedWriter

| 메서드 명            | 선언부와 설명                                         |
| ---------------- | ----------------------------------------------- |
| BufferedReader() | public BufferedReader(Reader in)                |
|                  | in을 이용해 크기가 8192인 버퍼를 갖는 BufferedReader를 생성한다.  |
|                  | public BufferedReader(Reader in, int sz)        |
|                  | in을 이용해 크기가 sz인 버퍼를 갖는 BufferedReader를 생성한다.    |
| BufferedWriter() | public BufferedWriter(Writer out)               |
|                  | out을 이용해 크기가 8192인 버퍼를 갖는 BufferedWriter를 생성한다. |
|                  | public BufferedWriter(Writer out, int sz)       |
|                  | out을 이용해 크기가 sz인 버퍼를 갖는 BufferedWriter를 생성한다.   |

- BufferedReader : readLine() → 줄 단위로 데이터를 읽어 들임

<br>

> **객체 직렬화**

- 객체를 파일등에 저장하거나 네트워크로 전송하기 위해 연속적인 데이터롤 변환하는 것
- 반대의 경우는 역 직렬화(deserialization)
- 직렬화 되기 위한 조건
  - Serializable 인터페이스를 구현할 것
  - 클래스의 모든 멤버가 Serializable 인터페이스를 구현해야 함
  - 직렬화에서 제외하려는 멤버는 transient 선언
- serialVersionUID
  - 클래스의 변경 여부를 파악하기 위한 유일 키
  - 직렬화 할 때의 UID와 역 직렬화 할 때의 UID가 다를 경우 예외 발생
  - 직렬화되는 객체에 UID가 설정되지 않았을 경우 컴파일러가 자동 생성
    - 멤버 변경으로 인한 컴파일 시마다 변경 → InvalidClassException 초래
  - 직렬화되는 객체에 대해서 serialVersionUID 설정 권장

<br>

> **ObjectInputStram, ObjectOutputStream**

| 메서드 명                | 선언부와 설명                                                                     |
| -------------------- | --------------------------------------------------------------------------- |
| ObjectOutputStream() | public ObjectOutputStream(OutputStream out) throws IOException              |
|                      | out을 이용해 ObjectOutputStream 객체를 생성한다.                                       |
| writeObject()        | public final void writeObject(Object obj) throws IOException                |
|                      | obj를 직렬화해서 출력한다.                                                            |
| ObjectInputStream()  | public ObjectInputStream(InputStream in) throws IOException                 |
|                      | in을 이용해 ObjectInputStream 객체를 생성한다.                                         |
| readObject()         | public final Object readObject() throws IOException, ClassNOtFoundException |
|                      | 직렬화된 데이터를 역직렬화해서 Object로 리턴한다.                                              |

<br>

> **Scanner와 BufferedReader**

- char 형태의 데이터를 읽기위한 클래스들
- Scanner - 자동 형변환을지원하는 등 사용히 간편하지만 속도가 느림
- BufferedReader - 직접 스트림을 구성해야 하는 등 번거롭지만 속도가 빠름
