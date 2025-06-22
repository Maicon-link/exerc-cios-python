#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float (input('Preço do produto: R$'))
d = p * 0.05
n = p - d
print ('O valor do produto com desconto de 5% é R${:.2f}!'.format(n))


#===========================================            OU

Preço = float (input('Preço do produto: R$'))
print ('Com o desconto de 5% \nSeu produto de R${:.2f} '
       '\nFica com o valor de R${:.2f}!'.format(Preço, Preço - (Preço * 0.05)))
