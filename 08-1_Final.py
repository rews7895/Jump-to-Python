# Q1. 문자열 바꾸기
string = 'a:b:c:d'
li = string.split(':')
print('#'.join(li))

# Q2. 딕셔너리 값 추출하기
li = {'A': 90, 'B': 80}
li.get('C', 70)

# Q3. 리스트 더하기와 extend 함수
a = [1, 2, 3]
a = a + [4, 5]
b = [1, 2, 3]
b.extend([4, 5])
print(id(a))
print(id(b))

# Q4. 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark

print(result)

# Q5. 피보나치 함수
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 2) + fib(n - 1)

for i in range(10):
    print(fib(i))

# Q6. 숫자의 총합 구하기
userInput = input('숫자를 입력하세요: ')
numbers = userInput.split(',')
total = 0
for n in numbers:
    total += int(n)
print(total)

# Q7. 한 줄 구구단
userInput = input('구구단을 출력할 숫자를 입력하세요(2~9): ')
dan = int(userInput)
for i in range(1, 10):
    print(i*dan, end= ' ')

# Q8. 역순 저장
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

# Q9. 평균값 구하기
f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)
f = open('result.txt', 'w')
f.write(str(average))
f.close()

# Q10. 사칙연산 계산기
class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def add(self):
        result = 0
        for num in self.numberList:
            result += num
        return result
    def avg(self):
        total = self.add()
        return total / len(self.numberList)

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.add())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.add())
print(cal2.avg())

# Q11. 모듈 사용 방법
# import sys
# sys.path.append('/')
# import mymod

# Q12. 오류와 예외 처리
# 7이 출력됨

# Q13. DashInsert 함수
data = '4546793'

numbers = list(map(int, data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers) -1:
        isOdd = num % 2 == 1
        isNextOdd = numbers[i + 1] % 2 == 1
        if isOdd and isNextOdd:
            result.append('-')
        elif not isOdd and not isNextOdd:
            result.append('*')

print(''.join(result))

# Q14. 문자열 압축하기
def compressString(s):
    _c = ''
    cnt = 0
    result = ''
    for c in s:
        if c != _c:
            _c = cif cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compressString("aaabbccccca"))

# Q15. Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10
print(chkDupNum("0123456789"))

# Q16. 모스 부호 해독
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

# Q17. 기초 메타 문자
import re

p = re.compile("a[.]{3,}b")

print(p.match("acccb"))
print(p.match("a....b"))
print(p.match("aaab"))
print(p.match("a.cccb"))

# Q18. 문자열 검색
p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end())

# Q19. 그루핑
# 전화번호 패턴
s = """
park 010-9999-9988
kim 0110-9909-7789
lee 010-8789-7768
"""
pat = re.compile("\d{3}[-]\d{4}[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)

# Q20. 전방 탐색
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))