# while 구문(무한 반복 될 수 도 있으니 조심해야함)
# 파이썬 반복문

# while <expr 표현식>:
#   <statement(s)>

n = 5
while n > 0:
    n = n - 1
    print(n)

a = ["foo", "bar", "baz"]

while a:
    print(a.pop())

# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)


m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)

# if 중첩
i = 1

while i <= 10:
    print("i", i)
    if i == 6:
        break
    i += 1

# while else
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        continue
else:
    print("else out.")


a = ["fa", "as", "dsf", "sdfsaf"]
s = "asdf"

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, "not found in list")


# 무한반복
# while True:

a = ["fa", "as", "dsf", "sdfsaf"]

while True:
    if not a:
        break
    print(a.pop())
