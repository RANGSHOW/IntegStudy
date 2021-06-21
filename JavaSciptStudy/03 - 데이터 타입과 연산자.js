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


