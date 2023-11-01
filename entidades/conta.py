from entidades.cliente import Cliente

class Conta:

    __LIMITE_DE_SAQUE = 3

    def __init__(self, numero, cliente):

        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0.00
        self.movimentacao = ''
        self.__numero_de_saques_realizados = 0

    def depositar(self, valor):

        if type(valor) == float and valor > 0:
            
            if self.movimentacao != '':
                self.movimentacao += f'\n\nSaldo: R$ {self.__saldo:.2f}'
            else:
                self.movimentacao += f'\nSaldo: R$ {self.__saldo:.2f}'

            self.__saldo += valor
            self.movimentacao += f'\n\nDepósito de R$ {valor:.2f} (+)'
            print('### Depósito realizado com sucesso.')
        
        else:
            print('@@@ Não foi possível realizar o depósito.')

    def sacar(self, valor):
        
        if type(valor) == float and valor > 0 and self.__saldo >= valor and self.__numero_de_saques_realizados < Conta.__LIMITE_DE_SAQUE:
            
            if self.movimentacao != '':
                self.movimentacao += f'\n\nSaldo: R$ {self.__saldo:.2f}'
            else:
                self.movimentacao += f'\nSaldo: R$ {self.__saldo:.2f}'

            self.__saldo -= valor
            self.movimentacao += f'\n\nSaque de R$ {valor:.2f} (-)'
            print('### Saque realizado com sucesso.')
            self.__numero_de_saques_realizados += 1

        else:
            print('@@@ Não foi possível realizar o saque.')

    def exibir_extrato(self):

        print(f'Conta Corrente nº {self.numero}\n')
        print('$$$$$$$  EXTRATO  $$$$$$$')
        print(self.movimentacao)
        print(f'\nSaldo Atual: R$ {self.__saldo:.2f}')