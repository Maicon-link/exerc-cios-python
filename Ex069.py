# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.



pessoas = homens = mulheres = 0


while True:
     idade = int(input('Qual a idade da pessoa? '))
     sexo = ' '
     while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F] ')).upper().strip()[0]
     if idade >= 18:
       pessoas += 1
     if sexo == 'M':
       homens += 1
     if sexo == 'F' and idade < 20:
       mulheres += 1
       print(f'A pessoa tem {idade} anos e é do sexo {sexo}')
     escolha = ' '
     while escolha not in 'SN':
       print('=-=' * 15)
       escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
       print('=-=' * 15)
     if escolha == 'N':
           break
print(f'Temos {pessoas} pessoas maiores\n'
      f'Foram cadastrados {homens} homens\n'
      f'E {mulheres} mulheres com menos de 20 anos.')























