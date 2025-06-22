# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
from time import sleep

d = float(input('Qual a distância em Km? '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))
if d >= 200:
    p = d * 0.45
    print('Sua viagem vai custar R${:.2f}'.format(p))
else:
    p = d * 0.50
    print('Sua viagem vai custar R${:.2f}'.format(p))
print('Vai ser Débito ou Crédito? ')
(sleep(3))
print('Obrigado, Boa viagem!')


#===============================        OU             FORMA SIMPLIFICADA


d = float(input('Qual a distância em Km da viagem? '))
print ('Você está prestes a iniciar uma viagem de {}Km'.format(d))
p = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem, será de R${:.2f}'.format(p))

