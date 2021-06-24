// 숫자 타입
var intNum = 10;
var floatNum = 0.1;

// 문자열 타입
var singleQuoteStr = 'sigle quote string';
var doubleQuoteStr = "double quote string";
var singleChar = 'a';

// 불린 타입
var boolVar = true;

// undefined 타입
var emptyVar;

// null 타입
var nullVar = null;

console.log(
    typeof intNum,
    typeof floatNum,
    typeof singleQuoteStr,
    typeof doubleQuoteStr,
    typeof singleChar,
    typeof boolVar,
    typeof nullVar,
    typeof emptyVar,
)


// 자바스크립트 나눗셈 연산
var num = 5 / 2
console.log(num);  // (출력값) 2.5
console.log(Math.floor(num));  // (출력값) 2


// 자바스크립트 문자열 예제
// str 문자열 생성
var str = "test";
console.log(str[0], str[1], str[2], str[3]);  // (출력값) t e s t

// 문자열의 첫 글자를 대문자로 변경?
str[0] = 'T';
console.log(str);  // (출력값) test

var a = [1, 2, 3];
b = a
console.log(a == b)
console.log(a === b)


// 객체 생성 //

// Object()를 이용한 foo 빈 객체 생성
var foo = new Object();

// foo 객체 프로퍼티 생성
foo.name = 'foo';
foo.age = 30;
foo.gender = 'male';

console.log(typeof foo);    // (출력값) object
console.log(foo);           // (출력값) { name: 'foo', age: 30, gender: 'male }


// 객체 리터럴 방식으로 foo 객체 생성
var foo = {
    name: 'foo',
    age: 30,
    gender: 'male'
};

console.log(typeof foo);    // (출력값) object
console.log(foo);           // (출력값) { name: 'foo', age: 30, gender: 'male }


// 객체의 프로퍼티 접근하기
var foo = {
    name: 'foo',
    major: 'computer science'
};

// 객체 프로퍼티 읽기
console.log(foo.name);      // (출력값) foo
console.log(foo['name']);   // (출력값) foo
console.log(foo.nickname);  // (출력값) undefined

// 객체 프로퍼티 갱신
foo.major = 'electronics engineering';
console.log(foo.major);     // (출력값) electronics engineering
console.log(foo['major']);  // (출력값) electronics engineering

// 객체 프로퍼티 동적 생성
foo.age = 30;
console.log(foo.age);       // (출력값) 30

// 대괄호 표기법만 사용해야 할 경우
foo['full-name'] = 'foo bar';   
console.log(foo['full-name']);      // (출력값) foo bar
console.log(foo.full-name);         // (출력값) NaN
console.log(foo.full);              // (출력값) undefined
console.log(name);                  // (출력값) undefined

// 3.2.3 for in 문을 통한 객체 프로퍼티 출력
// 객체 리터럴을 통한 foo 객체 생성

var foo = {
    name: 'foo',
    age: 30,
    major: 'cumputer science'
};

console.log(typeof foo);  // (출력값) object


// for in 문을 이용한 객체 프로퍼티 출력
var prop;
for (prop in foo) {
    console.log(prop, foo[prop]);
}

// 3.2.4 객체 프로퍼티 삭제
// 객체 리터럴을 통한 foo  객체 생성

var foo = {
    name: 'foo',
    nickname: 'babo'
};

console.log(foo.nickname);
delete foo.nickname;
console.log(foo.nickname);

delete foo;
console.log(foo.name);

// 3.3.0 동일한 객체를 참조하는 두 변수 objA와 objB
var objA = {
    val: 40
};
var objB = objA;

console.log(objA.val);  // (출력값) 40
console.log(objB.val);  // (출력값) 40

objB.val = 50;
console.log(objA.val);  // (출력값) 50
console.log(objB.val);  // (출력값) 50


