# 딕셔너리 자료형
# Dictionary = Hash
# key : value형식
dic = {'name': 'Junseok', 'phone': '01011111111', 'birth': '1118'}
a = {1: 'hi'}
a = {'a': [1, 2, 3]}

# 딕셔너리 추가
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'Junseok'
print(a)
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제
del a[1]
print(a)

# key를 사용해 value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])
a = {1: 'a', 2: 'b'}

# 주의사항
# key는 고유한 값이므로 중복되는 값을 설정해 놓으면 하나를 제외한 나머지는 무시된다.
a = {1: 'a', 1: 'b'}
print(a)

# key list
a = {'name': 'pey', 'phone': '01111111111', 'birth': '1118'}
# dic.keys() -> dict_keys([])형태로 반환
print(a.keys())
for k in a.keys():
    print(k)
# list로 변환
print(list(a.keys()))

# value list
print(a.values())

# key, value 쌍 얻기(tuple형태로 리턴)
print(a.items())

# key로 vaule 얻기
print(a.get('name'))
print(a.get('phone'))
# key로 검색하여 없으면 None리턴
print(a.get('address'))

# dictionary key로 검색하여 value값이 없을 경우 디폴트 값 세팅
print(a.get('foo', 'bar'))

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in a)
print('email' in a)

# key: value 쌍 모두 지우기
a.clear()
print(a)