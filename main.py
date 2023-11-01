from entidades.banco import Banco
from entidades.agencia import Agencia
from entidades.cliente import Cliente
from entidades.conta import Conta

MENU_PRINCIPAL = [
    '[B] ->\tAcesso Banco',
    '[C] ->\tAcesso Conta',
    '[S] ->\tSair',
]

MENU_BANCO = [
    '[C] ->\tCadastrar Cliente',
    '[A] ->\tAbrir Conta Corrente',
    '[V]  ->\tVoltar',
]

MENU_CONTA = [
    '[D] ->\tDepositar',
    '[S] ->\tSacar',
    '[E] ->\tExtrato',
    '[V] ->\tVoltar',
]

def exibir_menu(menu):
    print()
    for item in menu:
        print(item)

if __name__ == '__main__':

    nome_do_banco = input('\nDigite o nome do seu banco: ')
    banco = Banco(nome_do_banco)

    numero_da_agencia = '0001'
    agencia = Agencia(numero_da_agencia)
    banco.agencias.append(agencia)

    opcao = ''

    while opcao != 'S':

        exibir_menu(MENU_PRINCIPAL)
        opcao = input('\nDigite a opção desejada: ').strip().upper()

        if opcao == 'B':

            while opcao != 'V':

                exibir_menu(MENU_BANCO)
                opcao = input('\nDigite a opção desejada: ').strip().upper()

                if opcao == 'C':
                    
                    cpf = input('\nDigite o CPF: ')
                    nome = input('Digite o nome completo: ')
                    data_de_nascimento = input('Digite a data de nascimento: ')

                    print()
                    banco.cadastrar_cliente(cpf, nome, data_de_nascimento)

                elif opcao == 'A':

                    cpf = input('\nDigite o CPF: ')

                    cliente = banco.localizar_cliente(cpf)

                    if cliente:

                        numero_da_conta = f'{str(len(agencia.contas) + 1).zfill(7)}'
                        agencia = banco.localizar_agencia(numero_da_agencia)

                        print()
                        agencia.abrir_conta(numero_da_conta, cliente)

                    else:

                        print('\n@@@ Cliente não localizado.')


                elif opcao != 'V':
                   
                    print('\n@@@ Opção inválida!')

        elif opcao == 'C':

            cpf = input('\nDigite o CPF do titular: ')
            conta = agencia.localizar_conta(cpf)

            if not conta:
                print('\n@@@ Conta não localizada.')
                continue

            while opcao != 'V':

                exibir_menu(MENU_CONTA)
                opcao = input('\nDigite a opção desejada: ').strip().upper()

                if opcao == 'D':
                    
                    valor = input('\nDigite o valor do depósito: R$ ')

                    print()

                    try:
                        conta.depositar(float(valor))
                    except:
                        print('@@@ Depósito não realizado.')

                elif opcao == 'S':
                    
                    valor = input('\nDigite o valor do saque: R$ ')

                    print()

                    try:
                        conta.sacar(float(valor))
                    except:
                        print('@@@ Saque não realizado.')

                elif opcao == 'E':
                    
                    print(f'\n{banco.nome}\n')
                    
                    print(f'Cliente: {conta.cliente.nome}\n')
                    print(f'CPF nº {conta.cliente.cpf}\n')

                    print(f'Agência nº {agencia.numero}\n')

                    conta.exibir_extrato()

                elif opcao != 'V':
                    
                     print('\n@@@ Opção inválida!')
        
        elif opcao != 'S':

            print('\n@@@ Opção inválida!')

        else:

            print('\nAcesso encerrado.\n')



