# 튜플 자료형
# 특징 : (), 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
# 따라서 프로그램이 실행되는 동안 그 값이 변하지 않기를 바라는 값에 사용하면 된다.

t1 = ()
# 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 붙여야 한다.
t2 = (1, )
t3 = (1, 2, 3)
# 괄호 생략 가능
t4 = 1, 2, 3
print(t4)
t5 = ('a', 'b', ('ab', 'cd'))

# 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 슬라이싱
print(t1[1:])

# 튜플 더하기
t2 = (3, 4)
print(t1 + t2)

# 튜플 곱하기
print(t2 * 3)

# 튜플 길이 구하기
print(len(t1))