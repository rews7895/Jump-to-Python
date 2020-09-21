# 함수
"""
def 함수 이름(매개변수):
    수행할 문장1
    수행할 문장2
    ...
"""
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)
print(add(a, b))

# 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

# 결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))

# 여러개의 입력값을 받는 함수
# 매개변수 이름 앞에 *을 붙이면 전부 모아서 튜플로 만들어줌
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1, 2, 3)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# **키워드 파라미터 : 매개변수가 딕셔너리가 되고 모든 key = value 형태의 결괏값이 그 딕셔너리에 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a = 1)
print_kwargs(name = 'foo', age = 3)

# 결괏값은 언제나 하나로 리턴된다.
def add_and_mul(a, b):
    return a + b, a * b
result = add_and_mul(3, 4)
print(result) # 튜플 형태로 리턴
# 두개로 리턴 받고 싶으면?
result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

# return은 함수를 빠져나가고 싶을 때도 사용가능

# 매개변수에 초깃값 미리 설정
def say_myself(name, old, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {old}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박준석", "29")

# global 명령어
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)

# lambda : 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. 보통 함수를 한줄로 간결하게 만들 때 사용한다. 
# lambda 매개변수1, 매개변수2, ...: 매개변수를 사용한 표현식
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.
add = lambda a, b: a + b
result = add(3, 4)
print(result)