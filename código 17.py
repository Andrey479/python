#12 elementos diviseis por 2 ou 3 e 12 elementos não diviseis por 5.
A=[]
B=[]
C=[]
i=1
while i<=12:
    n=int(input('(Matriz A) Digite um valor: '))
    if n%2==0 or n%3==0:
        A.append(n)
        i+=1
    else:
        print ('Valor inválido!')
print ('-'*30)
i=1
while i<=12:
    n=int(input('(Matriz B) Digite um valor: '))
    if not n%5==0:
        B.append(n)
        i+=1
    else:
        print ('Valor inválido!')
C.extend(A+B)
for i in range(0,24):
    print (C[i])