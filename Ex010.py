#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# CONSIDERE: US$1,00 = R$3,27

r = float (input ('Quantos reais? R$'))
v = r / 3.27
print ('Com R${:.2f}, você pode converter em US${:.2f} '.format(r, v))
