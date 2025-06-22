# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000,00
# C) Qual é o nome do produto mais barato.


print('--' * 20)
print('         \033[4;34;40m[*! SHOPPING CENTER !*]\033[m')
print('--' * 20)
quant = total = menor = cont = 0
barato = ''

while True:
   nome = str(input('Nome do produto: '))
   preço = float(input('Valor do produto: R$'))
   cont += 1
   total += preço
   if preço > 1000:
      quant += 1
   if cont == 1 or preço < menor:
      menor = preço
      barato = nome
   escolha = ' '
   while escolha not in 'SN':
      escolha = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
   if escolha == 'N':
       break
print(f'O total gasto na loja é R${total:.2f}\n' f'{quant} produtos custam mais de R$1000,00\n'
      f'{barato} é o produto mais barato, custando R${menor:.2f}. ')

















































