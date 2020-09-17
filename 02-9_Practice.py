# Q1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
kor = 80
eng = 75
math = 55
result = (kor + eng + math) / 3
print(result)

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
num = 13
if num % 2 == 0:
    print(True)
else:
    print(False)

# Q3. 홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연월일부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
pin = "881120-1068234"
spl = pin.split('-')
yyyymmdd = spl[0]
num = spl[1]
print(yyyymmdd)
print(num)

# Q4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.
pin = "881120-1068234"
print(pin[7])
if pin[7] == 1:
    print('남자')
else: 
    print('여자')

# Q5. 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6. [1, 3, 5, 4, 2]리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7. ['Life', 'is', 'too', 'short']리스트를 Life is too short문자열로 만들어서 출력해보자.
result = ' '.join(['Life', 'is', 'too', 'short'])
print(result)

# Q8. (1, 2, 3)튜플에 값 4를 추가하여 (1, 2, 3, 4)를 만들어 출력해보자.
a = (1, 2, 3)
a = a + (4, )
print(a)

# Q9. a = dict()라는 딕셔너리가 있다. 다음중 오류가 발생하는 경우를 고르고, 그 이유를 설명해보자.
# (3). a[[1]] = 'python' : key형식이 맞지 않다.(key로는 변하는 값을 사용할 수 없다.)

# Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출해보자.
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# Q11. a 리스트에서 중복되는 숫자를 제거해보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
#      그리고 이런 결과가 나오는 이유에 대해 설명해보자.
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)
print(id(a))
print(id(b))
# a와 b는 같은 주소값을 공유하고 있기 때문에 a의 요소를 변경하면 b의 요소도 변경된다.
