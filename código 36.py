A = float(input('Valor de A: '))
B = float(input('Valor de B: '))
C = float(input('Valor de C: '))
if A==0 or B==0 or C==0:
    print ('Um dos valores é inválido.(dica: Insira um número diferente de zero)')
else:
    DELTA = B**2-4*A*C
    if DELTA < 0:
        print ('Não há solução real.')
    elif DELTA == 0:
        X=(-B+(DELTA**(1/2)))/(2*A)
        print (f'As duas raizes iguais são: {X:.2f}')
    else:
        X1=(-B+(DELTA**(1/2)))/(2*A)
        X2=(-B-(DELTA**(1/2)))/(2*A)
        print (f'X1: {X1:.2f} e X2: {X2:.2f}')
    print (f'∆ = {DELTA}')
    




