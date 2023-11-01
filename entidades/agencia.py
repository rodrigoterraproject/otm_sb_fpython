from entidades.conta import Conta
from entidades.cliente import Cliente

class Agencia:

    def __init__(self, numero):

        self.numero = numero
        self.contas = []

    def abrir_conta(self, numero, cliente):

        if self.localizar_conta(cliente.cpf):
            print('@@@ Conta já cadastrada.')
        
        else:
            nova_conta = Conta(numero, cliente)
            self.contas.append(nova_conta)
            print('### Conta cadastrada com sucesso.')

    def localizar_conta(self, cpf):

        for c in self.contas:
            if c.cliente.cpf == cpf:
                return c
        
        return None