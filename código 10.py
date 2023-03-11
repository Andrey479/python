A = []
teste = False
n = int(input("Digite um valor: "))
if n>=1 and n<=10:
    for i in range(1,11):
        x=n+i
        A.append(x)
    for i in range(n+1,n+11):
        x=i-n
        A.append(x)
    for i in range(1,11):
        x=n*i
        A.append(x)
    for i in range(1,11):
        x=(i*n)/n
        A.append(x)
    teste = True
else:
    print ("O valor esta fora da faixa permitida.")
if teste==True:
    for i in range(0,40): 
        print (f' {A[i]}')
    