
testCase = int(input())


for i in range(testCase):
    str1 = str(input())
    str2 = str (input())

    set1 = set(str1)
    set2 = set(str2)

    if set1.intersection(set2):
        print("YES")
    else:
        print("NO")