import unittest
from mocker import Mocker

from spoj1734 import ordena,calculaAlunoAprovado

class TestOrdenacao(unittest.TestCase):
    def test_ordenacao_com_4_nomes(self):
        lista = [("cardonha",9),("infelizreprovado",3),("marcel",9),("infelizaprovado",3)]
        resultado = [("infelizreprovado",3),("infelizaprovado",3),("marcel",9),("cardonha",9)]
        self.assertListEqual(resultado,ordena(lista))
        
    def test_ordenacao_com_2_nomes(self):
        lista = [("cardonha",9),("marcel",9)]
        resultado = [("marcel",9),("cardonha",9)]
        self.assertListEqual(resultado,ordena(lista))
        
        
class TestCalculaAlunoAprovado(unittest.TestCase):
    def test_calcula_aluno_aprovado_com_uma_instancia(self):
        self.assertEqual("infelizreprovado",calculaAlunoAprovado([("cardonha",9),("infelizreprovado",3),("marcel",9),("infelizaprovado",3)]))
        
    def test_calcula_aluno_aprovado_com_uma_instancia_letra_maiscula(self):
        self.assertEqual("jb",calculaAlunoAprovado([("ja",9),("jb",9)]))
        
if __name__ == "__main__":
    unittest.main()
    