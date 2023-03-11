#os elementos de indice par na lista A, atribuem a B, um elemento de índice impar
A=[]
B=[]
for i in range (0,6):
    A.append(float(input('Digite um valor: ')))
for i in range(0,6):
    if i%2==0:
        B.append(A[i+1])
    else:
        B.append(A[i-1])
    print (A[i], B[i])