def normalize(arr):
    diff = []
    diff.append(0)
    first = elephant[0]
    for i in range(1,m):
        diff.append(elephant[i]-first)
    return diff

def match(arr, test, ini, fim):
    diff = []
    diff.append(0)
    first = arr[ini]
    for i in range(ini+1,fim):
        if not ((arr[i]-first)==test[i-ini]):
            return False
    return True

n, m = [int(x) for x in input().split()]
bears = [int(x) for x in input().split()]
elephant = [int(x) for x in input().split()]

test = normalize(elephant)
count = 0
if n>m:
    for i in range(n-m+1):
        if match(bears, test, i, i+m):
            count+=1
print(count)
