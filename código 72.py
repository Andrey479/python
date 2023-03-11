A = []
B = []
for i in range (0,15):
    A.append (int(input("Digite um valor: ")))
    i2 = 1
    x1 = 1
    while i2<=A[i]:
        x1*=i2
        i2+=1
    B.append (x1)
for i in range(0,15):
    print (f'{A[i]}!: {B[i]}')