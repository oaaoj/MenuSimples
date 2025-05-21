menu = """
====================
Selecione a operação
====================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair 
====================
> """

balance = 0
limit = 500
extract = ""
numbers_out = 0
LIMIT_OUT = 3

while True:
    option = input(menu)

    if option == "1":
        value = float(input("Digite o valor a ser depositado:\n"))
        if value > 0:
                balance += value
                extract += f"Depósito de: R$ {value:.2f}\n"
        else:
                print("Operação falhou! O valor informado não é válido")
                     
    elif option == "2":
        value = float(input("Digite um valor a ser sacado:\n"))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_out = numbers_out > LIMIT_OUT

        if exceeded_balance:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif exceeded_limit:
            print("Operação falhou! O valor excedeu o limite disponível para saques.")
        elif exceeded_out:
            print("Operação falhou! O limite de saques foi excedido")
        
        elif value > 0:
            balance -= value
            extract += f"Saque de: R$ {value:.2f}\n"
            numbers_out += 1
        else:
            print("Operação falhou! O valor informado não é válido.")    

    elif option == "3":
        print("\n================ Extrato ================")
        print("Não foi realizada nenhuma operação." if not extract else extract)
        print(f"Seu saldo é: R${balance: .2f}")
        print("=========================================")

    elif option == "4":
        break

    else:
        print("Opção inválida. Tente novamente.")