notas = []
soma = 0
for i in range(0,4):
    notas.append(float(input(f'Nota {i+1}: ')))
    soma+=notas[i]
MD1 = soma/len(notas)
if MD1 >= 7.0:
    print (f'''Aprovado
Média do aluno: {MD1:.2f}''')
else: 
    NE = float(input('Nota do exame: '))
    MD2 = (MD1 + NE)/2
    if MD2 >= 5.0:
        print ('Aprovado em exame')
    else:
        print ('Reprovado')
    print (f'Média do aluno: {MD2:.2f}')
