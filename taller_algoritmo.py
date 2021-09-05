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


# Ejercicio 2

def calcularNumPulsaciones(edad):
    
    pulsaciones = (200 - edad) / 10
    
    return pulsaciones

print("Se va a calcular el numero de pulsaciones.")
edad = int(input("Digite su edad: \n"))
print("El numero de pulsaciones que debe tener por 10 seg es :")
print(calcularNumPulsaciones(edad))


# Ejercicio 3

def calcularPorcentaje(dinTotal, dinInver):
    
    porcentaje = (dinInver * 100) / dinTotal
    
    return porcentaje

print("Se va a calcular el porcentaje de inversion de cada persona.")
print("Persona 1")
persona1 = float(input("Digite su dinero a invertir: \n"))
print("Persona 2")
persona2 = float(input("Digite su dinero a invertir: \n"))
print("Persona 3")
persona3 = float(input("Digite su dinero a invertir: \n"))
dinTotal = persona1 + persona2 + persona3
print("El porcentaje de la Persona 1 es: ")
print(f"% {calcularPorcentaje(dinTotal, persona1)}")
print("El porcentaje de la Persona 2 es: ")
print(f"% {calcularPorcentaje(dinTotal, persona2)}")
print("El porcentaje de la Persona 3 es: ")
print(f"% {calcularPorcentaje(dinTotal, persona3)}")

