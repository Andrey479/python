A = []
B = []
C = []
for i in range (0,15):
    A.append (int(input(f'{i+1}° Digite um valor: ')))
    C.append (A[i])
for i in range (0,15):
    B.append (int(input(f'{i+1}° Digite um valor: ')))
    C.append (B[i])
for i in range (0,30):
    print (f'{C[i]}')