# 탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tabContent = f.read()
f.close()

spaceContent = tabContent.replace("\t", " " * 4)
print(spaceContent)
f = open(dst, 'w')
f.write(spaceContent)
f.close()