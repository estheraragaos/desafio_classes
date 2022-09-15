class CartaoDeCredito:

    def __init__(self, nome_cartao:str, limite_total:float):

        self.nome_cartao   = nome_cartao
        
        self.limite_cartao = limite_total
        self.limite_atual  = limite_total

    def comprar(self, valor_compra:float) -> bool:

        if self.limite_atual >= valor_compra:

           self.limite_atual -= valor_compra
           
           return True

        return False
    

    def consultar_valor_fatura(self):
        
        return self.limite_cartao - self.limite_atual


    def pagar_fatura(self, conta:Conta) -> bool:
        
        valor_fatura = self.limite_cartao - self.limite_atual

        if conta.saldo >= valor_fatura:

          conta.saldo -= valor_fatura 

          return True

        return False
        


class Conta:

    def __init__(self, nome:str, cpf:str, senha:str, renda:float, chave_pix:str, saldo:float):
        '''Terá atributos do usuário como:'''

        self.nome      = nome
        self.cpf       = cpf
        self.senha     = senha
        self.renda     = renda
        self.chave_pix = chave_pix
        self.saldo     = saldo

        self.lista_cartoes_de_credito = list()

    def criar_cartao_de_credito(self) -> CartaoDeCredito:
        '''Criar objeto cartao de credito na conta, dados limite e nome do cartão de crédito, chamará metodo de análise de crédito do banco
        para definir limite'''
        pass


    def pagar_boleto(self) -> bool:

        print('Digite o código de barras referente ao boleto:')
        cod_barras = input()
        
        print('Digite o valor do boleto:')
        valor_boleto = input()

        if self.saldo >= valor_boleto:

          self.saldo -= valor_boleto

          return True

        return False


    def sacar_dinheiro(self, qtd:float) -> bool:

        if self.saldo >= qtd:

          self.saldo -=  qtd

          return True

        return False


    def depositar_dinheiro(self, qtd:float) -> bool:
        
        self.saldo += qtd

        return True
  

    def criar_alterar_chave_pix(self, chave_pix:str) -> bool:
        
        if self.chave_pix != chave_pix:

          self.chave_pix = chave_pix

          return True 

        return False

    def fazer_pix(self, chave_pix_destino:str, qtd:float, banco_destino:Banco) -> bool:

    if self.saldo >= qtd:
      for cliente in banco_destino.lista_clientes:
        if chave_pix_destino in cliente.chave_pix:

          self.saldo -= qtd
          cliente.saldo += qtd

          return True

    return False
    
    def exibir_info(self):

            return {
            'nome': self.nome,
            'cpf': self.cpf,
            'senha': self.senha,
            'renda': self.renda,
            'chave_pix': self.chave_pix,
            'saldo': self.saldo
        }

    def exibir_cpf(self) -> str:

        return self.cpf

    def exibir_senha(self) -> str:

        return self.senha

    def exibir_renda(self):

        return self.renda



class Banco:

    def __init__(self, nome_banco: str):

        self.nome = nome_banco

        self.lista_clientes = list()

    def cadastrar_cliente(self, nome: str, cpf: str, senha: str, renda: float, chave_pix: str, saldo: float) -> bool:
        '''Criar um objeto conta dado nome, cpf, senha e renda'''
        
        for conta in self.lista_clientes:

            if conta.exibir_cpf() == cpf:

                return False

        self.lista_clientes.append(
            Conta(nome, cpf, senha, renda, chave_pix, saldo)
            )

        return True

    def acessar_conta(self, cpf: str, senha: str) -> Conta:
        '''Dado um cpf e senha, procurar a conta na lista de clientes e retornar a conta'''

        for conta in self.lista_clientes:

            if conta.exibir_cpf() == cpf and conta.exibir_senha() == senha:

                return conta.exibir_info()

        return False
        

    def analisar_credito(self, conta: Conta) -> float:
        '''Dada renda de uma conta, definir regras que retornem um limite adequado para o cliente'''

        for cliente in self.lista_clientes:

            if cliente.exibir_cpf() == conta:

                return cliente.exibir_renda() * 3

        return False
