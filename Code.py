# Funções do sistema bancário

def criar_usuario(usuarios, nome, cpf):
    if cpf in usuarios:
        print("Usuário já cadastrado.")
        return False
    usuarios[cpf] = nome
    print(f"Usuário {nome} criado com sucesso.")
    return True

def criar_conta_corrente(contas, cpf):
    if cpf not in contas:
        contas[cpf] = {"saldo": 0, "extrato": "", "numero_saques": 0}
        print("Conta corrente criada com sucesso.")
    else:
        print("Conta já existe.")

def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(conta, valor):
    limite = 500
    LIMITE_SAQUES = 3

    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def visualizar_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Menu e interação com o usuário

usuarios = {}
contas = {}

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[n] Criar Conta Corrente
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        cpf = input("Informe o CPF do usuário: ")
        valor = float(input("Informe o valor do depósito: "))
        if cpf in contas:
            depositar(contas[cpf], valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "s":
        cpf = input("Informe o CPF do usuário: ")
        valor = float(input("Informe o valor do saque: "))
        if cpf in contas:
            sacar(contas[cpf], valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "e":
        cpf = input("Informe o CPF do usuário: ")
        if cpf in contas:
            visualizar_extrato(contas[cpf])
        else:
            print("Conta não encontrada.")

    elif opcao == "c":
        nome = input("Informe o nome do usuário: ")
        cpf = input("Informe o CPF do usuário: ")
        criar_usuario(usuarios, nome, cpf)

    elif opcao == "n":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta_corrente(contas, cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
