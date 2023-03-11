A = []
B = []
C = []
D = []
for i in range(0,15):
    A.append(float(input('Lista A, Digite um valor: ')))
for i in range(0,15):
    B.append(float(input('Lista B, Digite um valor: ')))
for i in range(0,15):
    C.append(float(input('Lista C, Digite um valor: ')))
for i in range(0,15):
    D.append((A[i]+B[i]+C[i])**3)
for i in range (0,14):
    for j in range(i+1,15):
        if D[i]>D[j]:
            x = D[i]
            D[i] = D[j]
            D[j] = x
for i in range(0,15):
    print (D[i])