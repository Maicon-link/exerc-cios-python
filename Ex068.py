# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-=-' * 10)
print('VAMOS JOGAR ÍMPAR OU PAR!')
print('-=-' * 10)
v = 0
while True:
    computador = randint(1, 20)
    jogador = int(input('Escolha um valor: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
         print('Você VENCEU!')
         v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! Você venceu {v} vezes.')























































