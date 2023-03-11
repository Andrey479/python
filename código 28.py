A=[]
B=[]
C=[]
for i in range(0,20):
    A.append(input('Matriz A. Escreva alguma coisa: ').strip().upper())
for i in range(0,30):
    B.append(input('Matriz B. Escreva alguma coisa: ').strip().upper())
C.extend(A+B)
for i in range(0,49):
    for j in range(i+1,50):
        if C[i]<C[j]:
            x=C[i]
            C[i]=C[j]
            C[j]=x
for i in range(0,50):
    print (C[i])