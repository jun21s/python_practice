# 파이썬 함수식, 람다식(Lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code


# ex1
def first_func(w):
    print("hello, ", w)


word = "goodboy"
first_func(word)


# ex2
def return_func(w1):
    value = "hello, " + str(w1)
    return value


x = return_func("good11")
print(x)


# ex3 다중반환
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


x, y, z = func_mul(10)

print(x, y, z)


# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


q = func_mul2(10)

print(type(q), q, list(q))


# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul2(10)

print(type(p), p, set(p))


# 딕셔너리 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {"v1": y1, "v2": y2, "v3": y3}


d = func_mul2(10)

print(type(d), d, d.items(), d.keys())
