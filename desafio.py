

menu = """
(1) Depósito
(2) Saque
(3) Extrato
(0) Sair

R: """

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

while True:
    print("\n================= MENU =================")
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeuSaldo = valor > saldo
        excedeuLimite = valor > limite
        excedeuSaques = numeroSaques >= limiteSaques

        if excedeuSaldo:
            print("Erro! Você não tem saldo suficiente.")
        
        elif excedeuLimite:
            print("Erro! O valor do saque excede o limite.")

        elif excedeuSaques:
            print("Erro! Númeo máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeroSaques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Erro! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "0":
        print("================== FIM ==================")
        break
    
    else:
        print("Erro! Por favor selecione novamente a operação desejada.")
        


