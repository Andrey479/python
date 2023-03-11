nome = []
for i in range (0,10):
    nome.append (str(input(f"{i+1}°Nome: ")))
print ("-" * 30)
for i in range (0,10):
    print (f"{nome[i]}")