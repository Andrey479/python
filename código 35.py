notas = []
soma = 0
for i in range(0,4):
    notas.append(float(input(f'Nota {i+1}: ')))
    soma+=notas[i]
NG = soma/len(notas)
if NG >= 5.0:
    print ('Aprovado')
else:
    print ('Reprovado')
print (f'Média do aluno: {NG:.2f}')





