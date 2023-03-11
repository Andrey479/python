A=[]
B=[]
for i in range(0,15):
    A.append(int(input('Digite um valor: ')))
for i in range(0,15):
    contador=1
    fatorial=1
    while contador<=A[i]:
        fatorial*=contador
        contador+=1
    B.append(fatorial)
for i in range(0,14):
    for j in range(i+1,15):
        if B[i]>B[j]:
            x=B[i]
            B[i]=B[j]
            B[j]=x
for i in range(0,15):
    print(B[i])