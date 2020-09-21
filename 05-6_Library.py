# 외장 함수
# $python test.py abc pey guido
# sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
# sys.exit() : 강제로 스크립트 종료

# pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# 어떤 자료형이든 저장하고 불러올 수 있다.
# ex) dump함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법
import pickle
f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close

# os : 환경 변수나 디렉터리, 파일 등의 os자원을 제어할 수 있게 해주는 모듈
import os
# os.environ : 내 시스템의 환경 변수 값을 알고 싶을 때
print(os.environ)
print(os.environ['PATH'])
# os.chdir : 디렉터리 위치 변경

# print(os.chdir("/home/junseok/pythonProjects"))

# os.getcwd() : 디렉터리 위치 돌려받기
print(os.getcwd())

# os.system : 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수 있다.
os.system("dir")
# 실행한 시스템 명령어의 결괏값 돌려받기
f = os.popen("dir")
print(f.read())
"""
os.mkdir : 디렉터리를 생성한다.
os.rmdir : 디렉터리를 삭제한다. (단 비어있을 때)
os.unlink : 파일을 지운다.
os.rename(src, dst) : src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""

# shutil : 파일을 복사해 주는 파이썬 모듈
import shutil
# shutil.copy(복사할 파일, 복사한 파일)
shutil.copy('test.txt', 'dst.txt')

# glob : 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때
import glob
# glob.glob(pathname) : 디렉터리에 있는 파일들을 리스트로 만들기
print(glob.glob("/home/junseok/pythonProjects/Jump-to-Python"))

# tempfile : 파일을 임시로 만들어서 사용할 때 사용하는 모듈
import tempfile
# tempfile.mktemp() : 중복되지 않는 임시 파일을 무작위로 만들어서 돌려준다.
# s3와 같이 다른 곳에 저장할 때 사용가능한지 확인 필요
filename = tempfile.mktemp()
print(filename)

# time : 시간과 관련된 time 모듈
import time
# time.time : UTC를 사용하여 현재시간을 실수 형태로 돌려주는 함수
print(time.time())

# time.localtime : 연도, 월, 일, 시, 분, 초의 형태로 바꾸어 주는 함수
print(time.localtime(time.time()))

# time.asctime : 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려준다.
print(time.asctime(time.localtime(time.time())))

# time.ctime : 현재 시간만을 돌려준다.
print(time.ctime())

# time.strftime : 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷코드를 제공
"""
%a : 요일 줄임말
%A : 요일
%b : 달 줄임말
%B : 달
%c : 날짜와 시간을 출력
%d : 날
%H : 시간(24)
%I : 시간(12)
%j : 1년 중 누적 날짜
%m : 달
%M : 분
%p : AM or PM
%S : 초
%U : 1년 중 누적 주(일요일을 시작으로)
%w : 숫자로 된 요일
%W : 1년 중 누적 주(월요일을 시작으로)
%x : 현재 설정된 지역에 기반한 날짜 출력
%X : 현재 설정된 지역에 기반한 시간 출력
%Y : 연도 출력
%Z : 시간대 출력
%% : 문자
%y : 세기 부분을 제외한 연도 출력
"""
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# time.sleep : 주로 루프 안에서 많이 사용. 일정한 시간 간격을 두고 루프를 실행할 수 있다.
# for i in range(1, 11):
#     print(i)
#     time.sleep(1)

# calender : 달력을 볼 수 있게 해주는 모듈
import calendar
# calender.calender(연도) : 그 해 전체 달력을 볼 수 있다.
# print(calendar.calendar(2020))
# print(calendar.prcal(2020))
# prmonth : 월
print(calendar.prmonth(2020, 12))
# weekday : 날짜에 해당하는 요일 정보 리턴 0 : 월 ~ 6 : 일
print(calendar.weekday(2020, 9, 21))
# monthrange : 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 튜플 형태로 돌려준다.
print(calendar.monthrange(2020, 8))

# random : 난수 발생
import random
# 0.0 ~ 1.0 사이 실수 중 난수
print(random.random())
# 1 ~ 10 정수
print(random.randint(1, 10))

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

# shuffle : 리스트의 항목을 무작위로 섞고 싶을 때
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

# webbrowser : 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
import webbrowser
webbrowser.open("https://google.com")

# threading
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task) # 스레드 생성
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

print("End")





