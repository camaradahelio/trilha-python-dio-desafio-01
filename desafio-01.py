LIMITE_NUMERO_SAQUES = 3

MENU = """

[c] Cadastrar Cliente
[a] Abrir Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

clientes = []

def listar_clientes():
    print(clientes)

def gerar_numero_conta():
    total_contas = 0

    for cliente in clientes:
        for conta in cliente[cpf]["contas"]:
            total_contas += 1

    print(f"Total de contas: {total_contas}")

    return str(total_contas)

def buscar_cliente(cpf):
    cliente_selecionado = None

    for cliente in clientes:
        if cpf in cliente:
          cliente_selecionado = cliente
          break

    if cliente_selecionado is None:
        print("Cliente não encontrado. Cadastre o cliente antes de criar uma conta.")
        return
    
    return cliente_selecionado

def buscar_conta(cliente_selecionado, numero_conta):
    conta_selecionada = None

    for conta in cliente_selecionado[cpf]["contas"]:
        if numero_conta in conta:
            conta_selecionada = conta
            break 

    if conta_selecionada is None:
        print("Conta não encontrada.")
        return
    
    return conta_selecionada

def cadastrar_cliente(nome, cpf, data_nascimento, endereco):

    for cliente in clientes:
        if cpf in cliente:
          print("Cliente já cadastrado.")
          return

    cliente = { cpf : {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
            "contas": []
        }
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")

def cadastrar_conta(agencia, numero_conta, cpf):

    cliente_selecionado = buscar_cliente(cpf)    

    conta = { numero_conta: {
            "agencia": agencia,
            "saldo": 0,
            "numero_saques": 0,
            "historico": []
        }
    }   

    cliente_selecionado[cpf]["contas"].append(conta)
    print("Conta cadastrada com sucesso.")

def sacar(cpf, numero_conta, valor):   

    cliente_selecionado = buscar_cliente(cpf)    

    conta_selecionada = buscar_conta(cliente_selecionado, numero_conta)    
    
    if valor > conta_selecionada[numero_conta]["saldo"]:
        print("Saldo insuficiente.")
        return
    
    if conta_selecionada[numero_conta]["numero_saques"] >= LIMITE_NUMERO_SAQUES:
        print("Limite de saques diários atingido.")
        return
    
    conta_selecionada[numero_conta]["saldo"] -= valor
    conta_selecionada[numero_conta]["numero_saques"] += 1
    conta_selecionada[numero_conta]["historico"].append(f"Saque: R$ {valor:.2f}")
    print("Saque realizado com sucesso.")

    exibir_extrato(cpf, numero_conta)

def depositar(cpf, numero_conta, valor):   

    cliente_selecionado = buscar_cliente(cpf)
    
    conta_selecionada = buscar_conta(cliente_selecionado, numero_conta)   
    
    if valor <= 0:
        print("Valor de depósito inválido.")
        return
    
    conta_selecionada[numero_conta]["saldo"] += valor
    conta_selecionada[numero_conta]["historico"].append(f"Depósito: R$ {valor:.2f}")
    print("Depósito realizado com sucesso.")

    exibir_extrato(cpf, numero_conta)

def exibir_extrato(cpf, numero_conta):   

    cliente_selecionado = buscar_cliente(cpf)
    
    conta_selecionada = buscar_conta(cliente_selecionado, numero_conta)    
    
    print("\n================ EXTRATO ================")
    if not conta_selecionada[numero_conta]["historico"]:
        print("Não foram realizadas movimentações.")
    else:
        for item in conta_selecionada[numero_conta]["historico"]:
            print(item)
    print(f"\nSaldo: R$ {conta_selecionada[numero_conta]['saldo']:.2f}")
    print("==========================================")

while True:

    opcao = input(MENU)

    if opcao == "c":
        nome = input("Informe o nome do cliente: ")
        cpf = input("Informe o CPF do cliente: ")
        data_nascimento = input("Informe a data de nascimento do cliente (DD/MM/AAAA): ")
        endereco = input("Informe o endereço do cliente: ")
        cadastrar_cliente(nome, cpf, data_nascimento, endereco)

    elif opcao == "l":
        listar_clientes()

    elif opcao == "a":
        agencia = "0001"
        numero_conta = gerar_numero_conta()
        cpf = input("Informe o CPF do cliente: ")
        cadastrar_conta(agencia, numero_conta, cpf)

    elif opcao == "d":
        cpf = input("Informe o CPF do cliente: ")
        numero_conta = input("Informe o número da conta: ")
        valor = float(input("Informe o valor do depósito: "))
        depositar(cpf, numero_conta, valor)        

    elif opcao == "s":
        cpf = input("Informe o CPF do cliente: ")
        numero_conta = input("Informe o número da conta: ")
        valor = float(input("Informe o valor do saque: "))
        sacar(cpf, numero_conta, valor)        

    elif opcao == "e":
        cpf = input("Informe o CPF do cliente: ")
        numero_conta = input("Informe o número da conta: ")
        exibir_extrato(cpf, numero_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")