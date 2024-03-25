veses = int(input("Imprima os n primeiros números primos: "))
numero = 0
contador= 0
conf = 0
while contador < veses:
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                conf = 1
        if conf == 0:
            print(f"{numero}")
            contador += 1
    numero +=1
    conf = 0