n = int(input())
string  = "hackerrank"

for i in range(n):
    word = str(input())
    j = 0

    for i in word:
        if string[j] == i:
            j+=1

        if j==10:
            break
    
    if j==10:
        print("YES")
    else:
        print("NO")