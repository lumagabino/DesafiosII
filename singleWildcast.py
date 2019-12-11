n, m = [int(x) for x in input().split()]
s = str(input())
t = str(input())

result = "YES"

for i in range(n):
    if n > m:
        result = "NO"
        break
    if s[i]=='*':
        break
    if s[i]!=t[i]:
        result = "NO"
        break

if s[i]=='*':
    for j in range(n, i):
        if s[j]!=t[j]:
            result = "NO"
            break

print(result)


