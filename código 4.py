A = []
B = []
for i in range(0,8): 
    A.append (int(input("Digite um valor: ")))
    B.append (A[i]*3)
for i in range(0,8):
    print (f"{B[i]}")