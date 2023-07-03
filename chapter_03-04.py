# 파이썬 튜플
# 리스트와 비교 중요
# 튜플은 순서 o, 중복 o, 수정 x, 삭제 x = 불변

# 선언
a = ()
b = (1,)  # 원소가 하나 일 때는 , 를 찍어야지 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))  # 튜플 안에 튜플

# 인덱싱

print('>>>>>>>>')
print('인덱싱')
print('d-', d[1])
print('d-', d[1]+d[1]+d[0])
print('d-', d[-1])
print('e-', e[-1])
print('e-', e[-1][1])
print('e-', list(e[-1][1]))

# 수정 안되는거 확인
# d[0] = 10000 에러 발생함

# 슬라이싱

print('>>>>>>')
print('슬라이싱')
print('d-', d[0:3])
print('e-', e[1:3])
print('e-', e[2][0:3])

# 튜플 연산
print('>>>>>>')
print('튜플연산')
print('c+d', c+d)
print('c*3', c*3)

print('>>>>>>')
print('튜플함수')
a = (5, 2, 3, 1, 4)
print('a-', a)
print('a-', a.index(3))
print('a-', a.count(2))

# 팩킹, 언팩킹

print('>>>>>>')
print('팩킹')

t = ('foo', 'bar', 'asc', 'asd')  # 그냥 묶는거
print(t)
print(t[2])

print('>>>>>>')
print('언팩킹')
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4),)
print(x1, x2, x3, x4)
print(t)

t2 = 1, 2, 3  # 괄호가 없어도 튜플 선언 가능, 팩킹
t3 = 4,  # 튜플(한개여서 , 필수)
x1, x2, x3 = t2  # 언팩킹
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
