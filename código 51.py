BASE = -1
EXPO = -1
while BASE<0 or EXPO<0:
    print ("escreva apenas valores inteiros e maiores ou iguais a zero.")
    EXPO = int(input("Expoente: "))
    BASE = int(input("Base: "))
i = 0
while i<=EXPO:
    print (f'{BASE}^{i}: {BASE**i}')
    i+=1
