# chapter05_0
# 파이썬 함수 기초

# 함수 = 재사용
# 프로그래머가 만들어서 쓰는거
# 함수구현 -> 재사용, 루틴(프로시저, 서브루틴)

# 종류
# 1. 매개변수가 필요한 함수
# 2. 매개변수가 필요하지 않은 함수
# 3. 결과값을 반환하는 함수(return)
# 4. 결과값을 반환하지 않는 함수


# 예제1: 매개변수가 필요하지 않은 함수
def function1():
    print("예제 1 호출")


# 예제2: 매개변수가 필요한 함수
def function2(a, b):
    print("예제 2 호출", a, b)


# 예제3: 결과값을 반환하지 않는 함수
def function3(x, y):
    print("예제 3 호출", x, y)


# 예제4: 결과값을 반환하는 함수
def function4(x, y):
    return x + y


r = function4(1, 3)
# 실행
function1()
function2(10, 11)
function3(100, 200)
function4(1, 3)
print(r)
