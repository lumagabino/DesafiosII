# Tem um jeito de chegar por substring em um intervalo

n = int(input())

for i in range(n):
    digits = input()

    if digits == '1' or digits == '4' or digits == '78':
        print("+")
    
    elif digits[len(digits)-2] == '3' and digits[len(digits)-1] == '5':
        print("-")

    elif digits[0] == '1' and digits[1] == '9' and digits[2] == '0':
        print("?")
    
    else:
        print("*")