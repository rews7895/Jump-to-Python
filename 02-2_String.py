# 문자열 자료형
a = "Hello World"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python''' 
print(a)
print(b)
print(c)
print(d)

# 문자열에 작은따옴표(') 포함시키기
e = "Python's favorite food is perl"
print(e)
# 문자열에 큰따옴표(") 포함시키기
f = '"Python is very easy." he says.'
print(f)
# 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
g = 'Python\'s favorite food is perl'
h = "\"Python is very easy.\" he says."
print(g)
print(h)

# 줄 바꾸기
i = "Life is too short\nYou need python"
print(i)
j = '''
Life is too short
You need python
'''
k = """
Life is too short
You need python
"""
print(j)
print(k)

# 문자열 더해서 연결
head = "Python"
tail = " is fun!"
print(head + tail)
print(head * 2)
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이
string = "Life is too short, You need Python"
print(len(string))
# 문자열 인덱싱
print(string[3])
print(string[-1])
# -0 = 0과 같다
print(string[-0])
# 문자열 슬라이싱
print(string[0:4])
print(string[19:])
print(string[19:-7])
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
year = a[:4]
day = a[4: 8]
print(year)
print(day)

# 문자열 치환
a = "Pithon"
print(a[:1] + 'y' + a[2:])

# 문자열 포맷팅
a = "I eat %d apples." % 3
print(a)
a = "I eat %s apples." % "five"
print(a)
number = 3
a = "I eat %d apples." % number
print(a)
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)
# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
e = "Error is %d%%." %98
print(e)
a = "I eat {0} apples.".format(3)
print(a)
a = "I eat {0} apples.".format("five")
print(a)
number = 3
a = "I eat {0} apples.".format(number)
print(a)
day = "three"
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)
a = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)
a = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(a)
y = 3.42134234
print("{0:0.4f}".format(y))
# f문자열 포매팅 : 문자열 앞 f접두사를 붙이면 f문자열 포매팅 기능을 사용할 수 있다.
name = '박준석'
age = 29
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f"나는 내년이면 {age + 1}살이 된다")

# 찾는 문자 개수 세기
a = "hobby"
print(a.count('b'))

# 위치 알려주기, 없으면 -1 리턴
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
a = "Life is too short"
print(a.index('t'))
# 없으면 에러 발생
#print(a.index('k'))

# 문자열 삽입
a = ",".join("abcd")
print(a)
a = ",".join(['a', 'b', 'c', 'd'])
print(a)

# 소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())
# 대문자를 소문자로 바꾸기
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기
a = " hi "
print(a.lstrip())
# 오른쪽 공백 지우기
print(a.rstrip())
# 양쪽 공백 지우기
print(a.strip())

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))