#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int (input('Digite um número: '))
x = n * 0
x1 = n * 1
x2 = n * 2
x3 = n * 3
x4 = n * 4
x5 = n * 5
x6 = n * 6
x7 = n * 7
x8 = n * 8
x9 = n * 9
x10 = n * 10                        #               MAIS TRABALHOSO E DESORGANIZADO
print ('{} x 0 = {}'.format (n, x))
print ('{} x 1 = {}'.format (n, x1))
print ('{} x 2 = {}'.format (n, x2))
print ('{} x 3 = {}'.format (n, x3))
print ('{} x 4 = {}'.format (n, x4))
print ('{} x 5 = {}'.format (n, x5))
print ('{} x 6 = {}'.format (n, x6))
print ('{} x 7 = {}'.format (n, x7))
print ('{} x 8 = {}'.format (n, x8))
print ('{} x 9 = {}'.format (n, x9))
print ('{} x 10 = {}'.format (n, x10))

#==========================================              OU

n = int (input('Digite um número: '))
print ('-' *12)
print ('{} x {:2} = {}'.format(n, 0, n*0))
print ('{} x {:2} = {}'.format(n, 1, n*1))
print ('{} x {:2} = {}'.format(n, 2, n*2))
print ('{} x {:2} = {}'.format(n, 3, n*3))        #    MAIS SIMPLES E ORGANIZADO
print ('{} x {:2} = {}'.format(n, 4, n*4))
print ('{} x {:2} = {}'.format(n, 5, n*5))
print ('{} x {:2} = {}'.format(n, 6, n*6))
print ('{} x {:2} = {}'.format(n, 7, n*7))
print ('{} x {:2} = {}'.format(n, 8, n*8))
print ('{} x {:2} = {}'.format(n, 9, n*9))
print ('{} x {:2} = {}'.format(n, 10, n*10))
print ('-' *12)






















