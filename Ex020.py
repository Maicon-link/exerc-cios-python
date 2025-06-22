# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')
a5 = input('Nome do 5º aluno: ')
Lista = (a1, a2, a3, a4, a5)

print ('A ordem de apresentação é: {}'.format(random.sample(Lista, 5)))


