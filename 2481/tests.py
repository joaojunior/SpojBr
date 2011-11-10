import unittest

from spojbr2481 import Bolsa

class TestBolsa(unittest.TestCase):
    def test1AcaoVenda_Maior_AcaoCompra_ganho_0(self):
        bolsa = Bolsa()
        bolsa.add_ordem("C",2.00)
        bolsa.add_ordem("C",3.00)
        bolsa.add_ordem("V",3.50)
        self.assertEqual(0.00,bolsa.total)

    def test2AcaoVenda_Maior_AcaoCompra_ganho_0(self):
        bolsa = Bolsa()
        bolsa.add_ordem("C",2.00)
        bolsa.add_ordem("C",3.00)
        bolsa.add_ordem("V",3.50)
        bolsa.add_ordem("V",4.00)
        self.assertEqual(0.00,bolsa.total)
        
    def testAcaoCompra_Maior_AcaoVenda_ganho_50_centavos(self):
        bolsa = Bolsa()
        bolsa.add_ordem("C",2.00)
        bolsa.add_ordem("C",3.00)
        bolsa.add_ordem("V",3.50)
        bolsa.add_ordem("V",4.00)
        bolsa.add_ordem("V",2.50)
        self.assertEqual(0.50,bolsa.total)
        
        
    def testAcaoCompra_Maior_AcaoVenda_ganho_1e50(self):
        bolsa = Bolsa()
        bolsa.add_ordem("C",2.00)
        bolsa.add_ordem("C",3.00)
        bolsa.add_ordem("V",3.50)
        bolsa.add_ordem("V",4.00)
        bolsa.add_ordem("V",2.50)
        bolsa.add_ordem("C",4.50)
        self.assertEqual(1.50,bolsa.total)

if __name__ == "__main__":
    unittest.main()