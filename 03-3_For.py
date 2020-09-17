# for
"""
for 변수 in 리스트(또는 튜플, 문자열)
    수행할 문장1
    수행할 문장2
    ...
"""
# 기본 활용
testList = ['one', 'two', 'three']
for i in testList:
    print(i)
# 응용 활용1
a = ((1, 2), (3, 4), (5, 6))
for (first, last) in a:
    print(first + last)
# 응용 활용2
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")

# for문과 continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")

# for문과 함께 자주 사용되는 range함수
# range: 숫자 리스트를 자동으로 만들어 줌
a = range(10)
print(a)
a = range(1, 11)
print(a)
add = 0
for i in a:
    add = add + i
    print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print(f"{number + 1}번 학생 축하합니다. 합격입니다.")
# for와 range를 사용한 구구단 
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")

# 리스트 내포 사용
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)
# => 리스트 내포
result = [num * 3 for num in a]
print(result)
# 리스트 내포를 사용하여 [1, 2, 3, 4]중에서 짝수에만 3을 곱하여 담기
result = [num * 3 for num in a if num % 2 == 0]
print(result)
# 리스트 내포를 사용하여 구구단의 모든 결과를 리스트에 담기
result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result)

        