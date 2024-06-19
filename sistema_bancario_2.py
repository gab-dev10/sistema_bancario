def menu():
    menu = """\n
    ======= MENU =======
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova conta
    [l] Listar contas
    [u] Novo usuário
    [q] Sair
    => """
    return input(menu)

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Não é possível depositar valores menores que 1 Real")
    
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor inserido é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ===== EXTRATO =====")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario  = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco": endereco})

    print("Usuário cadastrado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("usuario não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:{conta['agencia']}
        C/C:{conta['numero_conta']}
        Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True: 
        opcao = menu()

        if opcao == "d":
            print("Depósito...")
            valor_deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            criar_usuario(usuarios)
        
        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "l":
            listar_contas(contas)   
        
        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()