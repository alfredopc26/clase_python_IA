# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:51:46 2021

@author: Carlos Perez
"""

# Ejercicio 1


def calcularMasa(presion, vol, temp):
    
    masa = (presion * vol) / (0.37 * (temp + 460))
    
    return masa


print("Se va a calcular la masa \n")
presion = float(input("Digite la presion : \n"))
vol = float(input("Digite el volumen : \n"))
temp = float(input("Digite la temperatura : \n"))
print(f"La masa calculada es {calcularMasa(presion, vol, temp)}")
