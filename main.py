simpleNumbers = {
  0: 'zero',
  1: 'um',
  2: 'dois',
  3: 'três',
  4: 'quatro',
  5: 'cinco',
  6: 'seis',
  7: 'sete',
  8: 'oito',
  9: 'nove',
  10: 'dez',
  11: 'onze',
  12: 'doze',
  13: 'treze',
  14: 'quatorze',
  15: 'quinze',
  16: 'dezesseis',
  17: 'dezessete',
  18: 'dezoito',
  19: 'dezenove',
  20: 'vinte',
  30: 'trinta',
  40: 'quarenta',
  50: 'cinquenta',
  60: 'sessenta',
  70: 'setenta',
  80: 'oitenta',
  90: 'noventa',
  100: 'cem',
  200: 'duzentos',
  300: 'trezentos',
  400: 'quatrocentos',
  500: 'quinhentos',
  600: 'seiscentos',
  700: 'setessentos',
  800: 'oitocentos',
  900: 'novecentos'
}

def recebeNumero(num):
  if num in simpleNumbers:
    return simpleNumbers[num]

  aux = ''

  if num / 100 > 1:
    cent = num // 100
    num = int(((num / 100) - cent) * 100)
    cent = cent * 100
    aux += 'cento' if cent == 100 else simpleNumbers[cent]
    aux += ' e '

  if num / 10 > 1:
    dezena = num // 10
    num = int(((num / 10) - dezena) * 10)
    dezena = dezena * 10
    aux += simpleNumbers[dezena]
    aux += ' e '

  aux += simpleNumbers[num]

  return aux

def recebe_numero_2(num):
  if num in simpleNumbers:
    return simpleNumbers[num]
  
  aux = retorna_centecima(num)
  return aux

def retorna_centecima(num):
  aux = ''
  if num / 100 > 1:
    cent = num // 100
    cent = cent * 100
    aux += 'cento' if cent == 100 else simpleNumbers[cent]
    aux += ' e '
  
  aux += retorna_decimal(int(((num / 100) - cent) * 100))

  return aux

def retorna_decimal(num):
  aux = ''
  if num / 10 > 1:
    dezena = num // 10
    dezena = dezena * 10
    aux += simpleNumbers[dezena]
    aux += ' e '

  aux += retorna_resto(int(((num / 10) - dezena) * 10))
  
  return aux

def retorna_resto(num):
  if num in simpleNumbers
    return simpleNumbers[num]
  return ''

