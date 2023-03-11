#ordenação de 12 valores em uma lista
A=[]
for i in range(0,12):
    A.append(int(input('Digite um valor: ')))
for i in range(0,11):
    for j in range(i+1,12):
        if A[i]<A[j]:
            x=A[i]
            A[i]=A[j]
            A[j]=x
for i in range(0,12):
    print (A[i])