class CartaoDeCredito:

    def __init__(self, nome_cartao:str, limite_total:float):

        self.nome_cartao   = nome_cartao 
        
        self.limite_cartao = limite_total
        self.limite_atual  = limite_total