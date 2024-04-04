menu = """
    Olá, seja bem-vindo(a) ao banco, selecione a opção que deseja.
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Verificar saldo
        [5] - Sair

"""

saldo = 0
qnt_saque = 0
limite_diario = 3
depositos = []
saques = []
deposito = 0
print(menu)

while True:
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        valor_deposito = float(input("Qual valor a ser depositado?: R$ "))
        depositos.append(valor_deposito)
        deposito += 1
        saldo += valor_deposito
        print("Depósito realizado!")
    elif opcao == 2:
            if qnt_saque < limite_diario:
                valor_saque = int(input("Qual valor deseja sacar?: R$ "))
                if valor_saque <= saldo and valor_saque <= 500:
                    saques.append(valor_saque)
                    qnt_saque += 1
                    saldo -= valor_saque
                    print("Saque realizado! Aguarde o dinheiro no local indicado.")
                else:
                    print("Você não possui valor suficiente para realizar esse saque ou está tentando sacar um valor acima do permitido R$500.00, tente novamente.")
            else:
                 print("Você excedeu o limite de saque diário, volte amanhã ou selecione outra opção")

    elif opcao == 3:
        print("Seu extrato abaixo!")
        for index, i in enumerate(depositos):
            print(f"Depósito {index + 1} - R$ {i}")

        for index, i in enumerate(saques):
            print(f"Saque {index + 1} - R$ {i}")
        print(f"Saldo final da conta R$ {saldo}")
    elif opcao == 4:
        print(f"Seu saldo é de R$ {saldo}")

    elif opcao == 5:
        print("Obrigado, até a próxima!")
        break

    else:
        print("Opção invalida, tente novamente")
        