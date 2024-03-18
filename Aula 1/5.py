import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes são: x' = {x1} e x'' = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"A raiz única é: x = {x}")
else:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(-delta) / (2*a)
    print(f"As raízes são complexas: x' = {parte_real} + {parte_imaginaria}i e x'' = {parte_real} - {parte_imaginaria}i")