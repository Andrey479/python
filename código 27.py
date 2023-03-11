A=[]
B=[]
C=[]
for i in range(0,12):
    A.append(float(input('Lista A: Digite um valor: ')))
for i in range(0,11):
    for j in range(i+1,12):
        if A[i]>A[j]:
            x=A[i]
            A[i]=A[j]
            A[j]=x
for i in range(0,12):
    B.append(float(input('Lista B: Digite um valor: ')))
for i in range(0,11):
    for j in range(i+1,12):
        if B[i]>B[j]:
            x=B[i]
            B[i]=B[j]
            B[j]=x
for i in range(0,12):
    C.append(A[i]+B[i])
for i in range(0,11):
    for j in range(i+1,12):
        if C[i]<C[j]:
            x=C[i]
            C[i]=C[j]
            C[j]=x
for i in range(0,12):
    print (C[i])