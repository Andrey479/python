i = 0
teste = True
soma = 0
média = 0
while teste == True: 
    n = float(input("Digite um valor: "))
    if not n<0:
        soma+=n
        i+=1
    else:
        teste = False
if soma>0:
    média = soma/i
print (f"Total de números lidos: {i}")
print (f"Soma total: {soma}")
print (f"média: {round(média,2)}")