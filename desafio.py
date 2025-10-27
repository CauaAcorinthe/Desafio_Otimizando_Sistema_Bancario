menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[lc] Listar Contas
[q] Sair

=> """

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def ver_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def saque(*, valor, saldo, limite, extrato, LIMITE_SAQUES, numero_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques

def filtro_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        
        
        
def criar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtro_usuario(cpf,usuarios)
    if usuario:
        print("\n Já existe um Usuário com esse CPF!")
        return
    

    nome = input("Digite o seu nome:")
    data_nascimento = input("Digite sua data de nascimento:")
    
    endereco = {}
    endereco["logradouro"] = input("Digite seu logradouro: ")
    endereco["numero"] = input("Digite seu número: ")
    endereco["bairro"] = input("Digite seu bairro: ")
    endereco["cidade/estado"] = input("Digite sua cidade e a sigla do estado: ")
    print("=====Seu usuario foi criado=====")
    
    usuarios.append({"Nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})
    return usuarios
    
    
contas = []
usuarios = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)   #positional only


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque( valor = valor, saldo=saldo, limite=limite, extrato=extrato, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques)

    elif opcao == "e":
        ver_extrato(saldo, extrato= extrato)

    elif opcao == "u":
        criar_usuario(usuarios)
           
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")