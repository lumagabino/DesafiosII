# Tem jeito de fazer direto com o join

names = input()
list = []

list.append(names[0])
for i in range(0,len(names)):
    if names[i] == '-':
        list.append(names[i+1])


print(''.join(list))