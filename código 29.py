A=[]
B=[]
for i in range(0,30):
    A.append(float(input('Digite um valor: ')))
    B.append(A[i]**3)
resp='SIM'
while resp=='SIM':
    pesq=float(input('Valor que deseja procurar: '))   
    i=0
    acha=False
    while i<=29 and acha==False:
        if pesq==B[i]:
            acha=True
        else:
            i+=1
    if acha==True:
        print (f'{pesq} foi localizado na posição: {i}')
    else:
        print (f'{pesq} não foi localizado')
    resp=input('Deseja continuar? (sim/não): ').strip().upper()