from entidades.cliente import Cliente
from entidades.agencia import Agencia

class Banco:

    def __init__(self, nome):

        self.nome = nome
        self.clientes = []
        self.agencias = []

    def cadastrar_cliente(self, cpf, nome, data_de_nascimento):
        
        if self.localizar_cliente(cpf):
            print('@@@ Cliente já cadastrado.')

        else:
            novo_cliente = Cliente(cpf, nome, data_de_nascimento)
            self.clientes.append(novo_cliente)
            print('### Cliente cadastrado com sucesso.')
    
    def localizar_cliente(self, cpf):

        for c in self.clientes:
            if c.cpf == cpf:
                return c
            
        return None
    
    def abrir_agencia(self, numero):

        if self.localizar_agencia(numero):
            print('@@@ Agência já cadastrada.')

        else:
            nova_agencia = Agencia(numero)
            self.agencias.append(nova_agencia)
            print('### Agência cadastrada com sucesso.')

    def localizar_agencia(self, numero):

        for a in self.agencias:
            if a.numero == numero:
                return a
        
        return None