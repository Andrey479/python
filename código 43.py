NOME = input ("Digite seu nome: ")
SEXO = input ("Digite seu sexo (M/F): ").strip().upper()
if SEXO == "M":
    print (f"Ilmo Sr. {NOME}")
elif SEXO == "F":
    print (f"Ilma Sra. {NOME}")
else:
    print ("Sexo informado inválido")


