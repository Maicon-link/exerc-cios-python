# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
# desconsiderando os espaços.
from time import process_time_ns

# EXEMPLOS:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA


pali = input('Digite uma Frase: ').upper().replace(' ','')

if pali == pali[:: -1]:
    print('A palavra é Palindroma','\n')
    print('Palavra Invertida: {}'.format(pali),'\n')
else:
    print('A palavra não é Palindroma','\n')

print('Palavra Digitada: {} '.format(pali),'\n')


#========================================     OU


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto [letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')





























