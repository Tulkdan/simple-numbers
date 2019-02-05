import unittest
import main

class Test(unittest.TestCase):
  def test_retorna_zero(self):
    self.assertEqual(main.recebeNumero(0), 'zero')

  def test_retorna_vinte_e_um(self):
    self.assertEqual(main.recebeNumero(21), 'vinte e um')

  def test_retorna_vinte_e_nove(self):
    self.assertEqual(main.recebeNumero(29), 'vinte e nove')

  def test_retorna_noventa_e_nove(self):
    self.assertEqual(main.recebeNumero(99), 'noventa e nove')

  def test_retorna_cinquenta_e_seis(self):
    self.assertEqual(main.recebeNumero(56), 'cinquenta e cinco')

  def test_retorna_cento_e_dez(self):
    self.assertEqual(main.recebeNumero(110), 'cento e dez')

'''
  def test_retorna_duzentos_e_vinte_e_cinco(self):
    self.assertEqual(main.recebeNumero(225), 'duzentos e vinte e cinco')

  def test_retorna_quinhentos_e_cinquenta(self):
    self.assertEqual(main.recebeNumero(550), 'quinhentos e cinquenta')

  def test_retorna_novecentos_e_noventa_e_cinco(self):
    self.assertEqual(main.recebeNumero(999), 'novecentos e noventa e cinco')
'''

unittest.main(verbosity=2)
