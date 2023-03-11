A = []
B = []
C = []
for i in range(0,12):
    A.append(float(input('Lista A, Digite um valor: ')))
for i in range(0,12):
    B.append(float(input('Lista B, Digite um valor: ')))
for i in range(0,12):
    C.append (A[i]*B[i])
resp = "SIM"
while resp == "SIM":
    pesq = float(input('Procure um valor: '))
    i = 0
    acha = False
    while i<12 and acha == False:
        if pesq == C[i]:
            acha = True
        else:
            i+=1
    if acha == True:
        print (f"{pesq} foi localizado na posição: {i+1}")
    else:
        print (f'{pesq} não foi localizado')
    resp = input('Deseja continar? (sim/não): ').strip().upper()