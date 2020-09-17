# Q1. 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수를 작성해보자.
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(is_odd(2))
# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자.(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))
# Q3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다. 이프로그램을 수행해보고 오류를 수정해보자.
# input1 = int(input("첫번째 숫자를 입력하세요: "))
# input2 = int(input("두번째 숫자를 입력하세요: "))
# total = input1 + input2
# print(f"두 수의 합은 {total}입니다.")
# Q4. 다음중 출력 결과가 다른 것 한 개를 골라 보자.
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
# Q5. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다. 이 프로그램은
#     우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 수정해보자.
f1 = open("test.txt", "w")
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
# Q6. 사용자의 입력을 파일에 저장하는 프로그램을 작성해보자.(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야한다.)
# user_input = input("저장할 내용을 입력하세요: ")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()
# Q7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어서 저장해보자.
f = open('test.txt', 'r')
body = """Life is too short
you need java"""
f.close()
body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()