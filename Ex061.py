# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# Da progressão usando a estrutura WHILE.


print('GERADOR DE P.A.')
print('=-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite sua razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += razão
    cont += 1
print('FIM.')


















