# 딕셔너리

# 범용적으로 가장 많이 사용됨
# 순서 x, 키 중복 x, 수정 o, 삭제 o

# 선언 딕셔너리는 {} 혹은 dict()로 선언
a = {'name': 'Kim', 'phone': '01000000000', 'birth': '010101'}
b = {0: 'hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Man',
    'City': 'Seoul',
    'Age': '20',
    'Grade': 'A',
    'Status': 'True'
}
e = dict([
    ('Name', 'Man'),
    ('City', 'Seoul'),
    ('Age', '20'),
    ('Grade', 'A'),
    ('Status', 'True')
])

f = dict(
    Name='nice',
    City='seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a-', type(a), a)
print('b-', type(b), b)
print('c-', type(c), c)
print('d-', type(d), d)
print('e-', type(e), e)
print('f-', type(f), f)

# 출력
print('a-', a['name'])  # 속성 접근=키가 없으면 오류
print('a-', a.get('name'))  # get으로 접근 = 키가 없으면 none 출력, 이거 추천(안전함)
print('b-', b[0])
print('b-', b.get(0))
print('f-', f.get('City'))
print('b-', f.get('Age'))


# 딕셔너리 추가
print('>>>>>>>>>>>>>')
a['address'] = 'seoul'  # 중복되면 수정됨
print('a-', a)
a['rank'] = [1, 2, 3]
print('a-', a)

# 딕셔너리 길이
print('a-', len(a))  # 키의 개수를 확인
print('b-', len(b))
print('c-', len(c))
print('d-', len(d))

# dict_key, dict_values, dict_items: 반복문(_iter_에서 사용 가능

print('a-', a.keys())
print('b-', b.keys())
print('c-', c.keys())
print('d-', d.keys())

print('a-', list(a.keys()))
print('b-', list(b.keys()))

print()

print('a-', a.values())
print('b-', b.values())
print('c-', c.values())

print('a-', list(a.values()))
print('b-', list(b.values()))

print('a-', a.items())
print('b-', b.items())
print('c-', c.items())

print()

# pop가 들어가면 원래 목록에서는 삭제됨
print('a-', a.pop('name'))
print('a-', a)

print('c-', c.pop('arr'))
print('c-', c)

print('f-', f.popitem())  # 무작위로 추출
print('f-', f)
print('f-', f.popitem())
print('f-', f)
print('f-', f.popitem())
print('f-', f)
print('f-', f.popitem())
print('f-', f)
print('f-', f.popitem())
print('f-', f)

print()
print('a-', 'birth' in a)
print('d-', 'City' in d)  # 대소문자 확인

# 추가, 수정
print('추가')
print('a-', a)
a['test'] = 'test_dict'
print('a-', a)
print('수정')
a['address'] = 'dj'
print('a-', a)

a.update(birth='0114')
print('a-', a)

temp = {'address': 'Busan'}
a.update(temp)
print('a-', a)
