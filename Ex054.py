# Crie um programa que leia o ano de nascimento de sete pessoas. No final
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

#nasc = int(input('Data de nascimento: '))
#idade = date.today().year - nasc
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Data de nascimento da {}º pessoa: '.format(c)))
    idade = date.today().year - nasc

    if idade < 18:
        menor += 1

    else:
        maior += + 1



print('{} Menores de idade.'.format(menor))
print('{} Maiores de idade.'.format(maior))