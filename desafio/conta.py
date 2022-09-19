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
