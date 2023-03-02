#número total de elementos pares na lista
A=[]
par=0
for i in range(0,15):
    A.append(int(input('Digite um valor: ')))
    if A[i]%2==0:
        par+=1
print (f'Existem: {par} elementos pares na matriz')