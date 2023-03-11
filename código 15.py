A = []
B = []
C = []
D = []
for i in range(0,6):
    A.append(int(input('Digite um valor: ')))
    if i%2==0:
        D.append(A[i])
    else:
        C.append(A[i])
for i in range(0,6):
    B.append(int(input('Digite um valor: ')))
    if i%2==0:
        D.append(B[i])
    else:
        C.append(B[i])
for i in range(0,6):
    print (f'{C[i]}----{D[i]}')