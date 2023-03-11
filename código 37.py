A = int(input("Valor de A: "))
B = int(input("Valor de B: "))
C = int(input("Valor de C: "))
if C>B:
    x = C
    C = B
    B = x
if C>A:
    x = C
    C = A
    A = x
if B>A:
    x = B
    B = A
    A = x
print (A,B,C)
