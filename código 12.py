A = []
B = []
for i in range(0,25):
    A.append(float(input('Digite uma temperatura em °C: ')))
    x = (A[i]*9/5)+32
    B.append(x)
for i in range(0,25):
    print (f'{round(A[i],2)}°C - {round(B[i],2)}°f')