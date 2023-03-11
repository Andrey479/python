A = []
B = []
N = 0
while N<10:
    x = int(input('Digite um valor: '))
    if x>=0:
        A.append (x)
        B.append (A[N]-A[N]*2)
        N+=1
    else:
        print ('O valor está fora da faixa permitida. Escreva apenas valores positivos.')
for i in range(0,10):
    print (f'{A[i]}...{B[i]}')