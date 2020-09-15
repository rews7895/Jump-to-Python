# 리스트 자료형 
a = []
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
d = [1, 2, 'Life', 'is']
e = [1, 2, ["Life", "is"]]

a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
# -1번째 인덱스는 문자열에서와 마찬가지로 리스트의 마지막 요솟값을 말함.
print(a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

# 슬라이싱(문자열 나누기)
a = [1, 2, 3, 4, 5]
print(a[0:2])

# 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 리스트 반복하기(*)
a = [1, 2, 3]
print(a * 3)

# 리스트 길이 구하기
print(len(a))

# 만약 문자열과 더하고 싶을 때는
print(str(a[2]) + "hi")

# 리스트 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# 리스트 값 삭제하기
a = [1, 2, 3]
del a[1]
print(a)
# 여러개 삭제하기
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# 리스트에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)
# append는 하나만!
#a.append(7, 8)
#print(a)

# 리스트 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)
b = ['a', 'c', 'b']
b.sort()
print(b)
c = ['가', '라', '다', '나']
c.sort()
print(c)

# 리스트 뒤집기
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 위치 반환 : 원하는 값을 검색하여 있으면 위치 index를 리턴
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# 없으면 ValueError
#print(a.index(5))

# 리스트에 요소 삽입
a = [1, 2, 3]
a.insert(0, 4) # 0번 index에 4를 삽입
print(a)
a.insert(3, 5)
print(a)

# 리스트 요소 삭제 : 요소가 중복되게 있다면 가장 앞 쪽에 있는 것을 삭제한다.
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# 리스트 요소 끄집어내기
a = [1, 2, 3]
print(a.pop())
# 그냥 pop()을 쓰면 맨 마지막 것을 삭제
print(a)
# pop(index)를 지정하면 해당 요소를 삭제
a = [1, 2, 3]
print(a.pop(1))
print(a)

# 리스트에 포함도니 요소 x의 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장 : extend(x)에서 x에는 리스트만 올 수 있으며 원래의 리스트에 x리스트를 더하게 된다
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
a += [8, 9]
print(a)

