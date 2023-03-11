A = []
B = []
C = []
for i in range (0,10):
    A.append (float(input("Valor A: ")))
    B.append (float(input("Valor B: ")))
    C.append (A[i] - B[i])
for i in range (0,10):
    print (f'{A[i]} - {B[i]} = {round(C[i],3)}')