# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

soma = 0
cont = 0
for num in range(1, 7):
   d = int(input('Digite o {}º valor: '.format(num)))
   if d % 2 == 0:
       soma += d
       cont += 1
print('Você informou {} números PARES e a soma entre eles é  {}'.format(cont, soma))