# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for


n = int(input('Escolha um número: '))
for c in range(0, 11):
    print(' {} X {:2} = {} '.format(n, c, n * c))





