# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido quando o número
# solicitado for negativo.





while True:
    t = int(input('Quer ver a tabuada de qual número? '))
    if t < 0:
        break
    print('-' * 30)
    for c in range (0, 11):
        print(f'{t} x {c} = {t * c}')
    print('-' * 30)
print('PROGRAMA ENCERRADO, Volte sempre!')



















