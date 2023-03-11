A = []
soma = 0
for i in range (0,10):
    A.append(float(input('Digite um valor: ')))
    soma += A[i]
média = soma/len(A)
print (f"média: {média}")
print (f"soma: {soma}")