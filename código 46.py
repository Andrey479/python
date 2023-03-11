n=int(input("Digite um número: "))
for i in range (1,11):
    print (f'{n} + {i} = {n+i}')
for i in range (n+1,n+11):
    print (f'{i} - {n} = {i-n}')
for i in range (1,11):
    print (f"{n} * {i} = {n*i}")
for i in range (1,11):
    print (f'{n*i} / {n} = {(n*i)/n}')
