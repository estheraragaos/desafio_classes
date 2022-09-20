from cartaodecredito import CartaoDeCredito
import random


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

    def criar_cartao_de_credito(self, banco:'Banco') -> bool:
        '''Criar objeto cartao de credito na conta, dados limite e nome do cartão de crédito, chamará metodo de análise de crédito do banco
        para definir limite'''

        nome_do_cartao = 'Mastercard' + str(random.randint(1, 100))
        limite = banco.analisar_credito(self)

        cartao_de_credito = CartaoDeCredito(nome_do_cartao, limite)

        for cartao in self.lista_cartoes_de_credito:
            if cartao_de_credito.nome_cartao == cartao.nome_cartao:
                return False

        self.lista_cartoes_de_credito.append(cartao_de_credito)

        return True


    def pagar_fatura_de_cartao(self, cartao:CartaoDeCredito) -> bool:
        
        valor_fatura = cartao.consultar_valor_fatura()

        if self.saldo >= valor_fatura:

            self.saldo -= valor_fatura

            cartao.limite_atual += valor_fatura

            return True

        return False


    def pagar_boleto(self, valor_boleto:float) -> bool:

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
        
        if self.chave_pix == chave_pix:

            return False 

        self.chave_pix = chave_pix

        return True
