a = str(input())
b = str(input())

lenA = len(a)+1
lenB = len(b)+1

matrix = [[0 for x in range(lenA)] for y in range(lenB)]

for i in range(1,lenB):
    for j in range(1,lenA):
        if a[j-1] != b[i-1]:
            maxElem = max(matrix[i-1][j], matrix[i][j-1])
            matrix[i][j] = maxElem
        else:
            matrix[i][j] = matrix[i-1][j-1] + 1

print(matrix[lenB-1][lenA-1])
