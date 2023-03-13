import math
A = []
for i in range(0,10):
    A.append(input('Digite uma palavra: ').strip().upper())
for i in range(0,9):
    for j in range(i+1,10):
        if A[i]>A[j]:
            x = A[i]
            A[i] = A[j]
            A[j] = x
print ('---'*15)
resp = "SIM"
while resp == "SIM":
    pesq = input('Palavra que deseja procurar: ').strip().upper()
    começo = 0
    final = 9
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