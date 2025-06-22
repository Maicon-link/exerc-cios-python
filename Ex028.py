# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from random import randint
from time import sleep

#lista = [0, 1, 2, 3, 4, 5]
#num = random.choice(lista)

#u = int(input('Vou pensar em um número de 0 a 5, tente adivinhar qual é. '))
#print ('PROCESSANDO...')
#if u == num:
# print('Parabéns, você me venceu!')
#else:
#    print('Que pena, você perdeu, eu pensei no número {}.'.format(num))


#=============================       OU

computador = randint(0, 5) # FAZ O COMPUTADOR ''PENSAR''
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))



















