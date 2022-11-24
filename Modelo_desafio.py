menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
depositos = 0
saldo = 1500 
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Infome o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito feito no valor de R$ {valor:.2f}\n"

        else:
            print("O valor informado e invalido, tentei inserir outro valor!")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Atenção você não possui saldo suficiente para realizar essa operação!")

        elif excedeu_limite:
            print("Atenção! O valor do saque excedeu o seu limite, procure seu gerente!")

        elif excedeu_saques:
            print("Atenção! o numero de saques foi excedido, voce não pode realizar mais saques hoje!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor informado invalido!") 

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizada movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação invalida! Por favor selecione novamente a operação desejada.")