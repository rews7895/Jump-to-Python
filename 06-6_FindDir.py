# 하위 디렉터리 검색하기
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            fullFilename = os.path.join(dirname, filename)
            if os.path.isdir(fullFilename):
                search(fullFilename)
            else:
                ext = os.path.splitext(fullFilename)[-1]
                if ext == '.py':
                    print(fullFilename)
    except PermissionError:
        pass

search('/')

# 하위 디렉터리 검색을 쉽게 해주는 os.walk
for (path, dir, files) in os.walk('/'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print('%s/%s' % (path, filename))