"""
s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123


����	���ܾ�
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
            # char �� ���ڰ� �ƴ϶� ������ �� ���ڽĺ�
            pass
    return answer

# ���ڰ� ������ ������
# ���࿡ ���ڰ� ���̿� ���� ���ڰ� �������� ���´ٸ�? 

question = "one4seveneight"
print(solution(question))

print('2'.isdigit())
print('s'.isdigit())