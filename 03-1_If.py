# if 문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
"""
    비교연산자
    <
    >
    ==
    !=
    >=
    <=
"""
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# or(x or y) : x와 y 둘 중에 하나만 참이면 참
# and(x and y) : x와 y 모두 참이어야 참
# not(not x) : x가 거짓이면 참
money = 2000
card = True
if money >= 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# in, not in : 리스트, 튜플, 문자열에 사용 가능
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else: 
    print('걸어 가라')
# pass
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

# elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

# 조건부 표현식
score = 60
message = "success" if score >= 60 else "failure"
print(message)