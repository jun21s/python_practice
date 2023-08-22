# input 사용법
# 기본타입 = str
# name = aaa
# print(name*3) 하면 aaaaaaaaa 이런식으로 문자를 3번 반복해 출력

# ex1
name = input("enter your name: ")
grade = input("enter your grade: ")
company = input("enter your company name: ")

print(name, grade, company)  # 작동 하기 위해서는 python chapter_05_02.py 를 cmd 창에다가 실행

# ex2
number = input("enter number: ")
print(number)
print("type of number", type(number))
print("type of name", type(name))

# ex3(계산)
f_number = int(input("enter number1: "))
s_number = int(input("enter number1: "))

total = f_number + s_number
print("f_number + s_number: ", total)

# ex4
float_number = float(input("enter float number: "))
print("input float: ", float_number)
print("input type: ", type(float_number))

# ex5
print(
    "first name -{0}, last name - {1}".format(
        input("enter first name: "), input("enter second name: ")
    )
)
