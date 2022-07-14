"""
s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123


숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine
"""

def solution(string: str) -> str:
    answer = []
    for char in string:
        if char.isdigit() == True:
            answer.append(char)
        else:
            # char 가 숫자가 아니라 문자일 때 문자식별
            pass
    return answer

# 숫자가 있으면 나눈다
# 만약에 숫자가 사이에 없고 문자가 연속으로 나온다면? 

question = "one4seveneight"
print(solution(question))

print('2'.isdigit())
print('s'.isdigit())