# 집합(set)
# 집합 자료형 (순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4, 1, 2, 3])
c = set([1, 4, 5, 6])
d = set([1, 2, "pen", "cap", "plate"])
e = {"foo", "bar", "bax", "sad", "dadfs"}
f = {42, "asd", (1, 2, 3), 3.141592}

print("a-", type(a), a)
print("b-", type(b), b)
print("c-", type(c), c)
print("d-", type(d), d)
print("e-", type(e), e)
print("f-", type(f), f)

# 튜플 변환(set->tuple)
t = tuple(b)
print("t-", type(t), t)
print("t-", t[0], t[1:3])

# 리스트 변환(set->list)
l = list(c)
l2 = list(e)

print("l-", l)
print("l2-", l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("s1&s2: ", s1 & s2)  # s1과 s2의 교집합
print("s1&s2: ", s1.intersection(s2))

print("s1|s2: ", s1 | s2)  # 합집합
print("s1|s2: ", s1.union(s2))

print("s1-s2: ", s1 - s2)  # 차집합
print("s1-s2: ", s1.difference(s2))

# 중복 원소 확인
print("s1 & s2: ", s1.isdisjoint(s2))  # 교집합이 있으면 false

# 부분 집합 확인
print("s1이 s2의 부분집합인지: ", s1.issubset(s2))  # 부분 집합이면 true
print("superset", s1.issuperset(s2))  # s1이 s2를 포함하는지

# 추가, 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)
s1.remove(1)  # 없는 원소를 삭제하면 에러 발생=예외 발생 가능
s1.discard(2)  # 없는 원소를 삭제해도 에러 발생 안함=예외 발생 안함
s1.clear()  # 전체 삭제
print(s1)


a = [1, 2, 3]
a.clear()
print(a)
