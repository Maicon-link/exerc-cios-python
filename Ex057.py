# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# M ou F. Peça a digitação novamente até ter um valor correto.


sexo = str(input('Qual o seu sexo? [M/F] ')).lower().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().lower()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))













