# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

from math import factorial



num = int(input('Digite um número para realizar \nseu fatorial. '))
c = num
f = 1
print('Calculando {}! = '.format(num), end= '')
while c > 0:
    print('{}'.format(c), end= '')
    print( ' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1

print('{}'.format(f))



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OU 




f = 1
num = int(input('Digite um número \nPara calcular seu fatorial!'))
for num in range(1, num, + 1):
    f *= num
print('O fatorial de {} é {}'.format(num, f))














