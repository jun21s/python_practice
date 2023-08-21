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


# 중요
# *args, **kwargs


# *args 언팩킹
# *이 없으면 하나하나의 요소로 생각
# *이 있으면 그 자체를 하나의 index로 생각
def args_func(*args):  # 매개변수 명 자유
    for i, v in enumerate(args):
        print("result: {}".format(i), v)
    print("----")


args_func("lee")
args_func("lee", "park")


# **kwargs 언팩킹
def kwargs_func(**kwargs):  # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("----")


kwargs_func(name1="hello")
kwargs_func(name1="hello", name2="mello")


# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, "lee", "kim", "park", "20", age1=10, age2=20, age3=50)


# 중첩함수
def nested_func(num):
    def func_in_func(num):  # 함수 설정
        print(num)

    print("in func")
    func_in_func(num + 100)  # 함수 안의 함수 실행


nested_func(100)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수: 객체 생성 -> 메모리 할당
# 람다식: 즉시 실행 함수(heap 초기화) -> 메모리 초기화
# 남발시 가독성 감소


def mul_func(x, y):
    return x * y


a = mul_func(10, 50)
print(a)
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 30))


def func_final(x, y, func):
    print(x * y * func(100, 100))


func_final(10, 20, lambda x, y: x * y)
