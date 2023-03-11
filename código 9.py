A = []
B = []
for i in range(0,10):
    A.append(int(input('Digite um valor: ')))
    B.append(A[i]/2)
for i in range (0,10):
    print (f'{A[i]}::{B[i]}')