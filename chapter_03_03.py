print('시작')
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서0, 중복0, 수정0, 삭제0)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foot', 3, 4, False, 3.141592]
print()
# 인덱싱
print('d-', type(d), d)
print('d-', d[1])
print('d-', d[1]+d[1]+d[0])
print('d-', d[-1])
print('e-', e[-1][1])
print('e-', list(e[-1][1]))
print()

# 슬라이싱
print('d-', d[0:3])
print('d-', d[2:])
print('e-', e[-1][1:3])
print()

# 리스트 연산
print('c+d', c+d)
print('c*3', c*3)
print("'Test+c[0]'", 'Test'+str(c[0]))
print()

# 값 비교
print(c == c[:3]+c[3:])
print(c)
print(c[:3]+c[3:])
print(c[:3])
print(c[3:])
print()

# identity
temp = c
print(temp, c)
print(id(c))
print(id(temp))

# 리스트 수정, 삭제
c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c']
print(c)
c[1] = ['a', 'b', 'c']
print(c)
c[1:3] = []
print(c)
del c[2]
print(c)

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a-', a)
a.append(10)
print('a-', a)
a.sort()
print('a-', a)
a.reverse()
print('a-', a)
print('a-', a.index(3), a[3])
a.insert(0, 7)
print('a-', a)
a.reverse()
print('a-', a)
#del a[6]
#print('a-', a)
a.remove(10)
print('a-', a)
print('a-', a.pop())
print('a-', a)
print('a-', a.pop())
print('a-', a)
print('a-', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a-', a)

# 삭제: remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
