# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

produto = float(input('Valor do produto: R$'))
print('\033[1;31m-=-\033[m' * 20)
print('''Temos essas formas de pagamento.
[ 1 ] À VISTA DINHEIRO/CHEQUE. 10 % de desconto 
[ 2 ] À VISTA NO CARTÃO. 5% de desconto
[ 3 ] EM ATÉ 2X NO CARTÃO. Preço normal.
[ 4 ] 3X OU MAIS NO CARTÃO. 20% de juros.''')
print('\033[1;31m-=-\033[m' * 20)

escolha = int(input('Escolha como deseja realizar o pagamento. '))
if escolha == 1:
   desconto = produto - (produto * 0.10)
   print('Produto com o valor de R${:.2f} tem um desconto de 10% e cai para R${:.2f}'.format(produto, desconto))
elif escolha == 2:
    desconto = produto - (produto * 0.05)
    print('Produto de R${:.2f} com desconto de 5% custa agora R${}'.format(produto, desconto))
elif escolha == 3:
    total = produto
    parcela = produto / 2
    print('O produto de R${:.2f} será dividido em duas parcelas de R${:.2f}.'.format(total, parcela))
elif escolha == 4:
    juros = produto + ( produto * 0.20)
    toparcelas = int(input('Quantas parcelas? '))
    parcela = juros / toparcelas
    print('Sua compra será parcelada em {}X de R${:.2f} com juros.'.format(toparcelas, parcela))
else:
    print('\033[1;31;40mNão existe essa opção. Escolha algo válido.\033[m')
