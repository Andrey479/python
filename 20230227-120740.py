#três listas uma com valores pares, outra com valores impares e a terceira com as duas listas
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
