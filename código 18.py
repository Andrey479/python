#porcentagem de n?meros impares em uma lista de 10 elementos
A=[]
impar=0
for i in range(0,10):
    A.append(int(input('Digite um valor: ')))
    if not A[i]%2==0:
        impar+=1
porcentagem=impar*100/len(A)
print (f'Na matriz há: {impar} elementos impares, que correspondem a {porcentagem}% do total de elementos.')