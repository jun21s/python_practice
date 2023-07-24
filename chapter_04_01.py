# if 구문
print(type(True))  # 0이 아닌 수, "문자", [1,2,3], (1,2,3)
print(type(False))  # 0, "", [], (), {} 비어있는 느낌

# 예1
if True:
    print("Good")

if 1:
    print("he")

if False:
    print("bad")

# ex2
if False:
    print("bad")
else:
    print("good")

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10
print(x == y)

print(x != y)

print(x >= y)

print(x < y)

city = "busan"
if city:
    print("your are in:", city)
else:
    print("please enter your city")

city = ""
if city:
    print("your are in:", city)
else:
    print("please enter your city")


# 논리연산자(*중요*)
# and, or, not

a = 75
b = 40
c = 50

print("and: ", a > b and b > c)
print("or: ", a > b or b > c)
print("not: ", not a > b)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 관계 논리 순으로 우선순위
print("e1: ", 3 + 12 > 7 + 3)
print("e2 ", 5 + 10 * 3 > 7 + 3 * 20)
print("e3 ", 5 + 10 > 3 and 7 + 3 == 10)
print("e4 ", 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = "a"

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == "a":
    print("pass")
else:
    print("fail")

id1 = "vip"
id2 = "admin"
grade = "platinum"

if id1 == "vip" or id2 == "admin":
    print("관리자")

if id2 == "admin" and grade == "platinum":
    print("최상위 관리자")

# 다중조건문
num = 78

if num >= 90:
    print("grade a")
elif num >= 80:
    print("grade b")
elif num >= 70:
    print("grade c")
else:
    print("fail")

# 중첩 조건문
grade = "c"
total = 95

if grade == "a":
    if total >= 90:
        print("전액 장학금")
    elif total >= 80:
        print("장학금 80%")
    else:
        print("장학금 50%")
else:
    print("장학금 없음")

# in, not in
q = [10, 20, 30]
w = [70, 80, 90, 100]
e = {"name": "lee", "city": "seoul", "grade": "a"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("seoul" in e.values())
