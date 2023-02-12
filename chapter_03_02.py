# 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are tou?"""
str4 = '''I'm fine.'''

print(type(str1), type(str2), type(str3), type(str4))

print(str1, str2, str3, str4)
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자 사용(escape code)
print("I'm Boy")
print('I\'m boy')
print('a\t b')  # tab 키 만큼 띄우기
print('a\n b')  # 줄바꿈
print('a\"\"b')
print()
escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# tab, 줄바꿈
t_1 = "Click \t Start"
t_2 = "New Line\n Check"
print(t_1)
print(t_2)

# raw string
raw_1 = r'D:\Python\test'
print(raw_1)
print()

# 멀티라인 입력
multi_str =\
    '''
sdafdasfsfsfsfsa
fsddddddddddssssssddddd
ddd000000000000000
000000000000000000
000'''
print(multi_str)
print()

# 문자열 연산
str_01 = 'Python'
str_02 = 'Apple'
str_03 = 'How are you'
str_04 = 'Seoul Daejeon Busan Jinju'
print(str_01*3)
print(str_01+str_02)
print('y' in str_01)
print('h' in str_03)
print('H' in str_03)
print('P' not in str_02)
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(True), type(str(True)), type(True))
print()

# 문자열 함수(upper, sialnum, startswith.....)
print("Capitalize: ", str_01.capitalize())
print("endswith?:", str_02.endswith("s"))
print("endswith?:", str_02.endswith("e"))
print("replace:", str_01.replace("thon", 'good'))
print("sorted:", sorted(str_01))
print("split:", str_04.split(' '))
print()

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))  # _iter_

for i in im_str:
    print(i)
print()

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3])
print(str_s1[5:11])
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1)-1])
print(str_s1[1:11:2])
print(str_s1[-2:])
print(str_s1[-11:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])
print()

# 아스키 코드, 유니코드
a = 'z'
print(ord(a))
print(ord('z'))
print(chr(122))
print(ord('가'))
print(ord('ㄱ'), ord('ㅏ'))
