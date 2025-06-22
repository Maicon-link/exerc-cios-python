# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, conforme a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

nasc = int(input('Qual o ano de nascimento do atleta? '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Atleta nasceu em {} \nTem {} anos \nSe enquadra na categoria MIRIM'.format(nasc, idade))
elif  idade <= 14:
    print('Atleta nasceu em {} \nTem {} anos  \nse enquadra na categoria INFANTIL'.format(nasc, idade))
elif idade <= 19:
    print('Atleta nasceu em {} \nTem {} anos \nQualificado para JUNIOR'.format(nasc, idade))
elif idade <= 25:
    print('Nasceu em {} \nTem a idade de {} anos \nClassifica como SÊNIOR'.format(nasc, idade))
else:
   print('Atleta nasceu em {} \nTem {} anos \nQualificado para a maior  categoria, MASTER'.format(nasc, idade))



