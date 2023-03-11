A=[]
B=[]
i=0
while i<20:
    n=int(input('Digite um valor negativo: '))
    if n<0:
        A.append(n)
        B.append(A[i]*(-1))
        i+=1
    else:
        print ('Valor inválido')
for i in range(0,19):
    for j in range(i+1,20):
        if B[i]<B[j]:
            x=B[i]
            B[i]=B[j]
            B[j]=x
for i in range(0,20):
    print (B[i])