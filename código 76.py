import math
A = []
for i in range(0,15):
    A.append(int(input('Digite um valor: ')))
for i in range(0,14):
    for j in range(i+1,15):
        if A[i]>A[j]:
            x = A[i]
            A[i] = A[j]
            A[j] = x
resp = "SIM"
while resp == "SIM":
    pesq = int(input('Valor que deseja procurar: '))
    começo = 0
    final = 14
    acha = False
    while começo<=final and acha == False:
        meio = math.ceil((começo+final)/2)
        if pesq == A[meio]:
            acha = True
        else:
            if pesq < A[meio]:
                final = meio - 1
            else:
                começo = meio + 1
    if acha == True:
        print (f'{pesq} foi localizado na posição: {meio+1}')
    else:
        print (f'{pesq} não foi localizado')        
    resp = input('Deseja continuar? (sim/não): ').strip().upper()