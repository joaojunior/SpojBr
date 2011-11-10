class Bolsa(object):
    def __init__(self):
        self.total = 0.00
        self.ordens_venda = []
        self.ordens_compra = []

    def add_ordem(self,tipo,valor):
        if tipo == "V":
            self.ordens_venda.append(valor)
        else:
            self.ordens_compra.append(valor)
        self.calcula_ganho_bolsa()
        
    def calcula_ganho_bolsa(self):
        if(self.exite_ordem_de_compra_e_de_venda()):
            maior_valor_compra = max(self.ordens_compra)
            menor_valor_venda = min(self.ordens_venda)
            diferenca = maior_valor_compra - menor_valor_venda
            if(diferenca >= 0):
                self.total += diferenca 
                self.ordens_venda.remove(menor_valor_venda)
                self.ordens_compra.remove(maior_valor_compra)

    def exite_ordem_de_compra_e_de_venda(self):
        return len(self.ordens_compra) > 0 and len(self.ordens_venda) > 0
        
def main():
    quantidade = int(raw_input())
    while(quantidade != 0):
        bolsa = Bolsa()
        for i in xrange(quantidade):
            ordem = raw_input()
            ordem = ordem.split(" ")
            tipo = ordem[0]
            valor = float(ordem[1])
            bolsa.add_ordem(tipo,valor)
        print bolsa.total
        quantidade = int(raw_input())
if __name__ == "__main__":
    main()