# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = float (input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
alugado = dias * 60
quilometros = km * 0.15
valor = alugado + quilometros
print ('O total a pagar é de R${}'.format(valor))


#========================      OU

dias = float(input('Quantos dias alugado? '))
km = float (input('Quantos Km rodados? '))
valor = dias * 60 + (km * 0.15)
print ('Com {} dias alugado e {}Km rodados o valor a pagar é de R${:.2f}\nDebito ou Crédito?'.format(dias, km, valor))