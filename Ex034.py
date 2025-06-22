# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.


s = float(input('Digite um salário: R$'))
if s > 1250:
    a = s / 10 + s
    print('Com o aumento de 10% no salário, temos R${}'.format(a))
else:
    a = s * 0.15 + s
    print('Temos com aumento de 15% um salário de R${}'.format(a))


#================================     OU

salário = float(input('Digite o salário do funcionário: R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} agora vai ganhar R${:.2f}'.format(salário, novo))