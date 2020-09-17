# 사용자 입력과 출력
# input
# a = input()
# print(a)
# number = input("숫자를 입력하세요: ")
# print(number)

# print
# ,를 안붙이면 띄어쓰지 않음
print("Life" "is" "too short")
# ,를 쓰면 띄어씀
print("Life", "is", "too short")
# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end = ' ')
print("")

# 파일 생성
# 파일 객체 = open(파일이름, 파일 열기 모드)
# r = 읽기 모드
# w = 쓰기 모드
# a = 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용
# 디렉토리는 없으면 만들어야 함. 안그러면 에러남!
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
# readline : 한 줄 출력
f = open('새파일.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
# readlines : 모든 줄을 리스트로 돌려준다.
f = open('새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# read
f = open('새파일.txt', 'r')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가(a)
f = open('새파일.txt', 'a')
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

# with : 파일을 열고 닫는 것을 자동으로 처리
with open('새파일.txt', 'a') as f:
    f.write("Life is too short, you need python")