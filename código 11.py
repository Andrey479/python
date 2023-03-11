A=[]
soma=0
for i in range(0,20):
    A.append(float(input('Digite uma temperatura: ')))
    if i==0:
        ma=A[i]
        me=A[i]
    else:
        if A[i]>ma:
            ma=A[i]
        if A[i]<me:
            me=A[i]
    soma+=A[i]
média=soma/len(A)
print (f'Maior temperatura: {ma}°')
print (f'Menor temperatura: {me}°')
print (f'Temperatura média: {round(média,2)}°')   