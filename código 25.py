#Pesquisa binária de elementos de uma lista de 8 elementos
#Os elementos da matriz B são os elementos da matriz A * 5
#Assim sendo se vc inserir o valor 5 na matriz A, a matriz B possuirá o valor 25
A=[]
B=[]
for i in range(0,8):
    A.append(int(input('Digite um valor: ')))
for i in range(0,8):
    B.append(A[i]*5)
for i in range(0,7):
    for j in range(i+1,8):
        if B[i]>B[j]:
            x=B[i]
            B[i]=B[j]
            B[j]=x
resp='SIM'
while resp=='SIM':
    pesq=int(input('Valor que deseja procurar: '))
    começo=0
    final=8
    acha=False
    while começo<=final and acha==False:
        meio=int((começo+final)/2)
        if pesq==B[meio]:
            acha=True
        else:
            if pesq<B[meio]:
                final=meio-1
            else:
                começo=meio+1
    if acha==True:
        print(f"{pesq} foi localizado na posição {meio}")
    else:
        print(f'{pesq} não foi localizado')
    resp=input('deseja continuar?(sim/não): ').strip().upper();