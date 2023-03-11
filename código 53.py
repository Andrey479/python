A = []
B = []
C = []
D = []
E = []
for i in range(0,15):
    A.append(int(input('Lista A, Digite um valor: ')))
    somatório = 0
    contador = 0
    while contador <= A[i]:
        somatório += contador
        contador += 1
    C.append(somatório)
for i in range(0,15):
    B.append(int(input('Lista B, Digite um valor: ')))
    fatorial = 1
    contador = 1
    while contador <= B[i]: 
        fatorial *= contador
        contador += 1
    D.append(fatorial)
for i in range (0,len(C)):
    E.append (C[i]-D[i]) 
for i in range (0,len(A)):
    E.append (A[i]+B[i])
for i in range(0,29):
    for j in range(i+1,30):
        if E[i]>E[j]:
            x = E[i]
            E[i] = E[j]
            E[j] = x
for i in range(0,30):
    print (E[i])