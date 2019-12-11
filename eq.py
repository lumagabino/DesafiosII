def split(word): 
    return [char for char in word] 

size = int(input())
a = list(input())
b = list(input())

count = 0
for i in range(size):
    if a[i]!=b[i]:
        if (i+1)<size:
            if a[i+1]!=b[i+1] and a[i]!=a[i+1]:
                a[i] = b[i]
                a[i+1] = b[i+1]
                count+=1
            else:
                a[i] = b[i]
                count+=1
        else:
            a[i] = b[i]
            count+=1
print(count)

        
