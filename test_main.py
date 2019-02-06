import unittest
import main as m

class Test(unittest.TestCase):
  def test_retorna_zero(self):
    self.assertEqual(m.recebeNumero(0), 'zero')

  def test_retorna_vinte_e_um(self):
    self.assertEqual(m.recebeNumero(21), 'vinte e um')

  def test_retorna_vinte_e_nove(self):
    self.assertEqual(m.recebeNumero(29), 'vinte e nove')

  def test_retorna_noventa_e_nove(self):
    self.assertEqual(m.recebeNumero(99), 'noventa e nove')

  def test_retorna_cinquenta_e_seis(self):
    self.assertEqual(m.recebeNumero(56), 'cinquenta e cinco')

  def test_retorna_cem(self):
    self.assertEqual(m.recebeNumero(100), 'cem')

  def test_retorna_cento_e_dez(self):
    self.assertEqual(m.recebeNumero(110), 'cento e dez')

  def test_retorna_duzentos_e_vinte_e_cinco(self):
    self.assertEqual(m.recebeNumero(225), 'duzentos e vinte e cinco')

  def test_retorna_quinhentos_e_cinquenta(self):
    self.assertEqual(m.recebeNumero(550), 'quinhentos e cinquenta')

  def test_retorna_novecentos_e_noventa_e_cinco(self):
    self.assertEqual(m.recebeNumero(999), 'novecentos e noventa e nove')


class TesteRefatoracao(unittest.TestCase):
  def test_retorna_zero(self):
    self.assertEqual(m.recebe_numero_2(0), 'zero')

  def test_retorna_vinte_e_um(self):
    self.assertEqual(m.recebe_numero_2(21), 'vinte e um')

  def test_retorna_vinte_e_nove(self):
    self.assertEqual(m.recebe_numero_2(29), 'vinte e nove')

  def test_retorna_noventa_e_nove(self):
    self.assertEqual(m.recebe_numero_2(99), 'noventa e nove')

  def test_retorna_cinquenta_e_seis(self):
    self.assertEqual(m.recebe_numero_2(56), 'cinquenta e cinco')

  def test_retorna_cem(self):
    self.assertEqual(m.recebe_numero_2(100), 'cem')

  def test_retorna_cento_e_dez(self):
    self.assertEqual(m.recebe_numero_2(110), 'cento e dez')

  def test_retorna_duzentos_e_vinte_e_cinco(self):
    self.assertEqual(m.recebe_numero_2(225), 'duzentos e vinte e cinco')

  def test_retorna_quinhentos_e_cinquenta(self):
    self.assertEqual(m.recebe_numero_2(550), 'quinhentos e cinquenta')

  def test_retorna_novecentos_e_noventa_e_cinco(self):
    self.assertEqual(m.recebe_numero_2(999), 'novecentos e noventa e nove')

unittest.main(verbosity=2)
