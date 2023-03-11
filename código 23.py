#duas listas uma com valores pares e outra com valores impares
A=[]
B=[]
C=[]
for i in range(0,12):
    n=int(input('Digite um número: '))
    if n%2==0:
        A.append(n)
    else:
        B.append(n)
C.extend(A+B)
for i in range(0,len(C)):
    print (C[i])