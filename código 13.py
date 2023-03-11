A = []
B = []
for i in range(0,12):
    A.append(int(input('Digite um valor: ')))
    if A[i]%2==1:
        B.append(A[i]*2)
    else:
        B.append (A[i])
for i in range(0,12):
    print (B[i])