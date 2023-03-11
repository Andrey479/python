A = []
B = []
for i in range(0,15):
    A.append (int(input(f'{i + 1}° Valor: ')))
    B.append (A[i]**2)
for i in range(0,15):
    print (f'{A[i]} ** 2 = {B[i]}')