# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
#  e que se encontram no intervalo de 1 até 500.


s = 0  # Contador de soma
for num in range(1, 501):  # de 1 até 500
    if num % 2 != 0:  # Ímpares
        if num % 3 == 0:  # Ímpares múltiplos de 3
            s += num  # soma = soma + num
print("A soma dos múltiplos é: {}.".format(s))

#==========================       OU

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1 # ou contador += 1
        soma = soma + c   # ou soma += c
print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))















