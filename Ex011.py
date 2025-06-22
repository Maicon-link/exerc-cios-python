#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m**2.

l = float (input('Largura:'))
s = float (input('Altura:'))
a = (l * s)
t = a / 2
print ('Com uma dimensão de {}x{} \nMedindo uma área de {}m²\n'
       'Seria necessário {}L de tinta para pintar a parede!'.format(l, s, a, t ))
