# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a leta 'A'
# 2 - Em que posição ela aparece a primeira vez.
# 3 - Em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).strip().lower()
print ('Ela aparece {} vez(es).'.format(frase.count('a')))
print ('Ela aparece pela primeira vez na posição {}.'.format((frase.find('a'))))
print ('Ela aparece pela última vez na posição {}.'.format(frase.rfind('a')))