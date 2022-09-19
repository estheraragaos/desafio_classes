from conta import Conta

class Banco:

    def __init__(self, nome_banco: str):

        self.nome = nome_banco

        self.lista_clientes = list()

    def cadastrar_cliente(self, nome: str, cpf: str, senha: str, renda: float, chave_pix: str, saldo: float) -> bool:
        '''Criar um objeto conta dado nome, cpf, senha e renda'''
      
        for conta in self.lista_clientes:

            if conta.cpf == cpf:

                return False

        self.lista_clientes.append(
            Conta(nome, cpf, senha, renda, chave_pix, saldo)
            )

        return True

    def acessar_conta(self, cpf: str, senha: str) -> Conta:
        '''Dado um cpf e senha, procurar a conta na lista de clientes e retornar a conta'''

        for conta in self.lista_clientes:

            if conta.cpf == cpf and conta.senha == senha:

                return conta

        return None

    def analisar_credito(self, conta: Conta) -> float:
        '''Dada renda de uma conta, definir regras que retornem um limite adequado para o cliente'''

        for cliente in self.lista_clientes:

            if cliente == conta:

                return cliente.renda * 3

        return False
