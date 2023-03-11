A = []
B = []
for i in range(0,20):
    A.append(float(input("Digite um valor: ")))
for i in range (19,-1,-1):
    B.append(A[i])
for i in range (0,20):
    print (f'Lista A = {A[i]} e Matriz B = {B[i]}')