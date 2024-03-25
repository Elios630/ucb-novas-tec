num = int(input("Digite um numero: "))

res=1

for i in range(1,num+1):
    res=res*i
    
print(f"Seu fatorial: {res}")