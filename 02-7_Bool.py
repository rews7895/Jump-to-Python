# 불 자료형
"""
 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다. 
"""
a = True
b = False
print(type(a))
print(type(b))
print(1 == 1)
print(2 > 1)
print(2 < 1)

a = [1, 2, 3, 4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

# bool 내장함수
print(bool('python'))
print(bool(''))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(0))
print(bool(3))