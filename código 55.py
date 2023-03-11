anterior = 0
atual = 1
i = 1
while i<=15:
    if i==1:
        print (0)
    elif i==2:
        print (1)
    else:
        próximo = atual+anterior
        anterior = atual
        atual = próximo
        print (próximo)
    i+=1