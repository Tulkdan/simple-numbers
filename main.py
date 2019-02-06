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
    if num > 0:
      aux += ' e '

  if num / 10 > 1:
    dezena = num // 10
    num = int(((num / 10) - dezena) * 10)
    dezena = dezena * 10
    aux += simpleNumbers[dezena]
    if num > 0:
      aux += ' e '

  if num > 0:
    aux += simpleNumbers[num]

  return aux


# Refatoração da função acima
def recebe_numero_2(num):
  if num in simpleNumbers:
    return simpleNumbers[num]
  
  frase = retorna_centecima(num)
  return frase

def retorna_centecima(num):
  frase = ''
  if num / 100 > 1:
    cent = num // 100
    num = int(((num / 100) - cent) * 100)
    cent = cent * 100
    frase += 'cento' if cent == 100 else simpleNumbers[cent]
    frase += ' e ' if num > 0 else ''
  
  frase += retorna_decimal(num)

  return frase

def retorna_decimal(num):
  frase = ''
  if num / 10 > 1 and num > 0:
    dezena = num // 10
    num = int(((num / 10) - dezena) * 10)
    dezena = dezena * 10
    frase += simpleNumbers[dezena]
    frase += ' e ' if num > 0 else ''

  frase += retorna_resto(num)
  
  return frase

def retorna_resto(num):
  if num in simpleNumbers and num > 0:
    return simpleNumbers[num]
  return ''

