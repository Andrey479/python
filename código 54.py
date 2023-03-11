A=[]
B=[]
C=[]
for i in range(0,10):
    A.append(int(input('Lista A, Digite um valor: ')))
for i in range(0,10):
    B.append(int(input('Lista B, Digite um valor: ')))
for i in range(0,10):
    C.append((A[i]**2)+(B[i]**2))
for i in range(0,9):
    for j in range(i+1,10):
        if C[i]<C[j]:
            x=C[i]
            C[i]=C[j]
            C[j]=x
for i in range(0,10):
    print (C[i])