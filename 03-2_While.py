# while
"""
while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
    ...
"""
# exam1
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무 넘어갑니다.")

# exam2
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

