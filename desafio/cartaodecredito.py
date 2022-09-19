class CartaoDeCredito:


    def __init__(self, nome_cartao:str, limite_total:float):

        self.nome_cartao   = nome_cartao 

        self.limite_cartao = limite_total
        self.limite_atual  = limite_total


    def comprar(self, valor_compra:float) -> bool:
        '''Checar limite, se é possivel realizar a compra, reduzir limite, etc'''
        
        if self.limite_atual >= valor_compra:

            self.limite_atual -= valor_compra
            
            return True

        return False
