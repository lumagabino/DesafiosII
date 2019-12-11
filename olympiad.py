import itertools

count=0
n,l,r,x = raw_input().split(" ")

n = int(n)
l = long(l)
r = long(r)
x = long(x)

array = []
array2 = []
array2 = raw_input().split(" ")
for el in array2:
    array.append(int(el))

array.sort()

for L in range(2, len(array)+1):
    for subset in itertools.combinations(array, L):
        if sum(map(long,subset)) >= l and\
            sum(map(long,subset)) <= r and\
            max(subset)-min(subset) >= x:
                count+=1

# print count