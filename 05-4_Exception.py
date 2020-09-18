# 예외 처리
# try ~ except
"""
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
"""
"""
except구문의 3가지 방법
1. try, except만 쓰는 방법 : 오류 종류에 상관없이 오류가 발생하면 except블록을 수행 
try:
    ...
except:
    ...
2. 발생 오류만 포함한 except문 : 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except블록을 수행
try:
    ...
excecpt 발생오류:
    ...
3. 발생 오류와 오류 메시지 변수까지 포함한 except문 : 2번 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법
try:
    ...
except 발생오류 as 오류 메시지 변수:
    ...
"""
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# try ~ finally : finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행.
# 보통 사용한 리소스를 close해야할 때 많이 사용됨.
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
    print('a')
finally:
    f.close()

# 여러 개의 오류 처리하기 : 여러 개 중 가장 먼저 발생하는 에러에 대해 내용 출력
"""
try:
    ...
except 발생 오류1:
    ...
except 발생 오류2:
    ...    
"""
# 하나씩
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")
# 에러문구를 e로
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
# 에러를 묶어서
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 회피하기 :특정 오류가 발생할 경우 그냥 통과시켜야 할 때
"""
try:
    f = open('나없는파일', 'r')
except FileNotFoundError:
    pass
"""

# 오류 일부러 발생시키기(raise)
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    # pass
    def fly(self):
        print('very fast')

eagle = Eagle()
eagle.fly()

# 예외 만들기 : 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용.
# 내장 클래스인 Exception클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    def __str__(self): #__str__ : print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않는 별명입니다.')
# as e
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)

