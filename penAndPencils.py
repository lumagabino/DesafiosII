import math
testCase = int(input())

for i in range(testCase):
    a, b, c, d, k = [int(x) for x in input().split()]
    item1 = math.ceil(a/c)
    item2 = math.ceil(b/d)

    if item1+item2 <= k:
        print(item1, item2)
    else:
        print(-1)