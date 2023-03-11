dividendo = float(input("Valor dividendo: "))
divisor = float(input("Valor divisor: "))
divi = dividendo
i = 0
while divi >= divisor:
    divi-=divisor
    i+=1
print (f"{dividendo}/{divisor} = {i}, sobra {divi}")
