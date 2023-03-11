A = []
B = []
for i in range (0,20):
    A.append(int(input('Digite um valor: ')))
    i2 = 1
    soma = 0
    while i2<=A[i]:
        soma+=i2
        i2+=1
    B.append(soma)
for i in range (0,20):
    print (B[i])