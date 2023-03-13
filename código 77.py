import math
A = []
B = []
C = []
D = []
for i in range(0,15):
    A.append(int(input('Lista A, digite um valor: ')))
for i in range(0,15):
    B.append(int(input('Lista B, digite um valor: ')))
for i in range(0,15):
    C.append(int(input('Lista C, digite um valor: ')))
for i in range(0,15):
    D.append(A[i]+B[i]+C[i])
for i in range(0,14):
    for j in range(i+1,15):
        if D[i]>D[j]:
            x = D[i]
            D[i] = D[j]
            D[j] = x
resp = "SIM"
while resp == "SIM":
    pesq = int(input('Valor que deseja procurar: '))
    começo = 0
    final = 14
    acha = False
    while começo<=final and acha == False:
        meio = math.ceil((começo+final)/2)
        if pesq == D[meio]:
            acha = True
        else:
            if pesq < D[meio]:
                final = meio - 1
            else:
                começo = meio + 1
    if acha == True:
        print (f'{pesq} foi localizado na posição: {meio+1}')
    else:
        print (f'{pesq} não foi localizado')        
    resp = input('Deseja continuar? (sim/não): ').strip().upper()