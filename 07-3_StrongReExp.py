# 강력한 정규 표현식의 세계로

# 메타 문자
# | : or과 동일한 의미로 사용. A|B라는 정규식이 있다면 A또는 B라는 의미
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# ^ : 문자열의 맨 처음과 일치함을 의미.
# MULTILINE을 사용할 경우 여러 줄의 문자열일 때 각 줄의 처음과 일치하게 된다.
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# $ : ^메타 문자와 반대의 경우. 즉 $는 문자열의 끝과 매치함을 의미
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \A : 문자열의 처음과 매치됨
# MULTILINE 사용시 ^은 각 줄의 문자열의 처음과 매치되지만 \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.

# \Z : 문자열의 끝과 매치됨.
# MULTILINE 옵션 사용 시 $메타 문자와는 달리 전체 문자열의 끝과 매치된다.

# \b : 단어 구분자. 보통 단어는 whitespace에 의해 구분된다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

# \B : \b 메타 문자와 반대의 경우. 즉 whitespace로 구분된 단어가 아닌 경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

# 그루핑 : 특정 문자열이 계속해서 반복되는지를 확인할 때 사용
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+") # (\w+)으로 만들면 match객체의 group 메서드를 사용하여 그루핑된 부분의 문자열만 뽑아낼 수 있다.
"""
group(0) : 매치된 전체 문자열
group(1) : 첫 번째 그룹에 해당하는 문자열
group(2) : 두 번째 그룹에 해당하는 문자열
group(n) : n번째 그룹에 해당하는 문자열
"""
m = p.search('park 010-1234-1234')
print(m.group(1))
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search('park 010-1234-1234')
print(m.group(2))
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search('park 010-1234-1234')
print(m.group(3))

# 그루핑된 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()

# 정규식은 그룹을 만들 때 그룹 이름을 지정할 수 있다.
# (\w+) -> (?P<name>\w+)
p = re.compile("(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group('name'))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()

# 전방 탐색
"""
(?=...) / 긍정형 전방 탐색 : ...에 해당하는 정규식과 매치되어야ㅑ 하며 조건이 통과되어도 문자열이 소비되지 않는다.
(?!...) / 부정형 전방 탐색 : ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
"""
p = re.compile(".+:")
m = p.search('http://google.com')
print(m.group())

# 긍정형 전방 탐색 : ...에 해당하는 정규식과 매치되어야ㅑ 하며 조건이 통과되어도 문자열이 소비되지 않는다.
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

# 파일 확장자 정규식
"""
.*[.].*$
"""

# 부정형 전방 탐색 : ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
"""
.*[.](?!bat$).* bat 제외
.*[.](?!bat$|exe$).*$ bat, exe제외
"""

# sub : 문자열 바꾸기
p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))
# 딱 한 번만 바꾸고 싶은 경우 3번째 매개변수로 count 값을 넘기면 된다.
print(p.sub('color', 'blue socks and red shoes', count=1))
# subn : 문자열을 바꾸고 튜플로 반환
# sub 메서드를 사용할 때 참조 구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 참조번호도 가능
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))

# Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
len(s)
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
# Greed 제한 : ?사용하여 제한할 수 있다.
print(re.match('<.*?>', s).group())


