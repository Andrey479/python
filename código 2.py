quantidade_exercicios = int(input("Quantidade de exercícios: "))
i = 1
while i<=quantidade_exercicios:
    nome_exercicio = input("Nome do exercício: ")
    reps_exercicio = int(input("Repetições: "))
    peso_exercicio = int(input("Peso executado: "))
    rm = (0.033*reps_exercicio*peso_exercicio)+peso_exercicio
    print (f"1 RM: {round(rm)}Kg")
    resposta = input ("Deseja calcular % sobre esse peso? (sim/não): ").strip().upper()
    if resposta == "SIM":
        porcentagem = int(input("Quantos %: "))
        r = round(rm)*(porcentagem/100)
        print (f"{porcentagem}% = {round(r)}Kg")
    i+=1