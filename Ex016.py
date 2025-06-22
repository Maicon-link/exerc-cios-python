# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#EXEMPLO: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math

from math import trunc

num = float(input('Digite um número: '))
i = math.trunc(num)
print ('O número {} tem a função inteira de {}'.format(num, math.trunc(num)))


#===============================            OU

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))



#===============================            OU

num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
