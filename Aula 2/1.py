while True:
    print("\nMenu de Opções:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        num = int(input("Digite um número para ver sua tabuada de adição: "))
        print(f"Tabuada de adição do {num}:")
        for i in range(1, 11):
            print(f"{num} + {i} = {num + i}")

    elif escolha == 2:
        num = int(input("Digite um número para ver sua tabuada de subtração: "))
        print(f"Tabuada de subtração do {num}:")
        for i in range(1, 11):
            print(f"{num} - {i} = {num - i}")

    elif escolha == 3:
        num = int(input("Digite um número para ver sua tabuada de divisão: "))
        print(f"Tabuada de divisão do {num}:")
        for i in range(1, 11):
            print(f"{num} / {i} = {num / i}")
            
    elif escolha == 4:
        num = int(input("Digite um número para ver sua tabuada de multiplicação: "))
        print(f"Tabuada de multiplicação do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    elif escolha == 5:
        break