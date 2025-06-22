# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo e mostre o comprimento da hipotenusa.

import math


co = float (input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


#============================       OU


co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co **2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
