numero = int(input("Digite um número inteiro para verificar se é primo: "))
falso = 0
if numero <= 1:
    print(f"{numero} não é um número primo.")

for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        print(f"{numero} não é um número primo.")
        falso = 1
    
if falso!=1:
    print(f"{numero} é um número primo.")