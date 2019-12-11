n = int(input())

count = 0
row = 1 
numberOfRows = 1

while row*row <= n:
    numberOfRows = row - 1
    count += n//row - numberOfRows
    row += 1

print(count)