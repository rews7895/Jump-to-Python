# 정규 표현식 : 복잡한 문자열을 처리할 때 사용하는 기법
# 사용 전
data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"):
    wordResult = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():   # isdigit : 문자열이 숫자인지 아닌지를 True, False로 리턴
            word = word[:6] + "-" + "*******"
        wordResult.append(word)
    result.append(" ".join(wordResult))
print("\n".join(result))

# 사용 후
# re : 정규 표현식 사용을 위한 모듈
import re

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub('\g<1>-*******', data))