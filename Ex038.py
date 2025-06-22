# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# - O primeiro valor é maior    - O segundo valor é maior       - Não existe valor maior, os dois são iguais


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('\033[4;32mO primeiro valor é maior.\033[m')

elif b > a:
    print('\033[4;35mO segundo valor é maior.\033[m')
else:
    print('\033[4;33mNão existe valor maior, os dois são iguais!\033[m')

