# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:19:21 2021

@author: Carlos Perez
"""

# Calcule el valor de Y indicando paso a paso como llego al resultado
# Punto 1
# Se crea la variable y con la ecuacion
y = ((5 + 2 - 5) ** 2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
# Esta se valida con un print
print(y)
# Este imprime como resultado -18
#
# Punto 2
# Se crean las variables z, n, m
z = 5
n = 3
m = z - n
# Se crea la ecuacion con la variable Y y las variables configuradas
Y = (((z + 2 - n) ** 2 * m + 8 / 2 - 30) / 2 * 5 - 3) ** 5 + 15 * 3 - 9 / 3
# Se imprime el resultado
print(Y)
# Este imprime el resultado 248874.0
#
# Punto 3
# Se crean las variables Z, N, M
z = 5
n = ((8 + 2 - 4) ** 2 * 5 + 8 + 7 / 2 - 30 * 5) / 2 * 5 - 3
m = z ** 2 * 3 + n
# Se crea la ecuacion con la variable Y junto con las demas
# Como la ecuacion es muy larga y supera la reglamentacion PEP8
# Debemos construir una variable auxiliar que nos facilite el trabajo
# a esta la llamaremos Y1
Y1 = ((z + 2 - n) ** 2 * m + 8 / 2 - 30)
Y = ((Y1 / 2 * 5 - 3) ** 5 + 15 * 3 - 9 / 3) ** 2 - 5 / 4
# Imprimimos el valor de Y
print(Y)
# Este nos da 7.373988851809673e+65