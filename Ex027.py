# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EXEMPLO: Ana Maria de Souza
# Primeiro = Ana - / Último = Souza

n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()
print ('Primeiro nome: {}'.format(nome[0]))
print ('Último nome: {}'.format (nome[len(nome)-1]))