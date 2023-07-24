# 파이썬 반복문 for

# for in <collection>
#   <Loop body>

for v1 in range(10):  # 0-9
    print("v1 is: ", v1)

for v2 in range(1, 11):  # 1-10
    print("v2 is: ", v2)

for v3 in range(1, 11, 2):  # 1,3,5,7,9
    print("v3 is: ", v3)

# 1-1000합
sum1 = 0
for v in range(1, 1001):
    sum1 += v
print(sum1)

print(sum(range(1, 1001)))
print("1-1000까지 4의 배수의 합", sum(range(4, 1001, 4)))

# iterables 자료형 반복
# 문자열, 리스트,튜플,집합,사전(딕셔너리)
# iterable 리턴 함수: range,reversed,enumerate,filter,map,zip 들을 for 문에서 사용 가능

names = ["kim", "park", "cho", "lee", "choi", "yoo"]

for name in names:
    print("you are: ", name)


lotto_numbers = [11, 19, 21, 23, 28, 26]

for n in lotto_numbers:
    print("current number: ", n)

word = "beatiful"

for s in word:
    print("word: ", s)

my_info = {"name": "lee", "age": 33, "city": "seoul"}
print(1)
for k in my_info:
    print("key: ", my_info[k])
print(2)
for k in my_info:
    print("key: ", my_info.get(k))
print(3)
for v in my_info.values():
    print("value: ", v)

name = "fInEAPple"
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break 문 =>if 문 중단
number = [14, 3, 7, 4, 10, 24, 2, 1, 1115, 6, 8, 1, 34, 4545, 54]
for num in number:
    if num == 34:
        print("found 34")
        break
    else:
        print("not found", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
print(lt)
for v in lt:
    if type(v) is bool:
        continue
    print("current type: ", v, type(v))
    print(v * 3)

# for - else
number = [14, 3, 7, 4, 10, 24, 2, 1, 1115, 6, 8, 1, 34, 4545, 54]

for num in number:
    if num == 124:
        print("found 124")
        break
else:
    print("not found 124")

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print("{:4d}".format(i * j), end="")
    print()

# 변환 예제
name2 = "aceman"
print("reversed", reversed(name2))
print("list", list(reversed(name2)))
print("tuple", tuple(reversed(name2)))
print("set", set(reversed(name2)))  # 순서 없음
