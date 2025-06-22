# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

v = float(input('Qual a velocidade do veículo ? (Km/h): '))
if v > 80:
    print('Você foi multado por exceder o limite de 80Km/h.')
    m = (v - 80) * 7
    print('Precisa pagar uma multa de R${:.2f}'.format(m))
else:
    print('Está tudo bem, continue assim!')


