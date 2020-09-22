# 정규 표현식 시작하기
# 사용하는 메타 문자로는 다음과 같은 것들이 있다.
# . ^ & * + ? {} [] \ | ()
"""
[] 문자클래스 
[a-zA-Z] : 알파벳 모두
[0-9] : 숫자
^ : 반대 ex) [^0-9] : 숫자가 아닌 문자만 매치
\d : 숫자와 매치, [0-9]와 동일한 표현식이다.
\D : 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식.
\s : whitespace 문자(space, tab)와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞은 빈간은 공백 문자를 의미한다.
\S : whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w : 문자 + 숫자와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W : 문자 + 숫자가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식
* 대문자로 사용된 것은 소문자의 반대
"""

"""
Dot(.)
정규 표현식의 . 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미
ex) a.b = "a + 모든 문자 + b"
    a[.]b = "a + . + b" a와 b사이에 .문자가 있으면 매치
"""

"""
반복(*)
바로 앞에 있는 문자가 무한대로 반복될 수 있다.
ca*t
ct : a가 0번 반복이라 가능.
cat : 가능
caat : 가능
"""

"""
반복(+)
+는 최소 1번 이상 반복될때 사용
ca+t
ct : 최소 1번이기 때문에 불가
cat : 가능
caat : 가능
"""

"""
반복({m,n})
{m} : 2가 m번 반복되면 매치
ca{2}t : "c + a(반드시 2번 반복) + t"
{m,n} : 2가 (m~n번 반복)되면 매치
ca{2,5}t "c + a(2~5번 반복) + t"
"""

"""
?
ab?c = "a + b(있어도 되고 없어도 된다) + c"
"""

# 정규식을 지원하는 모듈 re
import re
p = re.compile('ab*')
# re.compile을 사용하여 정규 표현식을 컴파일한다. 

"""
정규식을 사용한 문자열 검색
match() : 문자열의 처음부터 정규식과 매치되는지 조사
search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
"""

p = re.compile('[a-z]+')

# match : 문자열의 처음부터 정규식과 매치되는지 조사
m = p.match("python")
print(m)

m = p.match("3 python")
print(m)
"""
p = re.compile(정규 표현식)
m = p.match("조사할 문자열")
if m:
    print("Match found: ", m.group())
else:
    print("No match")
"""

# search : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
m = p.search("python")
print(m)

m = p.search("3 python") # 첫 번째 문자열은 "3"이지만 search는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색하기 때문에 "3"이후의 "python"문자열과 매치된다.
print(m)

# findall : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
result = p.findall("life is too short")
print(result)

# finditer : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
result = p.finditer("life is too short")
print(result)
for r in result: print(r)

"""
match 객체의 메서드
group() : 매치된 문자열을 돌려준다. 
start() : 매치된 문자열의 시작 위치를 돌려준다.
end() : 매치된 문자열의 끝 위치를 돌려준다.
span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
"""
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# 축약형
p = re.compile('[a-z]+')
m = p.match("python")
# ----->
m = re.match('[a-z]+', "python")

"""
컴파일 옵션
DOTALL / S / : dot문자(.)가 줄바꿈 문자를 포함하여 모든 문자와 매치한다.
IGNORECASE / I : 대, 소문자에 관계없이 매치한다.
MULTILINE / M : 여러 줄과 매치한다.(^,$ 메타 문자의 사용과 관계가 있는 옵션이다.)
VERBOSE / X : verbose 모드를 사용한다.(정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수도 있다.)
"""

# DOTALL : dot문자(.)가 줄바꿈 문자(\n)를 포함하여 모든 문자와 매치한다.
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE : 대, 소문자에 관계없이 매치한다.
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

# MULTILINE : 여러 줄과 매치한다.(^,$ 메타 문자의 사용과 관계가 있는 옵션이다.)
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))