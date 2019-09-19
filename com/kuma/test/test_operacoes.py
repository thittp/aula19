from unittest import TestCase
from com.kuma.operacoes import operacoes


class TestOperacoes(TestCase):
	def setUp(self):
		self.operações = operacoes()
		
	def test_soma(self):
		self.assertEqual(self.operacoes.soma([1,5]), 6, "Deve ser 6")