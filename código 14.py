A = []
B = []
for i in range(0,15):
    A.append(float(input('Digite um valor: ')))
    if i%2==0:
        B.append(A[i]/2)
    else:
        B.append(A[i]*1.5)
for i in range(0,15):
    print (B[i])