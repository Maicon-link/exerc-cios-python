#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


a = input ('Digite algo:')
print ('O tipo primitivo desse valor é', type(a))
print ('Só tem espaços? {}'.format (a.isspace()))
print ('É um número? {}'.format (a.isnumeric()))
print ('É alfanumérico?', a.isalnum())
print ('É um alfabético?', a.isalpha())
print ('Está em maiúsculo?', a.isupper())
print ('Está em minúsculas?', a.islower())
print ('Está capitalizado?', a.istitle())