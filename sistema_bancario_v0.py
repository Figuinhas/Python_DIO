def menu():
    menu = """
        Olá, seja bem-vindo(a) ao banco, selecione a opção que deseja.
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Novo usuário
            [5] - Nova conta
            [6] - Listar Contas
            [7] - Sair
            Digite sua opção: 
            
            """
    return int(input(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Depósito realizado!")

    else: 
        print("!!! Operação não realizada, valor inválido, tente novamente !!!")

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, qnt_saque, limite_diario):
     excedeu_saldo = valor_saque > saldo
     excedeu_limite = valor_saque > limite
     excedeu_saques = qnt_saque > limite_diario

     if excedeu_saldo:
          print("!!! Operação falhou, você não possui saldo o suficiente.!!!")

     elif excedeu_limite:
          print("!!! Operação falhou, valor excede o limite permitido (R$ 500,00!!!")

     elif excedeu_saques:
          print("!!! Operação falhou, você excedeu o numero de saques permitidos (3)!!!")

     elif valor_saque > 0:
          saldo -= valor_saque 
          extrato += f"Saque: R$ {valor_saque:.2f}\n"
          print("Saque realizado com sucesso!")
          print(qnt_saque)

     else:
          print("!!! Operação falho, valor invalido.!!!")

     return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n----------EXTRATO----------")
    if not extrato:
        print("Não foram realizadas movementações.")
    else:
        print(extrato)
        print(F"\nSaldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somento números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("!!! !!! Já existe usuário cadastrado com esse CPF")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf , "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("!!! Usuário não encontrado, criação da conta encerrada. !!!")    

def listar_contas(lista_contas):
    for conta in lista_contas:
        linha = f"""
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular; {conta["usuario"]["nome"]}
"""
        print("-" * 100)
        print(linha) 

def main():
    agencia = "0001"
    saldo = 0
    limite = 500
    qnt_saque = 0
    limite_diario = 3
    extrato = ""
    usuarios = []
    lista_contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor_deposito = float(input("Qual valor a ser depositado?: R$ "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

            #depositos.append(valor_deposito)
            
        elif opcao == 2:
            valor_saque = int(input("Qual valor deseja sacar?: R$ "))
            qnt_saque += 1
            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                qnt_saque=qnt_saque,
                limite_diario=limite_diario,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(lista_contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                lista_contas.append(conta)

        elif opcao == 6:
            listar_contas(lista_contas)

        elif opcao == 7:
            break

main()
