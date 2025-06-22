# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiúsculas.
# 2 - O nome com todas as letras minúsculas.
# 3 - Quantas letras totais (sem considerar espaços).
# 4 - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')). strip()
print ('Analisando seu nome...')
print ('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print ('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print ('Seu nome tem ao todo {} letas.'.format(len(nome)-nome.count(' ')))
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# separa = nome.split()
# print ('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))