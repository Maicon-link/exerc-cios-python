# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final
# mostre os 10 primeiros termos dessa progressão.


primeiro = int(input('Digite o primeiro termo da P.A. : '))
razao = int(input('Digite a razão da P.A. : '))
decimo = primeiro + (10 - 1) * razao #10 - 1, pois você quer achar o decimo termo, essa é a fórmula matematica

for c in range(primeiro, decimo + razao, razao):
    formula = primeiro + razao

    print(c, end=' --> ')
print('FIM')
