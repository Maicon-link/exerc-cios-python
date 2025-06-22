# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import emoji
from time import sleep




for c in range(10, 0,  - 1):
    sleep(1.5)
    print(c)

print('FELIZ ANO NOVOOOOOOOOO!!!!')

print (emoji.emojize(':fogos_de_artifício: ' * 20, language="pt"))