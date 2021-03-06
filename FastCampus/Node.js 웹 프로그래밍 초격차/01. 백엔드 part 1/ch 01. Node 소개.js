
/*

>>> ch01_01. JavaScript 생태계와 Node의 역사

|| 자바 스크립트 

    - 스크립트 언어 (한 줄 한 줄 실행되던 언어)
    - 사용자 친화적인 웹 / 앱을
    - 2008년 V8 JS Engine 공개 (크롬에 들어간 Open Source)
        - 실행 환경에 상관없이 작동하는 JS Engine (브라우저든 서버든)
        - 서버에서 동작하는 자바 스크립트 런타임을 만들게 된다 -> Node.js 의 시초
    - 다양한 프레임워크로 한 가지 언어도 풀스택 개발을 가능하게 함
    - 서버 사이드 렌더링과 같은 고급 기술을 사용할 수 있게 됨


    cf. 런타임(Runtime)이란? 
        - 프로그램이 실행되고 있는 동안의 동작
        - 프로그램이 실행되고 있는 때 존재하는 곳, 프로그밍 언어가 구동되는 환경
        - 프로그램이 싱핼되는 동안의 시간
        - 런타임 환경 (Runtime Environment)
            - 운영체제 위에서 또는 운영 체제 자체에서 실행되며,
            위 계층이 사용하거나 필요한 서비스를 제공하는 환경 (ex. JRE)

    cf. 서버 사이드 렌더링(SSR)이란?
        - 서버에서 페이지를 그려 클라이언트(브라우저)로 보낸 후 화면에 표시하는 기법
        - 검색 엔진 최적화 (결과가 사용자에게 많이 노출될 수 있도록 최적화하는 기법)
        - 빠른 페이지 렌더링이 장점


>>> ch01_02. Node의 특징, 강점, 약점

|| 고전적인 처리 방식

    let databaseResult = queryDatabase() 
    let apiResult = getSomethingFromAPI()

        - 여타 절차적 프로그래밍 언어들처럼 순서대로 실행
        - 위에 있는 줄이 실행되는 동안 그 아래에 있는 코드를 실행할 수 없다
            - 네트워크를 통하는 순간 대기 시간이 기하급수적으로 증가한다


|| JavaScript식 비동기 처리 방식 (원래는 한 줄씩 실행하는 동기적 언어)

    queryDatabase(result => { // Do sth w.result.. })
    getSomethingFromAPI(result => { // Do sth w.result.. })

        - 위에 줄이 실행되고 결과를 기다리는 동안 (데이터 베이스로 부터 응답이 오기 전에)
        아래의 코드 실행할 수 있다
        - 결과가 돌아오면 해당 결과를 바탕으로 코드를 실행하면 된다 
        - 모든 요청을 보내버리고 돌아오면 대응을 하는 방식이다

    - JavaScript는 언어 수준에서 비동기 문제를 잘 해결해두었다.
        - 사이사이에서 낭비되는 클럭 수는 없다.
        
저수준의 오래 걸리는 일은 Node에게, 고수준의 로직은 메인 스레드에서 (offloading 방식이라고 함)


|| 저수준 처리의 개선
    - 저수준 처리는 Node가 빠르게 처리하기 어려운 부분이다
    - Node.js 는 C와 WebAssembly 모듈을 바인딩해 사용하는 방법을 제공
    - C는 Node-gyp를 통해, WebAssembly는 Node 12 버전부터 제공되고 있다


|| npm (node package manager)
    방대한 오픈 소스 생태계


>>> ch01_03. Glitch로 설정 없이 바로 Node 웹 서버 코딩해보기

    const http = require('http')

    const server = http.createServer((req, res) => {
        res.statusCode = 200
        res.end('Hello!')
    })

    const PORT = 3000

    server.listen(PORT, () => {
        console.log('The Server is listening at port', PORT)
    })



*/