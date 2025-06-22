# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 - Para binário          2 - Para octal          3 - Para hexadecimal

import math

número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[  1  ] converter em BINÁRIO
[  2  ] converter em OCTAL
[  3  ] converter para HEXADECIMAL''')
opção = int(input('Qual será a base de conversão? '))
if opção == 1:
     print('O número {} em binário é igual a {}'.format(número, bin(número)))
if opção == 2:
     print('O número {} em octal é igual a {}'.format(número, oct(número)))
elif opção == 3:
    print('O número {} em hexadecimal é {}'.format(número, hex(número)))
else:
    print('Opção inválida, Tente novamente.')



