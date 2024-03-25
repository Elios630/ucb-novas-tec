numero = input("Digite o número de conta n: ")
res =0
for i in range(0,len(numero)):
    res += int(numero[i])
    
while len(numero) !=6:
    numero = '0' + numero
    print(numero)
    
res =res%10
print(f"Número de conta completo: {numero}-{res}")