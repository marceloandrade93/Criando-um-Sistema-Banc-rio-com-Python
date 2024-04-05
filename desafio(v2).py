import textwrap

def menu():  #OK
    menu = """\n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor,extrato, /):  #OK
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso! ")
    else:
        print("\n Operação falhou! O valor informado é inválido. ")
    
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):  #OK
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeroSaques > limiteSaques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente. ")
    
    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excedeu o limite. ")

    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido. ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numeroSaques += 1
        print("\n Saque realizado com sucesso! ")
    
    else:
        print("\n Operação falhou! O valor informado é inválido. ")

    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):  #OK
    print("\n================= MENU =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================")

def criarUsuario(usuarios):  # OK
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtartUsuarios(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF")
        return
    
    nome = input("Informe o cnome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso! ")

def filtartUsuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarConta(agencia, numeroConta, usuarios):  #OK
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtartUsuarios(cpf, usuarios)

    if usuario:
        print("\n Conta Criada com sucesso! ")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}

    print("\n Usuário não encontrato, fluxo de criação de conta encerrado! ")

def listarContas(contas):  #OK
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numeroConta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():  #OK
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":  #OK
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato, = depositar(saldo, valor, extrato)

        elif opcao == "s":  #OK
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaques=numeroSaques,
                limiteSaques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":  #OK
            exibirExtrato(saldo, extrato=extrato)

        elif opcao == "nu":  #OK
            criarUsuario(usuarios)
        
        elif opcao == "nc":  #OK
            numero_conta = len(contas) + 1
            conta = criarConta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":  #OK
            listarContas(contas)

        elif opcao == "q":  #OK
            break

        else:  #OK
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()