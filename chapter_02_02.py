# 파이썬 변수

# 기본 선언
n = 700
print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = "change value"

# 출력
print(var)
print(type(var))
print()

# object references
# 변수 값 할당 상태
# 1. 타입어 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300)
print(int(300.12))
print()

# ex2)
n = 777
print(n, type(n))
print()

m = n
print(m)
print(type(m))
print()

# id(identity) 객체의 고유값 확인
m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))
print()
print(id(800))
print(id(m) == 800)
print()

# 다양한 변수 선언
# camel case: camelCase -> method
# pascal case: CamelCase -> class
# snake case: camel_case -> python 변수

student_grade = 3
print(student_grade)
print()

# 허용하는 변수 선언 법
age = 1
Age = 2
AGE = 3
aGe = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 사용 불가능
# as, class 등등등
# python reserved words 검색하면 예약어 목록 나와있음
