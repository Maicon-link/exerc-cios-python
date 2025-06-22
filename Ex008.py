#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida =  float (input('Metros:'))
cm = medida * 100
mm = medida * 1000
print ('{} metros possui {:.0f} centímetros e {:.0f} milímetros!'.format(medida, cm, mm))

