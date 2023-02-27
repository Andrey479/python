i = 0
teste = True
soma = 0
while teste == True: 
    n = float(input("Digite um valor: "))
    if not n<0:
        soma+=n
        i+=1
    else:
        teste = False
média = soma/i
print ("Total de números lidos = %d"%i)
print ("Soma total: ")
print (soma)
print ("média: ")
print (média)