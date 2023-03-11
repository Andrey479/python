import math
A=[]
B=[]
for i in range(0,15):
    A.append(int(input('Digite um valor: ')))
    B.append(math.ceil(A[i]/2))
for i in range(0,14):
    for j in range(i+1,15):
        if A[i]<A[j]:
            x=A[i]
            A[i]=A[j]
            A[j]=x
for i in range(0,14):
    for j in range(i+1,15):
        if B[i]>B[j]:
            x=B[i]
            B[i]=B[j]
            B[j]=x
for i in range(0,15):
    print (A[i],B[i])