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
numberAlpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

string = "23four5six7"
string.replace('zero', '0')

def solution(s):
    s.replace('zero', '0')
    s.replace('one', '1')
    s.replace('two', '2')
    s.replace('three', '3')
    s.replace('four', '4')
    s.replace('five', '5')    
    s.replace('six', '6')
    s.replace('seven', '7')
    s.replace('eight', '8')
    s.replace('nine', '9')
    answer = int(s)
    return answer

def solution2(string: str) -> str: # �̿ϼ� 
    answer = []
    for i in len(string):
        if string[i].isdigit() == True:
            answer.append(i)
        else:
            if string[i] == 'z':
                answer.append('0')
                # i�� ��ġ �ٽ� ���
            elif string[i] == 'o':
                answer.append('1')
                # i�� ��ġ �ٽ� ���    
            elif string[i] == 't': # two, three ����
                if string[i + 1] == 'w':
                    answer.append('2')
                    # i�� ��ġ �ٽ� ���                  
                else:
                    answer.append('3')
                    # i�� ��ġ �ٽ� ���                  
                pass

# ���ڰ� ������ ������
# ���࿡ ���ڰ� ���̿� ���� ���ڰ� �������� ���´ٸ�? 

question = "one4seveneight"
print(solution(question))

print('2'.isdigit())
print('s'.isdigit())