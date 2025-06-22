#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float (input('Primeira nota:'))
n2 = float (input ('Segunda nota:'))
s = n1 + n2                               #  CÁLCULO SIMPLES
m = s/ 2
print ('A média é {:.1f}!'.format (m))

#======================================          OU

n1 = float (input('Primeira nota:'))
n2 = float (input('Segunda nota:'))
var = (n1 + n2) / 2                       #  USANDO ORDEM DE PRECEDÊNCIA
print ('A média é {:.1f}!'.format (var))