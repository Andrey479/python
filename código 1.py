i = 1
teste = True
while teste == True:
    num = int(input("Digite um valor: "))
    if num<0:
        teste = False
    else:
        if i==1:
            maior = num
            menor = num
            i+=1
        else:
            if num>maior:
                maior = num
            if num<menor:
                menor = num
if i==2:
    print (menor)
    print (maior)