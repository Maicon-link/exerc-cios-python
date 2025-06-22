#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int (input('Digite um número:'))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print ('O dobro de {} é {}\nSeu triplo é {} \nE sua raiz quadrada é {:.2f}'.format (n1, d, t, r))


#==============================         OU


n = int (input('Digite um número:'))
print ('O dobro de {} vale {}.'.format (n, (n*2)))
print ('O triplo de {} vale {},\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, n*3, n, n**(1/2)))