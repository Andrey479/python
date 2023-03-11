suporte1 = "-" * 30
exer = input('Exercicio: ')
reps = int(input("Quantidade de repetições: "))
peso = int(input("Peso usado: "))
rm = (0.033*reps*peso)+peso
pergun = input("Deseja calcular porcentagem sobre o valor de 1RM? (Sim/Não): ").strip().upper() 
if pergun == "SIM":
    suporte2 = "%"
    per = int(input("Quantos %? "))
    rpercento = round(rm)*(per/100)
    print ('''
%s
Exercício: %s
Quantidade de repetições: %d
Peso de execução: %dKg
1RM: %dKg
%d%s de 1RM: %dKg''' % (suporte1, exer,reps,peso,round(rm),per,suporte2,rpercento))
else:
    print ('''
%s
Exercício: %s
Quantidade de repetições: %d
Peso de execução: %dKg
1RM: %dKg''' % (suporte1, exer,reps,peso,round(rm)))