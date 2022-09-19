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
