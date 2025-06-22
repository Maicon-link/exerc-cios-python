# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é condição de parada. No final mostre quantos números foram digitados
# e qual foi a soma entre eles (Desconsiderando o flag).


n = cont = soma = 0

n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:

    soma += n
    cont += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))


print('\033[0;35;40m*\033[m' * 20)
print('\033[0;34;40mPROGRAMA FINALIZADO.\033[m')
print('\033[0;35;40m*\033[m' * 20)
print('\033[4;33mO total de números digitados foi {} e a soma entre eles é {}\033[m'.format(cont, soma))


























