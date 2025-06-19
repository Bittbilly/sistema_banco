print("agradeçemos a sua preferência e confiança em nosso banco!")

menu = """
seja bem vindo, por favor ecolha uma opção:

   [1] DEPOSITAR
   [2] SACAR
   [3] CONSULTAR SALDO
   [4] SAIR
     """

saldo = 0 
saque = 0
extrato = ""
SAQUE_MAXIMO = 500
LIMITE_SAQUES = 3
numero_saques = 0


while True:
    opcao = input(menu)
# opção de deposito
    if opcao == "1":
        valor = float(input("digite o valor que deseja depositar:"))
       
        if valor > 0 :
            saldo += valor
            extrato += f"deposito: R$ {valor}\n"
            print("depósito realizado com sucesso!\n")
            print(f"Seu saldo atual é: R$ {saldo}")

        elif valor <= 0:
            print("valor inválido, por favor tente novamente.")
            
# opção de saque 
    elif opcao == "2":
        saque = float(input("Digite o valor desejado para saque: "))

        if saque > saldo:
            print("Seu saldo é insuficiente para efetuar o saque!")

        elif saque > SAQUE_MAXIMO:
            print(f"O valor máximo por saque é R$ {SAQUE_MAXIMO:.2f}")

        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de {LIMITE_SAQUES} saques diários atingido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            print(f"Seu saldo atual é: R$ {saldo:.2f}")

        else:
            print("Valor de saque inválido!")
    


    # Consultar saldo
    elif opcao == "3":
        print(f"Seu saldo é: R$ {saldo}")
        print("Extrato:")
        print(extrato if extrato else "Nenhuma movimentação realizada.")

    else:
        print("Obrigado por utilizar nossos serviços!")
        break

