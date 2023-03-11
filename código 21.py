#quadrado da soma dos elementos da lista A e B
A=[]
B=[]
C=[]
for i in range(0,10):
    A.append(int(input('(Matriz A) Digite um valor: ')))
for i in range(0,10):
    B.append(int(input('(Matriz B) Digite um valor: ')))
for i in range(0,10):
    C.append((A[i]+B[i])**2)
    print (C[i])