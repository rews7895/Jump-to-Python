# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print(result)