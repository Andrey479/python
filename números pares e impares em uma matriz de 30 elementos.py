#Quantidade números pares e impares em uma matriz de 30 elementos digitados pelo usuário
A=[]
par=0
impar=0
for i in range(0,30):
    A.append(int(input('Digite um valor: ')))
    if A[i]%2==0:
        par+=1
    else:
        impar+=1
print (f'''Exitem: {par} valor(es) par(es) na matriz.
Existem: {impar} valor(es) impar(es) na matriz.''')  