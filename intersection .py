a1, b1, c1 = [int(x) for x in input().split()]
a2, b2, c2 = [int(x) for x in input().split()]

det = (a1*b2) - (a2*b1)
res = 1


if (a1 == 0 and b1 == 0) and (a2 == 0 and b2 == 0) and c1 != c2:
    res = 0
elif (a1 == 0 and b1 == 0 and c1 == 0) or (a2 == 0 and b2 == 0 and c2 == 0):
    res = -1
elif (a1 == 0 and b1 == 0 and c1 != 0) or (a2 == 0 and b2 == 0 and c2 != 0) and (c1==c2):
    res = 0
elif ((a1*b2)==(b1*a2) and (a1*c2)==(a2*c1) and (b1*c2)==(b2*c1)):
    res = -1
elif det == 0:
    res = 0

print(res)
