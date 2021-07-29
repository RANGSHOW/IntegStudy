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

arr = [1, 2, 3, 4]

var a = 100;
var b = 100;

var objA = { value: 100 };
var objB = { value: 100 };
var objC = objA;

console.log(objA == objB);
console.log(objA === objB);
console.log(objA == objC);
console.log(objA === objC);

// 3.3.2 Call by Value  와 Call by Reference 차이

var a = 100;
var objA = { value: 100 };

function changeArg(num, obj) {
    num = 200;
    obj.value = 200;

    console.log(num);
    console.log(obj);

}
changeArg(a, objA);

console.log(a);
console.log(objA);

// 3.4.0 객체 생성 및 출력 (p.50)
var foo = {
    name: 'foo',
    age: 30
};

console.log(foo.toString());
console.dir(foo);


// 3.5.1. 배열 리터럴을 통한 배열 생성

// 배열 리터럴을 통한 5개 원소를 가진 배열 생성
var colorArr = ['orange', 'yellow', 'blue', 'green', 'red'];
console.log(colorArr[0]);
console.log(colorArr[1]);
console.log(colorArr[4]);


// 3.5.3  배열의 legnth 프로퍼티
for (let i=0; i<10; i++) {
    for (let j=0; j<10; j++) {
         
    }
}

var myObject = {
    name: 'Kim',
    age: 30,
    job: null
}

var array = [1, 2, 3, 4, 5, 6]
console.log(array[1])

// 3.5.2 배열 요소 생성

// 빈 배열
var emptyArr = [];
console.log(emptyArr[0]);  // (출력값) undefined

// 배열 요소 동적 생성
emptyArr[0] = 100;
emptyArr[3] = 'eight';
emptyArr[7] = true;
console.log(emptyArr);  // (출력값) [ 100, <2 empty items>, 'eight', <3 empty items>, true ]

console.log(emptyArr.length);  // (출력값) 8


// 3.5.3 배열의 length 프로퍼티
// 배열 내에 가장 큰 인덱스에 1을 더한 값

var arr = [];
console.log(arr.length);  // (출력값) 0

arr[0] = 0;  // arr.length == 1
arr[1] = 1;  // arr.length == 2
arr[2] = 2;  // arr.length == 3
arr[100] = 100;
console.log(arr.length); // (출력값) 101

// 배열 프로퍼티의 명시적 변경
var arr = [0, 1, 2];
console.log(arr.length);  // (출력값) 3

arr.length = 5;
console.log(arr);  // (출력값) [ 0, 1, 2, <2 empty items> ]

arr.length = 2;
console.log(arr);  // (출력값) [ 0, 1 ]
console.log(arr[2]);  // (출력값) undefine


// 3.5.3.1. 배열 표준 메서드와 length 프로퍼티

// arr 배열 생성
var arr = ['zero', 'one', 'two'];

// push() 메서드 호출
arr.push('three');
console.log(arr);  // (호출값) ['zero', 'one', 'two', 'three']

// length 값 변경 후, push() 메서드 호출
arr.length = 5;
arr.push('four');
console.log(arr);  // (출력값) ['zero', 'one', 'two', 'three', undefined, 'four']


// 3.5.4 배열과 객체

// colorArray 배열
var colorArray = ['orange' ,'yellow', 'green'];
console.log(colorArray[0]);  // (출력값) orange
console.log(colorArray[1]);  // (출력값) yellow
console.log(colorArray[2]);  // (출력값) green

// colorObj 객체
var colorObj = {
    '0': 'orange',
    '1': 'yellow',
    '2': 'green'
}

console.log(colorObj[0]);  // (출력값) orange
console.log(colorObj[1]);  // (출력값) yellow
console.log(colorObj[2]);  // (출력값) green

// typeof 연산자 비교
console.log(typeof colorArray);  // (출력값) object (not array)
console.log(typeof colorObj);  // (출력값) object

// length 프로퍼티
console.log(typeof colorArray);  // (출력값) 3
console.log(typeof colorObj);  // (출력값) undefined

// 배열 표준 메서드
colorArray.push('red'); // ['orange' ,'yellow' ,'green', 'red']
colorObj.push('red');
    // Uncaught TypeError: Object #<Object> has no method 'push'

var intNum = 3;
for (var i=0; i<intNum; i++) {
    for (var j=0; j<intNum; j++) {
        if (i + j > 2) {
            console.log("i: " + i + " j: " + j);
        }
    }
}

var arrList = [1, 2, 3, 4, 5]

```