A=[]
B=[]
for i in range(0,20):
    A.append(int(input('Digite um valor: ')))
    B.append(A[i]+2)
for i in range(0,19):
    for j in range(i+1,20):
        if B[i]>B[j]:
            x=B[i]
            B[i]=B[j]
            B[j]=x
resp='SIM'
while resp=='SIM':
    pesq=int(input('Valor que deseja procurar: '))
    começo=0
    final=20
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