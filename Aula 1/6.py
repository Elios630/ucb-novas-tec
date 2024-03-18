num = int(input("Entre o numero de segundos"))

dia = (num//(60*60*24))%60
horas = (num//(60*60))%24
min = (num//60)%60
seg =  num % 60

print(f"Dias={dia}, horas={horas}, minutos={min}, segundos={seg}")