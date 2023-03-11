resp = "SIM"
soma_total = 0
while resp == "SIM":
    cômodo = input("Cômodo da casa: ")
    largura = float(input("Largura (em metros): "))
    comprimento = float(input("comprimento (em metros): "))
    área = largura * comprimento
    soma_total += área
    print(f'área do cômodo = {área}M²')
    resp = input("Deseja calcular mais comodos?(sim/não): ").strip().upper()
print (f'área total da casa: {soma_total}M²')