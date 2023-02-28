
A=[]
B=[]
C=[]
i=1
while i<=10:
    n=int(input('(Matriz A) Digite um número: '))
    if n%2==0 and n%3==0:
        A.append(n)
        i+=1
    else:
        print('Valor inválido.')
i=1
while i<=10:
    n=int(input('(Matriz B) Digite um número: '))
    if n%5==0:
        B.append(n)
        i+=1
    else:
        print('Valor inválido.')
C.extend(A+B)
for i in range(0,20):
    print(C[i])     