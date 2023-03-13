A = []
B = []
for i in range(0,10):
    A.append(input('Digite: ').strip().casefold().capitalize())
for i in range(9,-1,-1):
    B.append (A[i])
for i in range(0,9):
    for j in range(i+1,10):
        if B[i]>B[j]:
            x = B[i]
            B[i] = B[j]
            B[j] = x
print ('---'*10)
for i in range(0,10):
    print (B[i])