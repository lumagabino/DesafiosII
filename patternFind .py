import re

t = int(input())

for i in range(t):
    string, p = [str(x) for x in input().split()]
    indices = [m.start()+1 for m in re.finditer(p, string)]

    size = len(indices)
    if size>0:
        print(size)
        print(*indices)
    else:
        print()
        print("Not Found")