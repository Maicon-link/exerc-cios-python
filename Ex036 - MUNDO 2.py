#   Escreva programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

v = float (input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salário? R$'))
a = float(input('Em quantos anos você vai pagar?'  ))

quant_prestação = a * 12
prestação_mensal = v / quant_prestação

if s * 0.3 > prestação_mensal:
    print('Muito bem, seu empréstimo foi aprovado!'
          '\nvocê pagará {} prestações de R${:.2f} por {} anos'.
    format(quant_prestação, prestação_mensal, a))

else:
    print('O empréstimo foi negado!')


#==================================== OU

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo foi NEGADO!')
























