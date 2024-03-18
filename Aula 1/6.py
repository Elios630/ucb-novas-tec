segundos_total = int(input("Digite a quantidade de segundos: "))

dias = (segundos_total//(60*60*24))%60
horas = (segundos_total//(60*60))%24
min = (segundos_total//60)%60
seg =  segundos_total % 60

print(f"{segundos_total} segundos correspondem a:")
print(f"{dias} dias, {horas} horas, {min} minutos e {seg} segundos.")