# 내장 함수
# abs : 절대값을 리턴
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all : 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나로도 있으면 False
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

# any : x중 하나로도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때만 False
print(any([1, 2, 3, 0]))
print(any([0, '']))

# chr : 아스키 코드 값을 입력받아  그 코드에 해당하는 문자를 출력하는 함수
print(chr(97))
print(chr(65))

# dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 
print(dir([1, 2, 3]))
print(dir({'1': 'a'}))

# divmod : divmod(a, b)는 2개의 숫자를 입력받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플형태로 리턴
print(divmod(7, 3))

# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate객체를 리턴
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval : 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결관값을 돌려주는 함수
print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# filter : 첫번째 인수로 함수 이름, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때
#          반환 값이 참인 것만 묶어서 돌려준다.
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

def positiveFilter(x):
    return x > 0

print(list(filter(positiveFilter, [1, -3, 2, 0, -5, 6])))

# hex : 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수
print(hex(234))
print(hex(3))

# id
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))

# input : 사용자 입력을 받는 함수
# a = input()
# b = input("Enter: ")

# int : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력받으면 그대로 돌려준다.
print(int('3'))
print(int(3.4))
print(int('11', 2))  # 2진수의 11를 10진수로
print(int('1A', 16)) # 16진수의 1A를 10진수로

# isinstance : 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False
class Person: pass

a = Person()
print(isinstance(a, Person))

# len : 입력값의 길이를 돌려준다.
print(len("python"))
print(len([1, 2, 3]))
print(len((1, 'a')))

# list : 반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수
print(list("python"))
print(list((1, 2, 3)))

# map : 함수와 반복 가능한 자료형을 입력으로 받는다. 입력받은 자료형의 각 요소를 함수가 수행한 결과를 묶어서 돌려주는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)
# => map 사용
def two_times(x): return x * 2
print(list(map(two_times, [1, 2, 3, 4])))

# max : 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려줌
print(max([1, 2, 3]))
print(max("python"))

# min : 인수로 반복 가능한 자료형을 받아 그 최솟값을 돌려줌
print(min([1, 2, 3]))
print(min("python"))

# oct : 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려줌
print(oct(34))
print(oct(12345))

# open
# 파일 이름과 읽기 방법을 입력받아 파일 객체를 돌려주는 함수로 읽기 방법을 생략하면 기본값으로 읽기 전용모드(r)로 파일 객체를 만들어 돌려준다.
# w : 쓰기 모드, r : 읽기 모드, a : 추가 모드, b : 바이너리 모드
# b(바이너리 모드)는 w, r, a와 함께 사용됨
# f = open('binary_file', 'rb')
# f = open('read_mode.txt', 'r')
# f = open('read_mode.txt')
# f = open('append_mode.txt', 'a')

# ord : 문자의 아스키 코드 값을 돌려줌
print(ord('a'))
print(ord('0'))

# pow : x의 y 제곱한 결괏값을 돌려준다.
print(pow(2, 4))
print(pow(3, 3))

# range : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다. 주로 for문과 함께 사용
# 인수가 하나일 경우 0부터 시작
print(list(range(5)))
# 인수가 2개일 경우 시작과 끝(끝은 포함하지 않는다.)
print(list(range(5, 10)))
# 인수가 3개일 경우 마지막 숫자는 사이의 거리를 표현
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

# round : 숫자를 입력받아 반올림해주는 함수
print(round(4.6))
print(round(4.2))
print(round(4.25, 1))
print(round(5.678, 2))

# sorted : 입력값을 정렬한 후 그 결과를 리스트로 리턴
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))
print(sorted(['나', '다', '가']))

# str : 문자열 형태로 객체를 변환하여 돌려주는 함수
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

# sum : 입력받은 리스트나 튜플의 모든 요소의 함을 돌려주는 함수
print(sum([1, 2, 3]))
print(sum((4, 5, 6)))

# tuple : 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수
print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# type : 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc"))
print(type([]))
print(type((1, 2, 3)))

# zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))