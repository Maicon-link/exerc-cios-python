# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

n = int (input ('Digite um número:'))
s = n + 1
a = n - 1
print ('O sucessor é {} e o antecessor é {}!' .format (s, a))


#==============================             OU


n = int (input('Digite um valor:'))
print ('Com o valor {}, seu antecessor é {} e seu sucessor é {}!'. format(n, (n-1), (n+1)))