def distict(i):
    digitsList = []
    while i > 0:
        div = i%10
        i = i//10
        if div not in digitsList:
            digitsList.append(div)
        else:
            return False
    return True


l, r = [int(x) for x in input().split()]

result = -1
for i in range(l,r+1):
    if distict(i):
        result = i
        break

print(result)

