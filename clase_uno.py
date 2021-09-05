# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:51:46 2021

@author: Carlos Perez
"""

# Sume dos numeros e imprima su resultado 

numA = input('Para la suma de A + B. Digite el numero A: \n')
numB = input('Para la suma de A + B. Digite el numero B: \n')

print("El resultado es: " + str(int(numA) + int(numB)))


# Numero elevado al cuadrado

print('Vamos a elevar un numero al cuadrado.')
num = float(input('Digite el numero que desea elevar al cuadrado:'))
pow_num = pow(num, 2)

print(f'Su numero elevado al cuadrado es : {pow_num}')


# Tomar valor de un producto, aplicar el 20%
# de descuento, imrpima el valor del producto inicial,
# el valor con descuento y valor ahorrado

print('Calcular descuento de producto.')

product = float(input('Digite el valor del producto: \n'))
discont = product * 0.20
total_prod = product - discont

print(f'EL valor inicial del producto es: ${product}')
print(f'EL valor con descuento del producto es: ${total_prod}')
print(f'EL valor ahorrado cpn el descuento es: ${discont}')