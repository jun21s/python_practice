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
